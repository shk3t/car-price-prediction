import {carInfoFromResponse, CarInfo} from "../types/predict"
import {gwCfg} from "./api"

export default class PredictService {
  static async predict(carUrl: string, curlData: string): Promise<CarInfo> {
    const response = await gwCfg.post("/api/predict", {car_url: carUrl, curl_data: curlData})
    return carInfoFromResponse(response.data)
  }

  static async fineTune(carUrls: string, curlData: string): Promise<boolean> {
    console.log(carUrls.split("\n"))
    const response = await gwCfg.post("/api/fine_tune", {
      car_urls: carUrls.split("\n"),
      curl_data: curlData,
    })
    return 200 <= response.status && response.status <= 299
  }
}