package main

import (
	"gateway/internal/config"
	"gateway/internal/router"
	"gateway/internal/service"

	// "strconv"

	"github.com/bytedance/sonic"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
	"github.com/jackc/pgx/v5/pgxpool"
)

var dbPool *pgxpool.Pool

func main() {
	config.LoadEnvs()

	app := fiber.New(fiber.Config{
		Prefork:     false,
		JSONEncoder: sonic.Marshal,
		JSONDecoder: sonic.Unmarshal,
	})

	app.Use(logger.New())

	router.SetupRoutes(app)

	// app.Listen(":" + strconv.Itoa(config.Env.Port))

	service.GetCarInfo()
}