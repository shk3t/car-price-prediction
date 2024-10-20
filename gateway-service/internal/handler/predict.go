package handler

import (
	"bytes"
	"encoding/json"
	c "gateway/internal/config"
	m "gateway/internal/model"
	"gateway/internal/service"
	u "gateway/internal/utils"
	"net/http"
	"strconv"

	"github.com/gofiber/fiber/v2"
)

func Predict(fctx *fiber.Ctx) error {
	body := m.CarInfo{}
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

func WebScrap(fctx *fiber.Ctx) error {
	info, err := service.GetCarInfo()
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	report := u.GetAssertDefault(info, "report", map[string]interface{}{})
	ptsInfo := u.GetAssertDefault(report, "pts_info", map[string]interface{}{})
	yearWrapper := u.GetAssertDefault(ptsInfo, "year", map[string]interface{}{})
	modelYear := u.GetAssertDefault(yearWrapper, "value", -1.0)

	return fctx.SendString(strconv.Itoa(int(modelYear)))
}