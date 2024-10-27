package router

import (
	"gateway/internal/handler"
	"os"

	"github.com/gofiber/fiber/v2"
)

func SetupRoutes(app *fiber.App) {
	api := app.Group(os.Getenv("BASE_PATH") + "/api")

	api.Post("/predict", handler.Predict)
	api.Post("/fine_tune", handler.FineTune)
}