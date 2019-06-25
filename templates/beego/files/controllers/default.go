package controllers

import (
	"github.com/astaxie/beego"
  psh "github.com/platformsh/config-reader-go/v2"
)

type MainController struct {
	beego.Controller
  Config *psh.RuntimeConfig
}

func (c *MainController) Prepare() {

  // The Config Reader library provides Platform.sh environment information mapped to Go structs.
  config, err := psh.NewRuntimeConfig()
  if err != nil {
    panic("Not in a Platform.sh Environment.")
  }

  c.Config = config

}

func (c *MainController) Get() {
	c.Data["Website"] = "beego.me"
	c.TplName = "index.tpl"

}
