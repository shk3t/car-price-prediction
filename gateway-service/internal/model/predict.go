package model

type CarEntry struct {
	Brand        string  `json:"brand"`
	Model        string  `json:"model"`
	ModelYear    int     `json:"model_year"`
	Milage       int     `json:"milage"`
	FuelType     string  `json:"fuel_type"`
	Engine       string  `json:"engine"`
	Transmission string  `json:"transmission"`
	ExtCol       string  `json:"ext_col"`
	IntCol       string  `json:"int_col"`
	Accident     string  `json:"accident"`
	CleanTitle   string  `json:"clean_title"`
	Price        float64 `json:"price"`
}

type PredictionResponse struct {
	PriceRub float64 `json:"price_rub"`
}
