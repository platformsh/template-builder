const config = require("platformsh-config").config();

const credentials = config.credentials('postgresdatabase');

let settings = {
  client: "postgres",
  host: credentials.ip,
  port: credentials.port,
  database: credentials.path,
  username: credentials.username,
  password: credentials.password
};

module.exports = {
  defaultConnection: 'default',
  connections: {
    default: {
      connector: 'bookshelf',
      settings,
      options: {
        ssl: false,
        debug: false,
        acquireConnectionTimeout: 100000,
        pool: {
          min: 0,
          max: 10,
          createTimeoutMillis: 30000,
          acquireTimeoutMillis: 600000,
          idleTimeoutMillis: 20000,
          reapIntervalMillis: 20000,
          createRetryIntervalMillis: 200
        }
      }
    }
  }
};
