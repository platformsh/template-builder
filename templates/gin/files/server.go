package main

import (
	"net/http"
	"fmt"
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
	psh "github.com/platformsh/gohelper"
	"github.com/gin-gonic/gin"
)

var db = make(map[string]string)

func setupRouter() *gin.Engine {
	// Disable Console Color
	// gin.DisableConsoleColor()
	r := gin.Default()

	// Hello World
	r.GET("/", func(c *gin.Context) {

		// The psh library provides Platform.sh environment information mapped to Go structs.
		pi, err := psh.NewPlatformInfo()

		if err != nil {
			// This means we're not running on Platform.sh!
			// In practice you would want to fall back to another way to define
			// configuration information, say for your local development environment.
			fmt.Println(err)
			panic("Not in a Platform.sh Environment.")
		}

		fmt.Println("Yay, found Platform.sh info")

		dbString, err := pi.SqlDsn("mysql")
		checkErr(err)

		db, err := sql.Open("mysql", dbString)
		checkErr(err)

		// Force MySQL into modern mode.
		db.Exec("SET NAMES=utf8")
		db.Exec("SET sql_mode = 'ANSI,STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,ONLY_FULL_GROUP_BY'")

		_, err = db.Exec("DROP TABLE IF EXISTS userinfo")
		checkErr(err)

		_, err = db.Exec(`CREATE TABLE userinfo (
				uid INT(10) NOT NULL AUTO_INCREMENT,
				username VARCHAR(64) NULL DEFAULT NULL,
				departname VARCHAR(128) NULL DEFAULT NULL,
				created DATE NULL DEFAULT NULL,
				PRIMARY KEY (uid)
				) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;`)
		checkErr(err)

		// insert
		stmt, err := db.Prepare("INSERT userinfo SET username=?,departname=?,created=?")
		checkErr(err)

		res, err := stmt.Exec("platform", "Deploy Friday", "2019-06-17")
		checkErr(err)

		id, err := res.LastInsertId()
		checkErr(err)

		fmt.Println(id)
		// update
		stmt, err = db.Prepare("update userinfo set username=? where uid=?")
		checkErr(err)

		res, err = stmt.Exec("goPlatformsh", id)
		checkErr(err)

		affect, err := res.RowsAffected()
		checkErr(err)

		fmt.Println(affect)

		// query
		rows, err := db.Query("SELECT * FROM userinfo")
		checkErr(err)

		var uid int
		var username string
		var department string
		var created string
		for rows.Next() {
			err = rows.Scan(&uid, &username, &department, &created)
			checkErr(err)
		}

		// delete
		stmt, err = db.Prepare("delete from userinfo where uid=?")
		checkErr(err)

		res, err = stmt.Exec(id)
		checkErr(err)

		affect, err = res.RowsAffected()
		checkErr(err)

		db.Close()

		status := fmt.Sprintf(`Hello, World! - A simple Gin web framework template for Platform.sh


MySQL Tests:

* Connect and add row:
	 - Row ID (1): %d
	 - Username (goPlatformsh): %s
	 - Department (Deploy Friday): %s
	 - Created (2019-06-17): %s
* Delete row:
	 - Status (1): %d

		`, uid, username, department, created, affect)


		c.String(http.StatusOK, status)
	})

	return r
}

func main() {
	r := setupRouter()

	// The psh library provides Platform.sh environment information mapped to Go structs.
	p, err := psh.NewPlatformInfo()

	if err != nil {
		// This means we're not running on Platform.sh!
		// In practice you would want to fall back to another way to define
		// configuration information, say for your local development environment.
		fmt.Println(err)
		panic("Not in a Platform.sh Environment.")
	}

	fmt.Println("Yay, found Platform.sh info")

	// Listen and Server in 0.0.0.0:8080
	r.Run(":"+p.Port)
}

// checkErr is a simple wrapper for panicking on error.
// It likely should not be used in a real application.
func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
