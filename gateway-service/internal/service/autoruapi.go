package service

import (
	"bytes"
	"encoding/json"
	m "gateway/internal/model"
	u "gateway/internal/utils"
	"io"
	"net/http"
	"os"
	"regexp"
	"strconv"

	"os/exec"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

func GetCarInfo(carUrl string) (*m.CarInfo, error) {
	carInfo := m.CarInfo{
		Url: carUrl,
	}

	scriptPath := "scripts/curl.sh"
	// carUrl := "https://auto.ru/cars/used/sale/ford/mustang/1119446398-610c531a/"

	cmd := exec.Command("bash", scriptPath, carUrl)
	var stdout, stderr bytes.Buffer
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr

	// err := cmd.Run()
	// if err != nil {
	// 	return nil, err
	// }

	fileData, err := os.ReadFile("/home/shket/projects/draft/output.html")
	if err != nil {
		return nil, err
	}
	doc, err := goquery.NewDocumentFromReader(bytes.NewReader(fileData))

	// doc, err := goquery.NewDocumentFromReader(bytes.NewReader(stdout.Bytes()))
	if err != nil {
		return nil, err
	}

	data, _ := doc.Find("div#sale-data-attributes").First().Attr("data-bem")

	numRe := regexp.MustCompile(`\d+[.,]?\d*`)

	doc.Find("ul.CardInfo__list-MZpc1").Children().Each(
		func(_ int, el *goquery.Selection) {
			attrName := strings.ToLower(el.Children().First().Text())
			attrValue := strings.ToLower(el.Children().Last().Text())
			attrDivValue := strings.ToLower(el.Find("div > div").Text())
			attrAValue := strings.ToLower(el.Find("a").First().Text())
			switch attrName {
			case "двигатель":
				engParams := strings.Split(attrDivValue, "/")
				carInfo.EngineVolume = u.Default(
					strconv.ParseFloat(numRe.FindString(engParams[0]), 64),
				)
				carInfo.EnginePower = u.Default(strconv.Atoi(numRe.FindString(engParams[1])))
			case "коробка":
				switch attrValue {
				case "механическая":
					carInfo.TransmissionType = "manual"
				default:
					carInfo.TransmissionType = "automatic"
				}
			case "цвет":
				carInfo.Color = TranslateToEn(attrAValue)
			case "таможня":
				carInfo.CleanTitle = attrValue == "растаможен"
			}
		},
	)

	dataBem := map[string]interface{}{}
	err = json.Unmarshal([]byte(data), &dataBem)
	if err != nil {
		return nil, err
	}

	saleData := u.GetAssertDefault(dataBem, "sale-data-attributes", map[string]interface{}{})
	for key, value := range saleData {
		strValue, ok := value.(string)
		if ok {
			saleData[key] = strings.ToLower(strValue)
		}
	}

	carInfo.Image = u.GetAssertDefault(saleData, "image", "")
	carInfo.Brand = u.GetAssertDefault(saleData, "mark", "")
	carInfo.Model = u.GetAssertDefault(saleData, "model", "")
	carInfo.ModelYear = int(u.GetAssertDefault(saleData, "year", 0.0))
	carInfo.MilageKm = int(u.GetAssertDefault(saleData, "km-age", 0.0))
	carInfo.FuelType = u.GetAssertDefault(saleData, "engine-type", "")
	carInfo.Color = u.GetAssertDefault(saleData, "engine-type", "")
	carInfo.PriceRub = u.GetAssertDefault(saleData, "price", 0.0)

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