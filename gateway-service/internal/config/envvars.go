package config

import (
	force "gateway/internal/utils"
	"os"

	"strconv"

	"github.com/joho/godotenv"
)

type envConfig struct {
	Port         int
	SecretKey    string
	MlServiceUrl string
}

var Env envConfig

func LoadEnvs() {
	if err := godotenv.Load(".env"); err != nil {
		panic("Error loading .env file")
	}

	Env = envConfig{
		Port:         force.Default(strconv.Atoi(os.Getenv("PORT"))),
		SecretKey:    os.Getenv("SECRET_KEY"),
		MlServiceUrl: os.Getenv("ML_SERVICE_URL"),
	}
}
