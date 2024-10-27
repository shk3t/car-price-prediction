package config

import (
	"fmt"
	force "gateway/internal/utils"
	"os"

	"strconv"

	"github.com/joho/godotenv"
)

type envConfig struct {
	Port                  int
	SecretKey             string
	MlServiceUrl          string
	TranslationServiceUrl string
}

var Env envConfig

func LoadEnvs() {
	if err := godotenv.Load(".env"); err != nil {
		panic("Error loading .env file")
	}

	Env = envConfig{
		Port:      force.Default(strconv.Atoi(os.Getenv("PORT"))),
		SecretKey: os.Getenv("ML_SECRET_KEY"),
		MlServiceUrl: fmt.Sprintf(
			"http://%s:%s",
			os.Getenv("HOST"),
			os.Getenv("ML_SERVICE_URL"),
		),
		TranslationServiceUrl: fmt.Sprintf("http://%s:%s", os.Getenv("HOST"), os.Getenv("TR_PORT")),
	}
}