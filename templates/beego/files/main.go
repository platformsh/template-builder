package main

import (
	"github.com/astaxie/beego"
	config "github.com/platformsh/template-beego/conf"
	_ "github.com/platformsh/template-beego/routers"
)

func main() {
	beego.Run(":" + config.PshConfig.Port())
}
