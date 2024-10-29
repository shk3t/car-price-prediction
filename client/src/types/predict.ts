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