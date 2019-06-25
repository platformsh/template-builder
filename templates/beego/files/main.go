package main

import (
	"github.com/astaxie/beego"
	"github.com/platformsh/template-beego/controllers"
	_ "github.com/platformsh/template-beego/routers"
)

func getPort() string {
	var c controllers.MainController
	c.Prepare()
	return c.Config.Port()
}

func main() {

	// Get the port
	port := getPort()
	beego.Run(":" + port)
}
