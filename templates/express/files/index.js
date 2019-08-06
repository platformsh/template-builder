var express = require('express');
const mysql = require('mysql2/promise');
const config = require("platformsh-config").config();

// Define the application.
var app = express();

async function mariadbTest() {
    try {

        var results = [];

        // Connect to MariaDB.
        const credentials = config.credentials('database');
        const connection = await mysql.createConnection({
            host: credentials.host,
            port: credentials.port,
            user: credentials.username,
            password: credentials.password,
            database: credentials.path,
        });

        results[0] = `Connected to MariaDB at ${credentials.host}.`

        // Add the table.
        tableName = "userinfo";

        let sql = '';

        // Create a table.
        sql = `CREATE TABLE IF NOT EXISTS userinfo (
          uid INT(10) NOT NULL AUTO_INCREMENT,
          username VARCHAR(64) NULL DEFAULT NULL,
          departname VARCHAR(128) NULL DEFAULT NULL,
          created DATE NULL DEFAULT NULL,
          PRIMARY KEY (uid)
        ) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;`;

        await connection.query(sql);

        results[1] = "Created table 'userinfo'.";

        // Insert data.
        values = `(username, departname, created)`;
        newRow = `('platform', 'Deploy Friday', '2019-06-17')`;

        sql = "INSERT INTO userinfo (username, departname, created) VALUES ('platform', 'Deploy Friday', '2019-06-17')"

        await connection.query(sql);

        // Read the data.
        sql = "SELECT * FROM userinfo";
        let [rows] = await connection.query(sql);

        let output = '';

        if (rows.length > 0) {
          rows.forEach((row) => {
            output += `  - uid (1): ${row.uid}
  - username (platform): ${row.username}
  - departname (Deploy Friday): ${row.departname}
  - created (2019-06-17): ${row.created}`;
          });
        }

        results[2] = output;

        // Drop the table.
        sql = "DROP TABLE userinfo";
        await connection.query(sql);

        return results;

      } catch(error) {
        return Promise.reject(error);
      }
}

// Define the main route.
app.get('/', async function(req, res){

  let results = await mariadbTest();

  outputString = `Hello, World! - A simple Express web framework template for Platform.sh


MariaDB Tests:

* Connect:
  - ${results[0]}

* Add table:
  - ${results[1]}

* Add row to table and verify:
${results[2]}
`;

  res.set('Content-Type', 'text/plain');
  res.send(outputString);


});

// Get PORT and start the server
app.listen(config.port, function() {
  console.log(`Listening on port ${config.port}`)
});
