package service

import (
	"bytes"
	"encoding/json"
	"fmt"
	"gateway/internal/utils"
	"io"
	"net/http"
)

func GetCarInfo() (map[string]interface{}, error) {
	url := "https://auto.ru/-/ajax/desktop-search/getRichVinReport/"
	offerId := "1125106753-40922ec8"

	payload := fmt.Sprintf(
		`{"offerID":"%s","pow":{"hash":"00000192ab06594c1070da69b031a515","timestamp":1729446172829,"payload":"%s"}}`,
		offerId,
		offerId,
	)

	req, err := http.NewRequest("POST", url, bytes.NewBuffer([]byte(payload)))
	if err != nil {
		return nil, err
	}
	req.Header.Add("content-type", "application/json")
	req.Header.Add(
		"cookie",
		"_csrf_token=7caab4b74db0b923f6cbe36f33266757920e418d11447c0c; spravka=dD0xNzI5MTg3NzIxO2k9ODkuMjA3LjIyMS4xMDI7RD03QUIzMUMzNTIxNjIzOEFGRDU4NzQzQTU4MkIwQzEyOTZCMEJCQzQ5QzlGNzM4MDMxNjJEMTgzQTY3RDBGNzRGRjQwQTVFMjcxMzk2MEQyQTc2REVCM0IxNEI4REUwRTUxODIzM0ZEREE1NjAwQkE2OEJGQTQ1Q0YzRDA4MDVFRDI2MDUzRDJCQTcwMUQ5QTdFNkFFRUEyRDt1PTE3MjkxODc3MjEyODUyNzgxNTg7aD1jMmRjZDcxYjViMTQzNmM4YzU5YzE1ZjAwYTllNWEzYw==",
	)
	req.Header.Add("x-csrf-token", "7caab4b74db0b923f6cbe36f33266757920e418d11447c0c")

	client := http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	respMap := map[string]interface{}{}
	json.Unmarshal(utils.Default(io.ReadAll(resp.Body)), &respMap)

	return respMap, nil
}