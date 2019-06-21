package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	sqldsn "github.com/platformsh/config-reader-go/v2/sqldsn"
	psh "github.com/platformsh/config-reader-go/v2"
	"log"
	"net/http"
)

func main() {

	// The Config Reader library provides Platform.sh environment information mapped to Go structs.
	config, err := psh.NewRuntimeConfig()
	if err != nil {
		panic("Not in a Platform.sh Environment.")
	}

	// Set up an extremely simple web server response.
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {

		// Name the template on front page and print hello message
		fmt.Fprintf(w, "Hello, world! - A simple Go template for Platform.sh\n\n")

		// Run some background SQL, just to prove we can.
		trySql(config, w)

	})

		// The port to listen on is defined by Platform.sh.
		log.Fatal(http.ListenAndServe(":"+config.Port(), nil))

}

// trySql simply connects to a MySQL server defined by Platform.sh and
// writes and reads from it.  This is not particularly useful code,
// but demonstrates how you can leverage the Platform.sh Config Reader library.
func trySql(conf *psh.RuntimeConfig, w http.ResponseWriter) {

		// Accessing the database relationship Credentials struct
	credentials, err := conf.Credentials("database")
	if err != nil {
		panic(err)
	}

	// Using the sqldsn formatted credentials package
	formatted, err := sqldsn.FormattedCredentials(credentials)
	if err != nil {
		panic(err)
	}

	db, err := sql.Open("mysql", formatted)
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

	for rows.Next() {
		var uid int
		var username string
		var department string
		var created string
		err = rows.Scan(&uid, &username, &department, &created)
		checkErr(err)
		// Section for MySQL tests
		fmt.Fprintf(w, "\nMySQL Tests:\n\n")
		fmt.Fprintf(w, "* Connect and add row:\n")
		fmt.Fprintf(w, "   - Row ID (1): ")
		fmt.Fprintln(w, uid)
		fmt.Fprintf(w, "   - Username (goPlatformsh): ")
		fmt.Fprintln(w, username)
		fmt.Fprintf(w, "   - Department (Deploy Friday): ")
		fmt.Fprintln(w, department)
		fmt.Fprintf(w, "   - Created (2019-06-17): ")
		fmt.Fprintln(w, created)
	}

	// delete
	stmt, err = db.Prepare("delete from userinfo where uid=?")
	checkErr(err)

	res, err = stmt.Exec(id)
	checkErr(err)

	affect, err = res.RowsAffected()
	checkErr(err)

	fmt.Fprintf(w, "\n* Delete row:\n")
	fmt.Fprintf(w, "   - Status (1): ")
	fmt.Fprintln(w, affect)

	db.Close()
}

// checkErr is a simple wrapper for panicking on error.
// It likely should not be used in a real application.
func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
