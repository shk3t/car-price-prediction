package model

type CarInfo struct {
	Url                 string  `json:"url"`
	Image               string  `json:"image"`
	Brand               string  `json:"brand"`
	Model               string  `json:"model"`
	ModelYear           int     `json:"model_year"`
	MilageKm            int     `json:"milage_km"`
	FuelType            string  `json:"fuel_type"`
	EngineVolume        float64 `json:"engine_volume"`
	EnginePower         int     `json:"engine_power"`
	TransmissionSpeed   *int    `json:"transmission_speed"`
	TransmissionType    string  `json:"transmission_type"`
	Color               string  `json:"color"`
	InteriorColor       *string `json:"interior_color"`
	Accident            *string `json:"accident"`
	CleanTitle          bool    `json:"clean_title"`
	PriceRub            float64 `json:"price_rub"`
	RecommendedPriceRub float64 `json:"recommended_price_rub"`
}

type PredictRequest struct {
	CarUrl string `json:"car_url"`
}

type PredictionResponse struct {
	RecommendedPriceRub float64 `json:"recommended_price_rub"`
}