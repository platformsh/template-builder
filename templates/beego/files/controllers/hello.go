package controllers

import (
        "github.com/astaxie/beego"
)

type HelloController struct {
        beego.Controller
}

func (c *HelloController) Get() {
	c.Ctx.WriteString("Hello world! A Golang Beego template for Platform.sh.")
}
