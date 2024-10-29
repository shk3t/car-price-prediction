import MainContainer from "../components/containers/MainContainer"
import CenteringContainer from "../components/containers/CenteringContainer"
import NiceButton from "../components/buttons/NiceButton"
import NiceInput from "../components/inputs/NiceInput"
import SectionContainer from "../components/containers/SectionContainer"
import {capitalize} from "lodash"
import {CarInfo} from "../types/predict"
import styles from "../styles/base.module.css"
import {hexColors} from "../consts/utils"

export default function StartPage() {
  const carInfo: CarInfo = {
    url: "https://example.com/car-image",
    image: "https://avatars.mds.yandex.net/get-autoru-vos/2176223/1c9265384b26525d3926949e48c4a5ac/1200x900n",
    brand: "toyota",
    model: "corolla",
    modelYear: 2020,
    milageKm: 30000,
    fuelType: "gasoline",
    engineVolume: 1.8,
    enginePower: 140,
    transmissionSpeed: null, // Assuming no transmission speed provided
    transmissionType: "automatic",
    color: "blue",
    interiorColor: null, // Assuming no interior color provided
    accident: null, // Assuming no accident history provided
    cleanTitle: true,
    priceRub: 150000,
    recommendedPriceRub: 160000,
  }

  // carInfo.url = ""

  const emptyComponent = (
    <MainContainer>
      <CenteringContainer vertical={true}>
        <NiceInput
          size={80}
          placeholder="https://auto.ru/cars/used/sale/lamborghini/aventador/1116087097-7a1c0fc2/"
        ></NiceInput>
        <NiceButton>Predict</NiceButton>
      </CenteringContainer>
    </MainContainer>
  )

  const predictedComponent = (
    <MainContainer flexEnabled={false}>
      <SectionContainer>
        <NiceInput
          size={80}
          placeholder="https://auto.ru/cars/used/sale/lamborghini/aventador/1116087097-7a1c0fc2/"
        ></NiceInput>
        <NiceButton>Predict</NiceButton>
      </SectionContainer>
      <SectionContainer>
        <h1>
          Recommended price:{" "}
          <span
            style={{
              color: carInfo.recommendedPriceRub < carInfo.priceRub ? hexColors.foam : hexColors.love,
            }}
          >
            {carInfo.recommendedPriceRub.toLocaleString("ru-RU")} ₽
          </span>
        </h1>
      </SectionContainer>
      <SectionContainer>
        <CenteringContainer>
          <div style={{padding: "2em"}}>
            <img height="480em" src={carInfo.image} className={styles.bgFrame} />
          </div>
          <div style={{padding: "2em"}}>
            <p style={{fontSize: "1.2em"}}>
              Real price:{" "}
              <b>
                <span
                  style={{
                    color: carInfo.priceRub < carInfo.recommendedPriceRub ? hexColors.foam : hexColors.love,
                  }}
                >
                  {carInfo.priceRub.toLocaleString("ru-RU")} ₽
                </span>
              </b>
            </p>
            <br />
            <p>
              Brand: <b style={{color: hexColors.gold}}>{carInfo.brand.toUpperCase()}</b>
            </p>
            <p>
              Model: <b style={{color: hexColors.gold}}>{carInfo.model.toUpperCase()}</b>
            </p>
            <p>
              Year: <b style={{color: hexColors.gold}}>{carInfo.modelYear}</b>
            </p>
            <p>
              Milage in km: <b style={{color: hexColors.gold}}>{carInfo.milageKm.toLocaleString("ru-RU")}</b>
            </p>
            <p>
              Fuel type: <b style={{color: hexColors.gold}}>{carInfo.fuelType}</b>
            </p>
            <p>
              Engine volume: <b style={{color: hexColors.gold}}>{carInfo.engineVolume} L</b>
            </p>
            <p>
              Engine power: <b style={{color: hexColors.gold}}>{carInfo.enginePower.toLocaleString("ru-RU")} HP</b>
            </p>
            {carInfo.transmissionSpeed && (
              <p>
                Transmission speed: <b style={{color: hexColors.gold}}>{carInfo.transmissionSpeed} DT</b>
              </p>
            )}
            <p>
              Transmission type: <b style={{color: hexColors.gold}}>{carInfo.transmissionType}</b>
            </p>
            <p>
              Color: <b style={{color: hexColors.gold}}>{carInfo.color}</b>
            </p>
            {carInfo.interiorColor && (
              <p>
                Interior color: <b style={{color: hexColors.gold}}>{carInfo.interiorColor}</b>
              </p>
            )}
            {carInfo.accident && (
              <p>
                Accident history: <b style={{color: hexColors.gold}}>{capitalize(carInfo.accident)}</b>
              </p>
            )}
            <p>
              Clean title: <b style={{color: hexColors.gold}}>{carInfo.cleanTitle ? "yes" : "no"}</b>
            </p>
          </div>
        </CenteringContainer>
      </SectionContainer>
    </MainContainer>
  )

  return carInfo.url ? predictedComponent : emptyComponent
}