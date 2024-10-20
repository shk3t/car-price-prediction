package handler

import (
	"bytes"
	"encoding/json"
	c "gateway/internal/config"
	m "gateway/internal/model"
	"net/http"

	"github.com/gofiber/fiber/v2"
)

func Predict(fctx *fiber.Ctx) error {
	body := m.CarEntry{}
	if err := fctx.BodyParser(&body); err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	var buf bytes.Buffer
	err := json.NewEncoder(&buf).Encode(body)
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	resp, err := http.Post(c.Env.MlServiceUrl+"/api/predict", "application/json", &buf)
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}
	defer resp.Body.Close()

	pred := m.PredictionResponse{}
	err = json.NewDecoder(resp.Body).Decode(&pred)
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	return fctx.JSON(fiber.Map{"price_rub": pred.PriceRub})
}
