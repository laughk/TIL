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

	// Parameter in Path
	// --------------------------------------------------------
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

	// Queerystring parameters
	router.GET("/welcome", func(c *gin.Context) {
		firstname := c.DefaultQuery("firstname", "Guest")
		lastname := c.Query("lastname")
		// lastname := c.Request.URL.Query.GET("lastname")

		c.String(http.StatusOK, "Hello %s %s", firstname, lastname)
	})

	return router.Run(":8080")
}
