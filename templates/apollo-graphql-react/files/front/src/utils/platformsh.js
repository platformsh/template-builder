class NotValidPlatformError extends Error {}

class BuildTimeVariableAccessError extends Error {}

class NoCredentialFormatterFoundError extends Error {}

/**
 * Decodes a Platform.sh environment variable.
 *
 * @param {string} value
 *   Base64-encoded JSON (the content of an environment variable).
 *
 * @return {any}
 *   An associative array (if representing a JSON object), or a scalar type.
 */
function decode(value) {
    return JSON.parse(Buffer.from(value, 'base64'));
}

/**
 * Class representing a Platform.sh environment configuration.
 */
class Config {

    constructor(env = null, prefix = 'PLATFORM_') {
        this.environmentVariables = env || process.env;
        this.envPrefix = prefix;

        // Node doesn't support pre-defined object properties in classes, so
        // this is mostly for documentation but also to ensure there's always
        // a legal defined value.
        this.routesDef = [];
        this.relationshipsDef = [];
        this.variablesDef = [];
        this.applicationDef = [];
        this.credentialFormatters = {};

        let routes = this._getValue('ROUTES');
        if (routes) {
            this.routesDef = decode(routes);
            for (let [url, route] of Object.entries(this.routesDef)) {
                route['url'] = url;
            }
        }

        let relationships = this._getValue('RELATIONSHIPS');
        if (relationships) {
            this.relationshipsDef = decode(relationships);
        }

        this.registerFormatter('solr-node', nodeSolrFormatter);
        this.registerFormatter('mongodb', mongodbFormatter);
        this.registerFormatter('puppeteer', puppeteerFormatter);

        let variables = this._getValue('VARIABLES');
        if (variables) {
            this.variablesDef = decode(variables);
        }

        let application = this._getValue('APPLICATION');
        if (application) {
            this.applicationDef = decode(application);
        }
    }

    /**
     * Callback for formatting a set of credentials for a particular library.
     *
     * @callback registerFormatterCallback
     * @param {object} credentials
     *   A credential array, as returned by the credentials() method.
     * @return {mixed}
     *   The formatted credentials. The format will vary depending on the
     *   client library it is intended for, but usually either a string or an object.
     */

    /**
     * Adds a credential formatter to the configuration.
     *
     * A credential formatter is responsible for formatting the credentials for a relationship
     * in a way expected by a particular client library.  For instance, it can take the credentials
     * from Platform.sh for a PostgreSQL database and format them into a URL string expected by
     * a particular PostgreSQL client library.  Use the formattedCredentials() method to get
     * the formatted version of a particular relationship.
     *
     * @param {string} name
     *   The name of the formatter.  This may be any arbitrary alphanumeric string.
     * @param {registerFormatterCallback} formatter
     *   A callback function that will format relationship credentials for a specific client library.
     * @return {Config}
     *   The called object, for chaining.
     */
    registerFormatter(name, formatter) {
        this.credentialFormatters[name] = formatter;

        return this;
    }

    /**
     * Returns credentials for the specified relationship as formatted by the specified formatter.
     *
     * @param {string} relationship
     *   The relationship whose credentials should be formatted.
     * @param {string} formatter
     *   The registered formatter to use.  This must match a formatter previously registered
     *   with registerFormatter().
     * @return mixed
     *   The credentials formatted with the given formatter.
     */
    formattedCredentials(relationship, formatter) {
        if (!this.credentialFormatters.hasOwnProperty(formatter)) {
            throw new NoCredentialFormatterFoundError(`There is no credential formatter named "${formatter}" registered. Did you remember to call registerFormatter()?`);
        }

        return this.credentialFormatters[formatter](this.credentials(relationship));
    }

    /**
     * Checks whether the code is running on a platform with valid environment variables.
     *
     * @return {boolean}
     *   True if configuration can be used, false otherwise.
     */
    isValidPlatform() {
        return Boolean(this._getValue('APPLICATION_NAME'));
    }

    /**
     * Checks whether the code is running in a build environment.
     *
     * If false, it's running at deploy time.
     *
     * @return {boolean}
     */
    inBuild() {
        return this.isValidPlatform() && !this._getValue('ENVIRONMENT');
    }

    /**
     * Checks whether the code is running in a runtime environment.
     *
     * @return {boolean}
     */
    inRuntime() {
        return this.isValidPlatform() && Boolean(this._getValue('ENVIRONMENT'));
    }

    /**
     * Determines if the current environment is a Platform.sh Dedicated environment.
     *
     * @deprecated
     *
     * The Platform.sh "Enterprise" will soon be referred to exclusively as
     * "Dedicated". the `onEnterprise` method remains available for now, but it
     * will be removed in a future version of this library.
     *
     * It is recommended that you update your projects to use `onDedicated` as
     * soon as possible.
     *
     * @return {boolean}
     *   True on an Dedicated environment, False otherwise.
     */
    onEnterprise() {
        return this.onDedicated();
    }

    /**
     * Determines if the current environment is a Platform.sh Dedicated environment.
     *
     * @return {boolean}
     *   True on an Dedicated environment, False otherwise.
     */
    onDedicated() {
        return this.isValidPlatform() && this._getValue('MODE') === 'enterprise';
    }

    /**
     * Determines if the current environment is a production environment.
     *
     * Note: There may be a few edge cases where this is not entirely correct on Enterprise,
     * if the production branch is not named `production`.  In that case you'll need to use
     * your own logic.
     *
     * @return {boolean}
     *   True if the environment is a production environment, false otherwise.
     *   It will also return false if not running on Platform.sh or in the build phase.
     */
    onProduction() {
        if (!this.inRuntime()) {
            return;
        }

        let prodBranch = this.onEnterprise() ? 'production' : 'master';

        return this._getValue('BRANCH') === prodBranch;
    }

    /**
     * Returns the routes definition.
     *
     * @return {object}
     *   The routes definition object.
     * @throws {Error}
     *   If the routes are not accessible due to being in the wrong environment.
     */
    routes() {
        if (this.inBuild()) {
            throw new BuildTimeVariableAccessError('Routes are not available during the build phase.');
        }

        if (!this.routesDef) {
            throw new NotValidPlatformError('No routes defined.  Are you sure you are running on Platform.sh?');
        }

        return this.routesDef;
    }

    /**
     * Returns the primary route.
     *
     * The primary route is the one marked primary in `routes.yaml`, or else
     * the first non-redirect route in that file if none are marked.
     *
     * @return {object}
     *   The route definition.  The generated URL of the route is added as a "url" key.
     */
    getPrimaryRoute() {
        // eslint-disable-next-line no-unused-vars
        for (const [url, route] of Object.entries(this.routes())) {
            if (route.primary === true) {
                return route;
            }
        }

        throw new Error(`No primary route found. This isn't supposed to happen.`);
    }

    /**
     * Returns just those routes that point to a valid upstream.
     *
     * This method is similar to routes(), but filters out redirect routes that are rarely
     * useful for app configuration.  If desired it can also filter to just those routes
     * whose upstream is a given application name.  To retrieve routes that point to the
     * current application where the code is being run, use:
     *
     * routes =  config.getUpstreamRoutes(config.applicationName);
     *
     * @param {string|null} appName
     *   The name of the upstream app on which to filter, if any.
     * @return {object}
     *   An object map of route definitions.
     */
    getUpstreamRoutes(appName = null) {
        // Because routes is an object/dictionary, we can't just filter it directly.
        // Verbose way it is.

        const routes = this.routes();
        const filter = route => {
            return route.type === 'upstream'
                // On Dedicated, the upstream name sometimes is `app:http` instead of just `app`.
                // If no name is specified then don't bother checking.
                && (!appName || appName === route.upstream.split(':')[0]);
        };

        let ret = {};

        Object.keys(routes).forEach(function(key) {
            if (filter(routes[key])) {
                ret[key] = routes[key];
            }
        });

        return ret;
    }

    /**
     * Returns a single route definition.
     *
     * Note: If no route ID was specified in routes.yaml then it will not be possible
     * to look up a route by ID.
     *
     * @param {string} id
     *   The ID of the route to load.
     * @return {object}
     *   The route definition.  The generated URL of the route is added as a "url" key.
     * @throws {Error}
     *   If there is no route by that ID, an exception is thrown.
     */
    getRoute(id) {
        // eslint-disable-next-line no-unused-vars
        for (const [url, route] of Object.entries(this.routes())) {
            if (route.id === id) {
                return route;
            }
        }

        throw new Error(`No such route id found: ${id}`);
    }

    /**
     * Determines if a relationship is defined, and thus has credentials available.
     *
     * @param {string} relationship
     *   The name of the relationship to check.
     * @return {boolean}
     *   True if the relationship is defined, false otherwise.
     */
    hasRelationship(relationship) {
        return Boolean(this.relationshipsDef[relationship]);
    }

    /**
     * Retrieves the credentials for accessing a relationship.
     *
     * The relationship must be defined in the .platform.app.yaml file.
     *
     * @param {string} relationship
     *   The relationship name as defined in .platform.app.yaml.
     * @param {int} index
     *   The index within the relationship to access.  This is always 0, but reserved
     *   for future extension.
     * @return {object}
     *   The credentials array for the service pointed to by the relationship.
     * @throws {Error}
     *   Thrown if called in a context that has no relationships (eg, in build)
     * @throws {RangeError}
     *   If the relationship/index pair requested does not exist.
     */
    credentials(relationship, index = 0) {
        if (!this.relationshipsDef) {
            if (this.inBuild()) {
                throw new BuildTimeVariableAccessError('Relationships are not available during the build phase.');
            }
            throw new NotValidPlatformError('No relationships are defined. Are you sure you are on Platform.sh?'
                + '  If you\'re running on your local system you may need to create a tunnel'
                + ' to access your environment services.  See https://docs.platform.sh/gettingstarted/local/tethered.html');
        }

        if (!this.relationshipsDef[relationship]) {
            throw new RangeError(`No relationship defined: ${relationship}.  Check your .platform.app.yaml file.`);
        }
        if (!this.relationshipsDef[relationship][index]) {
            throw new RangeError(`No index ${index} defined for relationship: ${relationship}.  Check your .platform.app.yaml file.`);
        }

        return this.relationshipsDef[relationship][index];
    }

    /**
     * Returns a variable from the VARIABLES array.
     *
     * Note: variables prefixed with `env:` can be accessed as normal environment variables.
     * This method will return such a variable by the name with the prefix still included.
     * Generally it's better to access those variables directly.
     *
     * @param {string} name
     *   The name of the variable to retrieve.
     * @param {any} defaultValue
     *   The default value to return if the variable is not defined. Defaults to null.
     * @return mixed
     *   The value of the variable, or the specified default.  This may be a string or an array.
     */
    variable(name, defaultValue = null) {
        return this.variablesDef.hasOwnProperty(name) ? this.variablesDef[name] : defaultValue;
    }

    /**
     * Returns the full variables array.
     *
     * If you're looking for a specific variable, the variable() method is a more robust option.
     * This method is for cases where you want to scan the whole variables list looking for a pattern.
     *
     * @return {object}
     *   The full variables definition.
     */
    variables() {

        return this.variablesDef;
    }

    /**
     * Returns the application definition object.
     *
     * This is, approximately, the .platform.app.yaml file as a nested array.  However, it also
     * has other information added by Platform.sh as part of the build and deploy process.
     *
     * @return {object}
     *   The application definition object.
     */
    application() {
        if (!this.applicationDef) {
            throw new NotValidPlatformError('No application definition is available.  Are you sure you are running on Platform.sh?');
        }

        return this.applicationDef;
    }

    /**
     * The absolute path to the application directory.
     *
     * @returns {string}
     */
    get appDir() {
        return this._buildValue('APP_DIR', 'appDir');
    }

    /**
     * The name of the application container, as configured in the .platform.app.yaml file.
     *
     * @returns {string}
     */
    get applicationName() {
        return this._buildValue('APPLICATION_NAME', 'applicationName');
    }

    /**
     * The project ID.
     *
     * @returns {string}
     */
    get project() {
        return this._buildValue('PROJECT', 'project');
    }

    /**
     * The ID of the tree the application was built from.
     *
     * This is essentially the SHA hash of the tree in Git. If you need a unique ID
     * for each build for whatever reason this is the value you should use.
     *
     * @returns {string}
     */
    get treeId() {
        return this._buildValue('TREE_ID', 'treeId');
    }

    /**
     * The project project entropy value.
     *
     * This random value is created when the project is first created, which is then stable
     * throughout the project’s life. It should be used for application-specific unique-instance
     * hashing.
     *
     * @returns {string}
     */
    get projectEntropy() {
        return this._buildValue('PROJECT_ENTROPY', 'projectEntropy');
    }

    /**
     * The name of the Git branch.
     *
     * @returns {string}
     */
    get branch() {
        return this._runtimeValue('BRANCH', 'branch');
    }

    /**
     * The name of the environment generated by the name of the Git branch.
     *
     * @returns {string}
     */
    get environment() {
        return this._runtimeValue('ENVIRONMENT', 'environment');
    }

    /**
     * The absolute path to the web document root, if applicable.
     *
     * @returns {string}
     */
    get documentRoot() {
        return this._runtimeValue('DOCUMENT_ROOT', 'documentRoot');
    }

    /**
     * The SMTP host to use for sending email.
     *
     * If empty, it means email sending is disabled in this environment.
     *
     * @returns {string}
     */
    get smtpHost() {
        return this._runtimeValue('SMTP_HOST', 'smtpHost');
    }

    /**
     * The TCP port number the application should listen to for incoming requests.
     *
     * @returns {string}
     */
    get port() {
        if (this.inBuild()) {
            throw new BuildTimeVariableAccessError(`The "port" variable is not available during build time.`);
        }
        let value = this.environmentVariables['PORT'];
        if (!value) {
            throw new NotValidPlatformError(`The "port" variable is not defined. Are you sure you're running on Platform.sh?`);
        }
        return value;
    }

    /**
     * The Unix socket the application should listen to for incoming requests.
     *
     * @returns {string}
     */
    get socket() {
        if (this.inBuild()) {
            throw new BuildTimeVariableAccessError(`The "socket" variable is not available during build time.`);
        }
        let value = this.environmentVariables['SOCKET'];
        if (!value) {
            throw new NotValidPlatformError(`The "socket" variable is not defined. Are you sure you're running on Platform.sh?`);
        }
        return value;
    }

    /**
     * Returns a build-safe variable's value if defined, or throws an error.
     *
     * @param {string} property
     *   The name of the environment variable, without prefix.
     * @param {string} humanName
     *   The human-readable name of the property to be used in error messages.
     * @return {string}
     *   The variable's value.
     * @private
     */
    _buildValue(property, humanName) {
        let value = this._getValue(property);
        if (!value) {
            throw new NotValidPlatformError(`The "${humanName}" variable is not defined. Are you sure you're running on Platform.sh?`);
        }
        return value;
    }

    /**
     * Returns a runtime-only variable's value if defined, or throws an error.
     *
     * @param {string} property
     *   The name of the environment variable, without prefix.
     * @param {string} humanName
     *   The human-readable name of the property to be used in error messages.
     * @return {string}
     *   The variable's value.
     * @private
     */    _runtimeValue(property, humanName) {
        if (this.inBuild()) {
            throw new BuildTimeVariableAccessError(`The "${humanName}" variable is not available during build time.`);
        }
        let value = this._getValue(property);
        if (!value) {
            throw new NotValidPlatformError(`The "${humanName}" variable is not defined. Are you sure you're running on Platform.sh?`);
        }
        return value;
    }

    /**
     * Reads an environment variable, taking the prefix into account.
     *
     * @param {string} name
     *   The variable to read.
     * @return {string|null}
     */
    _getValue(name) {
        let checkName = this.envPrefix + name.toUpperCase();

        return this.environmentVariables[checkName] || null;
    }
}


/**
 * Returns a connection object appropriate for the solr-node library.
 *
 * @param credentials
 *   A solr credentials object.
 * @returns {object}
 *   A credentials object to pass to new SolrNode().
 */
function nodeSolrFormatter(credentials) {
    return {
        host: credentials.host,
        port: credentials.port,
        core: credentials.path.split('/').slice(-1)[0],
        protocol: 'http'
    }
}

/**
 * Returns a connection string appropriate for the mongodb library.
 *
 * @param credentials
 *   A mongodb credentials object
 * @returns {string}
 *   A connection string to pass to MongoClient.connect().
 */
function mongodbFormatter(credentials) {
    return `mongodb://${credentials["username"]}:${credentials["password"]}@${credentials["host"]}:${credentials["port"]}/${credentials["path"]}`;
}

/**
 * Returns a connection string appropriate for Puppeteer and headless Chrome.
 * @param cretentials
 *   A chrome-headless credentials object
 * @returns {string}
 *   A connection string to pass to puppeteer.connect().
 */
function puppeteerFormatter(credentials) {
    return `http://${credentials["ip"]}:${credentials["port"]}`;
}

/**
 * Creates a new Config instance that represents the current environment.
 *
 * @returns {Config}
 */
export function config({ env, envPrefix } = {}) {
    return new Config(env, envPrefix);
}

// In testing, also expsoe the class so we can pass in test data.
if (process.env.NODE_ENV === 'test') {
    module.exports.Config = Config;
}
