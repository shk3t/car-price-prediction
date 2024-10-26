package handler

import (
	"bytes"
	"encoding/json"
	"fmt"

	c "gateway/internal/config"
	m "gateway/internal/model"
	"gateway/internal/service"
	"net/http"

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

// func WebScrap(fctx *fiber.Ctx) error {
// 	resp, err := http.Get("http://localhost:5173/start")
// 	if err != nil {
// 		return fctx.Status(400).SendString(err.Error())
// 	}
// 	defer resp.Body.Close()
//
//
// 	info := m.CarInfo{}
// 	// cll.OnHTML("div.CardInfo-ateuv", func(e *colly.HTMLElement) {
// 	// 	e.DOM.Find("ul").First().Each(func(_ int, el *goquery.Selection) {
// 	// 		if el.HasClass("CardInfoRow_year") {
// 	// 			info.ModelYear, _ = strconv.Atoi(el.Find("div:last-child > a").Text())
// 	// 		}
// 	// 	})
// 	// })
// 	result, _ := doc.Find("button").First().Attr("placeholder")
// 	fmt.Println(result)
//
// 	responseData, err := json.Marshal(info)
// 	if err != nil {
// 		return fctx.Status(400).SendString(err.Error())
// 	}
// 	return fctx.Send(responseData)
// }

func WebScrap(fctx *fiber.Ctx) error {
	carInfo, err := service.GetCarInfo()
	if err != nil {
		return fctx.Status(400).SendString(err.Error())
	}

	fmt.Println(carInfo.FuelType)

	// report := u.GetAssertDefault(info, "report", map[string]interface{}{})
	// ptsInfo := u.GetAssertDefault(report, "pts_info", map[string]interface{}{})
	// yearWrapper := u.GetAssertDefault(ptsInfo, "year", map[string]interface{}{})
	// modelYear := u.GetAssertDefault(yearWrapper, "value", -1.0)

	return fctx.SendString("nice")
}