const path = require("path");
const config = require("platformsh-config").config();

let dbRelationship = "postgresdatabase";

// Strapi default sqlite settings.
module.exports = ({ env }) => ({
  connection: {
    client: "sqlite",
    connection: {
      filename: path.join(
        __dirname,
        "..",
        env("DATABASE_FILENAME", ".tmp/data.db")
      ),
    },
    useNullAsDefault: true,
  },
});

if (config.isValidPlatform() && !config.inBuild()) {
  // Platform.sh database configuration.
  const credentials = config.credentials(dbRelationship);
  console.log(
    `Using Platform.sh configuration with relationship ${dbRelationship}.`
  );

  settings = {
    connection: {
      client: "postgres",
      connection: {
        host: credentials.ip,
        port: credentials.port,
        database: credentials.path,
        username: credentials.username,
        password: credentials.password,
      },
    },
  };

  options = ({ env }) => ({
    ssl: env.bool("DATABASE_SSL", false),
    debug: false,
    acquireConnectionTimeout: 100000,
    pool: {
      min: 0,
      max: 10,
      createTimeoutMillis: 30000,
      acquireTimeoutMillis: 600000,
      idleTimeoutMillis: 20000,
      reapIntervalMillis: 20000,
      createRetryIntervalMillis: 200,
    },
  });
} else {
  if (config.isValidPlatform()) {
    // Build hook configuration message.
    console.log(
      "Using default configuration during Platform.sh build hook until relationships are available."
    );
  } else {
    // Strapi default local configuration.
    console.log(
      "Not in a Platform.sh Environment. Using default local sqlite configuration."
    );
  }
}
