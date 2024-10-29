export type CarInfo = {
  url: string
  image: string
  brand: string
  model: string
  modelYear: number
  milageKm: number
  fuelType: string
  engineVolume: number
  enginePower: number
  transmissionSpeed?: number | null
  transmissionType: string
  color: string
  interiorColor?: string | null
  accident?: string | null
  cleanTitle: boolean
  priceRub: number
  recommendedPriceRub: number
}

export const emptyCarInfo: CarInfo = {
  url: "",
  image: "",
  brand: "",
  model: "",
  modelYear: 0,
  milageKm: 0,
  fuelType: "",
  engineVolume: 0,
  enginePower: 0,
  transmissionSpeed: null,
  transmissionType: "",
  color: "",
  interiorColor: null,
  accident: null,
  cleanTitle: true,
  priceRub: 0,
  recommendedPriceRub: 0,
}

export function carInfoFromResponse(data: any): CarInfo {
  return {
    url: data.url,
    image: data.image,
    brand: data.brand,
    model: data.model,
    modelYear: data.model_year,
    milageKm: data.milage_km,
    fuelType: data.fuel_type,
    engineVolume: data.engine_volume,
    enginePower: data.engine_power,
    transmissionSpeed: data.transmission_speed,
    transmissionType: data.transmission_type,
    color: data.color,
    interiorColor: data.interior_color,
    accident: data.accident,
    cleanTitle: data.clean_title,
    priceRub: data.price_rub,
    recommendedPriceRub: data.recommended_price_rub,
  }
}