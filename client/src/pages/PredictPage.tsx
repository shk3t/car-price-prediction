import MainContainer from "../components/containers/MainContainer"
import CenteringContainer from "../components/containers/CenteringContainer"
import NiceButton from "../components/buttons/NiceButton"
import NiceInput from "../components/inputs/NiceInput"
import SectionContainer from "../components/containers/SectionContainer"
import {capitalize} from "lodash"
import {CarInfo, emptyCarInfo} from "../types/predict"
import styles from "../styles/base.module.css"
import {hexColors} from "../consts/utils"
import {useEffect, useState} from "react"
import {buildActionComponents} from "../helpers/builders"
import PredictService from "../services/PredictService"

export default function PredictPage() {
  const actionComponents = buildActionComponents("Predict", sendRequest, resetActionComponent)
  const [curActionComponent, setActionComponent] = useState<JSX.Element>(actionComponents.button)
  const [carUrl, setCarUrl] = useState<string>("")
  const [carInfo, setCarInfo] = useState<CarInfo>(emptyCarInfo)

  async function sendRequest() {
    const curlData = localStorage.getItem("curlData")
    if (curlData) {
      setActionComponent(actionComponents.loading)
      try {
        const newCarInfo = await PredictService.predict(carUrl, curlData)
        setCarInfo(newCarInfo)
        setActionComponent(actionComponents.done)
      } catch (error) {
        console.log(error)
        setActionComponent(actionComponents.requestError)
      }
    } else {
      setActionComponent(actionComponents.curlError)
    }
  }

  function resetActionComponent() {
    setActionComponent(actionComponents.button)
  }

  const emptyComponent = (
    <MainContainer>
      <CenteringContainer vertical={true}>
        <h3>Put your dream car URL here</h3>
        <NiceInput
          size={80}
          placeholder="https://auto.ru/cars/used/sale/lamborghini/aventador/1116087097-7a1c0fc2/"
          value={carUrl}
          onChange={(e) => setCarUrl(e.target.value)}
        ></NiceInput>
        {curActionComponent}
      </CenteringContainer>
    </MainContainer>
  )

  const predictedComponent = (
    <MainContainer flexEnabled={false}>
      <SectionContainer>
        <h3>Put your dream car URL here</h3>
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
              color:
                carInfo.recommendedPriceRub < carInfo.priceRub ? hexColors.foam : hexColors.love,
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
                    color:
                      carInfo.priceRub < carInfo.recommendedPriceRub
                        ? hexColors.foam
                        : hexColors.love,
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
              Milage in km:{" "}
              <b style={{color: hexColors.gold}}>{carInfo.milageKm.toLocaleString("ru-RU")}</b>
            </p>
            <p>
              Fuel type: <b style={{color: hexColors.gold}}>{carInfo.fuelType}</b>
            </p>
            <p>
              Engine volume: <b style={{color: hexColors.gold}}>{carInfo.engineVolume} L</b>
            </p>
            <p>
              Engine power:{" "}
              <b style={{color: hexColors.gold}}>
                {carInfo.enginePower.toLocaleString("ru-RU")} HP
              </b>
            </p>
            {carInfo.transmissionSpeed && (
              <p>
                Transmission speed:{" "}
                <b style={{color: hexColors.gold}}>{carInfo.transmissionSpeed} DT</b>
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
                Accident history:{" "}
                <b style={{color: hexColors.gold}}>{capitalize(carInfo.accident)}</b>
              </p>
            )}
            <p>
              Clean title:{" "}
              <b style={{color: hexColors.gold}}>{carInfo.cleanTitle ? "yes" : "no"}</b>
            </p>
          </div>
        </CenteringContainer>
      </SectionContainer>
    </MainContainer>
  )

  return carInfo.url ? predictedComponent : emptyComponent
}