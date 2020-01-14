package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	if err := run(); err != nil {
		panic(err)
	}
}

func run() error {

	router := gin.Default()

	router.GET("/user/:name", func(c *gin.Context) {
		name := c.Param("name")
		c.String(http.StatusOK, "Hello %s", name)
	})

	router.GET("/user/:name/*action", func(c *gin.Context) {
		name := c.Param("name")
		action := c.Param("action")
		message := name + " is " + action
		c.String(http.StatusOK, message)
	})

	// router.POST("/user/:name/*actoin", func(c *gin.Context) {
	// c.FullPath() == "/user/:name/*action"
	// })

	return router.Run(":8080")
}
