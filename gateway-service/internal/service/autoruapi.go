package service

import (
	"bytes"
	"encoding/json"
	"fmt"
	m "gateway/internal/model"
	u "gateway/internal/utils"
	"io"
	"net/http"
	"os/exec"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

func GetCarInfo() (*m.CarInfo, error) {
	scriptPath := "scripts/curl.sh"
	// offerId := "1125399844-18893495"

	cmd := exec.Command("bash", scriptPath)
	var stdout, stderr bytes.Buffer
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr

	err := cmd.Run()
	if err != nil {
		return nil, err
	}

	doc, err := goquery.NewDocumentFromReader(bytes.NewReader(stdout.Bytes()))
	if err != nil {
		return nil, err
	}

	data, _ := doc.Find("div#sale-data-attributes").First().Attr("data-bem")

	carInfo := m.CarInfo{}

	doc.Find("ul.CardInfo__list-MZpc1").Children().Each(
		func(_ int, el *goquery.Selection) {
			attrName := el.Find("div").First().Text()
			// attrValue := el.Find("div").Last().Text()
			attrAValue := el.Find("a").First().Text()
			switch attrName {
			case "Цвет":
				carInfo.ExtCol = u.Capitalize(TranslateToEn(attrAValue))
			}
		},
	)

	dataBem := map[string]interface{}{}
	err = json.Unmarshal([]byte(data), &dataBem)
	if err != nil {
		return nil, err
	}

	saleData := u.GetAssertDefault(dataBem, "sale-data-attributes", map[string]interface{}{})
	carInfo.Brand = strings.ToLower(u.GetAssertDefault(saleData, "mark", ""))
	carInfo.FuelType = strings.ToLower(u.GetAssertDefault(saleData, "engine-type", ""))

	return &carInfo, nil
}

func TranslateToEn(text string) string {
	// docker run -e LT_LOAD_ONLY="en,ru" -ti --rm -p 5000:5000 libretranslate/libretranslate
	url := "http://localhost:5000/translate"
	payload := map[string]string{
		"q":      text,
		"source": "ru",
		"target": "en",
	}
	payloadBytes, _ := json.Marshal(payload)

	resp, _ := http.Post(url, "application/json", bytes.NewBuffer(payloadBytes))
	defer resp.Body.Close()

	respMap := map[string]interface{}{}
	json.Unmarshal(u.Default(io.ReadAll(resp.Body)), &respMap)

	return u.GetAssertDefault(respMap, "translatedText", "")
}