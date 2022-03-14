const path = require("path");

let connection;
let db_relationship = 'database';

// Helper function for decoding Platform.sh base64 encoded JSON variables.
function decode(value) {
  return JSON.parse(Buffer.from(value, 'base64'));
}

if (!process.env.PLATFORM_RELATIONSHIPS) {
  if (process.env.PLATFORM_PROJECT) {
    console.log("In Platform.sh build hook. Using default SQLite configuration until services are available.");
  } else {
    console.log("Configuring local SQLite connection. \n\nIf you meant to use a tunnel, be sure to run \n\n$ export PLATFORM_RELATIONSHIPS=\"$(platform tunnel:info --encode)\"\n\nto connect to that service.\n");
  }
  // Define the SQLite connection.
  connection = {
    connection: {
      client: "sqlite",
      connection: {
        filename: path.join(
          __dirname,
          "..",
          process.env.DATABASE_FILENAME || ".tmp/data.db"
        ),
      },
      useNullAsDefault: true,
    },
  };
} else {
    if (process.env.PLATFORM_PROJECT) {
      console.log("In Platform.sh deploy hook. Using defined service configuration.");
    } else {
      console.log("Using tunnel for local development.")
    }
    // Define the managed service connection.
    let credentials = decode(process.env.PLATFORM_RELATIONSHIPS)[db_relationship][0];
    // Option 1. PostgreSQL.
    // On Platform.sh, PostgreSQL configuration assumes the following in your .platform/services.yaml file:
    // 
    // dbpostgres:
    //    type: postgresql:12
    //    disk: 256
    // 
    // As well as a relationship defined in your .platform.app.yaml file as follows:
    // 
    // relationships:
    //    database: "dbpostgres:postgresql"
    if (credentials.scheme == 'pgsql') {
        console.log("PostgreSQL detected.");
        let postgres_pool = {
            min: 0,
            max: 10,
            acquireTimeoutMillis: 600000,
            createTimeoutMillis: 30000,
            idleTimeoutMillis: 20000,
            reapIntervalMillis: 20000,
            createRetryIntervalMillis: 200,
          };
        connection = {
            connection: {
              client: "postgres",
              connection: {
                host: credentials.ip,
                port: credentials.port,
                database: credentials.path,
                user: credentials.username,
                password: credentials.password,
                ssl: false,
              },
              debug: false,
              postgres_pool,
            },
          };
      // Option 2. Oracle MySQL.
      // On Platform.sh, Oracle MySQL configuration assumes the following in your .platform/services.yaml file:
      // 
      // dbmysql:
      //    type: oracle-mysql:8.0
      //    disk: 256
      // 
      // As well as a relationship defined in your .platform.app.yaml file as follows:
      // 
      // relationships:
      //    database: "dbmysql:mysql"
      } else if (credentials.scheme == 'mysql') {
        console.log("MySQL detected.");
        connection = {
            connection: {
              client: "mysql",
              connection: {
                host: credentials.ip,
                port: credentials.port,
                database: credentials.path,
                user: credentials.username,
                password: credentials.password,
                ssl: false,
              },
              debug: false,
            },
          };
    }
}

// Export the connection to Strapi.
module.exports = ({ env }) => connection;
