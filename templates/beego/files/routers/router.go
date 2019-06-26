package routers

import (
	"github.com/platformsh/template-beego/controllers"
	"github.com/astaxie/beego"
)

func init() {
    beego.Router("/", &controllers.MainController{})
		beego.Router("/test", &controllers.MySQLTestController{})
}
