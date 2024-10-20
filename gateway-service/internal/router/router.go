package router

import (
	"gateway/internal/handler"
	"os"

	"github.com/gofiber/fiber/v2"
)

func SetupRoutes(app *fiber.App) {
	api := app.Group(os.Getenv("BASE_PATH") + "/api")

	api.Post("/predict", handler.Predict)
	api.Post("/webscrap", handler.WebScrap)

	// api.Get("/projects", handler.GetProjects)
	// api.Get("/projects/:id", handler.GetProject)
	//
	// api.Get("/tasks", handler.GetTasks)
	// api.Get("/tasks/:id", handler.GetTask)
	//
	// api.Get("/solutions", handler.GetSolutions)
	// api.Get("/solutions/:id", handler.GetSolution)
	//
	// api.Post("/projects", handler.LoadProject)
	// api.Put("/projects/:id", handler.LoadProject)
	// api.Delete("/projects/:id", handler.DeleteProject)
	// api.Post("/solutions", handler.SubmitSolution)
	//
	// api.Get("/delayed-tasks", handler.GetDelayedTasks)
	// api.Get("/delayed-tasks/:id", handler.GetDelayedTask)
}