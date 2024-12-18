package handler

import (
	"bytes"
	"encoding/json"
	"errors"
	c "gateway/internal/config"
	m "gateway/internal/model"
	"gateway/internal/service"
	u "gateway/internal/utils"
	"io"
	"net/http"

	"github.com/gofiber/fiber/v2"
)

func Predict(fctx *fiber.Ctx) error {
	reqBody := m.PredictRequest{}
	err := fctx.BodyParser(&reqBody)
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	carInfo, err := service.GetCarInfo(reqBody.CurlData, reqBody.CarUrl)
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	var buf bytes.Buffer
	err = json.NewEncoder(&buf).Encode(carInfo)
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

	carInfo.RecommendedPriceRub = pred.RecommendedPriceRub
	return fctx.JSON(carInfo)
}

func FineTune(fctx *fiber.Ctx) error {
	reqBody := m.FineTuneRequest{}
	err := fctx.BodyParser(&reqBody)
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	carInfos := []m.CarInfo{}
	for _, carUrl := range reqBody.CarUrls {
		carInfo, err := service.GetCarInfo(reqBody.CurlData, carUrl)
		if err != nil {
			return fctx.Status(400).SendString(err.Error())
		}
		carInfos = append(carInfos, *carInfo)
	}

	var buf bytes.Buffer
	err = json.NewEncoder(&buf).Encode(carInfos)
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	resp, err := http.Post(c.Env.MlServiceUrl+"/api/fine_tune", "application/json", &buf)
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}
	if resp.StatusCode >= 400 {
		err = errors.New(string(u.Default(io.ReadAll(resp.Body))))
		return fctx.Status(400).SendString(err.Error())
	}
	defer resp.Body.Close()
	return fctx.SendString("OK")
}