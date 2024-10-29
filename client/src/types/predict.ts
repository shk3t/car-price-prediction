export interface CarInfo {
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