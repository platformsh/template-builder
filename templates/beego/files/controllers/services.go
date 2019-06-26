package controllers

import (
        "fmt"
        "database/sql"
        _ "github.com/go-sql-driver/mysql"
        sqldsn "github.com/platformsh/config-reader-go/v2/sqldsn"
        config "github.com/platformsh/template-beego/conf"
)

type MySQLTestController struct {
        MainController
}

func (c *MySQLTestController) Get() {

  // Accessing the database relationship Credentials struct
  credentials, err := config.PshConfig.Credentials("database")
  if err != nil {
    panic(err)
  }

  // Using the sqldsn formatted credentials package
  formatted, err := sqldsn.FormattedCredentials(credentials)
  if err != nil {
    panic(err)
  }

  db, err := sql.Open("mysql", formatted)
  if err != nil {
    panic(err)
  }
  defer db.Close()

  // Force MySQL into modern mode.
  db.Exec("SET NAMES=utf8")
  db.Exec("SET sql_mode = 'ANSI,STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,ONLY_FULL_GROUP_BY'")

  _, err = db.Exec("DROP TABLE IF EXISTS userinfo")
  if err != nil {
    panic(err)
  }

  _, err = db.Exec(`CREATE TABLE userinfo (
      uid INT(10) NOT NULL AUTO_INCREMENT,
      username VARCHAR(64) NULL DEFAULT NULL,
      departname VARCHAR(128) NULL DEFAULT NULL,
      created DATE NULL DEFAULT NULL,
      PRIMARY KEY (uid)
      ) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;`)
  if err != nil {
		panic(err)
	}
  // insert
  stmt, err := db.Prepare("INSERT userinfo SET username=?,departname=?,created=?")
  if err != nil {
    panic(err)
  }

  res, err := stmt.Exec("platform", "Deploy Friday", "2019-06-17")
  if err != nil {
    panic(err)
  }

  id, err := res.LastInsertId()
  if err != nil {
    panic(err)
  }

  // update
  stmt, err = db.Prepare("update userinfo set username=? where uid=?")
  if err != nil {
    panic(err)
  }

  res, err = stmt.Exec("goPlatformsh", id)
  if err != nil {
    panic(err)
  }

  affect, err := res.RowsAffected()
  if err != nil {
    panic(err)
  }

  // query
  rows, err := db.Query("SELECT * FROM userinfo")
  if err != nil {
    panic(err)
  }

  var uid int
  var username string
  var department string
  var created string
  for rows.Next() {
    err = rows.Scan(&uid, &username, &department, &created)
    if err != nil {
      panic(err)
    }
  }

  // delete
  stmt, err = db.Prepare("delete from userinfo where uid=?")
  if err != nil {
    panic(err)
  }

  res, err = stmt.Exec(id)
  if err != nil {
    panic(err)
  }

  affect, err = res.RowsAffected()
  if err != nil {
    panic(err)
  }

  status := fmt.Sprintf(`Hello, World! - A simple Beego web framework template for Platform.sh


  MySQL Tests:

  * Connect and add row:
   - Row ID (1): %d
   - Username (goPlatformsh): %s
   - Department (Deploy Friday): %s
   - Created (2019-06-17): %s
  * Delete row:
   - Status (1): %d

  `, uid, username, department, created, affect)

	c.Ctx.WriteString(status)

}
