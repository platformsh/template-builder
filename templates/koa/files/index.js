const mysql = require('mysql2/promise');
const config = require("platformsh-config").config();
const Koa = require('koa');

const app = module.exports = new Koa();

// Connect to MariaDB.
async function openConnection () {
  const credentials = config.credentials('database');
  return await mysql.createConnection({
      host: credentials.host,
      port: credentials.port,
      user: credentials.username,
      password: credentials.password,
      database: credentials.path,
  });
};

// Drop the table and retrieve result information.
function dropTable (connection) {
  let results = connection.execute("DROP TABLE platforminfo")
  .then((result) => {
    return result;
  })
  return results
};

app.use(async function(ctx) {

  // Connect to MariaDB.
  let connection = await openConnection();

  // Create the table.
  connection.execute(
    `CREATE TABLE IF NOT EXISTS platforminfo (
      uid INT(10) NOT NULL AUTO_INCREMENT,
      username VARCHAR(64) NULL DEFAULT NULL,
      departname VARCHAR(128) NULL DEFAULT NULL,
      created DATE NULL DEFAULT NULL,
      PRIMARY KEY (uid)
    ) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;`
  );

  // Insert data.
  connection.execute(
    "INSERT INTO platforminfo (username, departname, created) VALUES ('platform', 'Deploy Friday', '2019-06-17')"
  );

  // Read the data.
  let [rows] = await connection.query("SELECT * FROM platforminfo");

  // Drop the table.
  let dropped_result = await dropTable(connection);

  // Make the output.
  var outputString = `Hello, World! - A simple Koa web framework template for Platform.sh

MariaDB Tests:

* Connect and add row:
  - Row ID (1): ${rows[0].uid}
  - Username (platform): ${rows[0].username}
  - Department (Deploy Friday): ${rows[0].departname}
  - Created (2019-06-17): ${rows[0].created}
* Delete row:
  - Status (0): ${dropped_result[0].warningStatus}`;

  ctx.body = outputString;

});

if (!module.parent) {
  app.listen(config.port)
};
