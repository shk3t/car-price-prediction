package model

type CarInfo struct {
	Brand             string  `json:"brand"`
	Model             string  `json:"model"`
	ModelYear         int     `json:"model_year"`
	MilageKm          int     `json:"milage_km"`
	FuelType          string  `json:"fuel_type"`
	EngineVolume      float64 `json:"engine_volume"`
	EnginePower       int     `json:"engine_power"`
	TransmissionSpeed float64 `json:"transmission_speed"`
	TransmissionType  string  `json:"transmission_type"`
	Color             string  `json:"color"`
	InteriorColor     string  `json:"interior_color"`
	Accident          string  `json:"accident"`
	CleanTitle        string  `json:"clean_title"`
	PriceRub          float64 `json:"price_rub"`
}

type PredictionResponse struct {
	PriceRub float64 `json:"price_rub"`
}

type WebScrapRequest struct {
	Url string `json:"url"`
}