import MainContainer from "../components/containers/MainContainer"
import CenteringContainer from "../components/containers/CenteringContainer"
import VeryNiceInput from "../components/inputs/VeryNiceInput"
import NiceButton from "../components/buttons/NiceButton"
import {hexColors} from "../consts/utils"

export default function StartPage() {
  let actionComponent
  let status = "loading"

  switch (status) {
    case "button":
      actionComponent = <NiceButton>Fit</NiceButton>
      break
    case "loading":
      actionComponent = <h5 style={{color: hexColors.text}}>Loading...</h5> // TODO: add animation
      break
    case "done":
      actionComponent = <h5 style={{color: hexColors.foam}}>Done!</h5>
      break
    case "error":
      actionComponent = <h5 style={{color: hexColors.love}}>Something went wrong :(</h5>
      break
  }

  return (
    <MainContainer>
      <CenteringContainer vertical={true}>
        <h3>Fine tuning</h3>
        <VeryNiceInput
          rows={20}
          cols={80}
          placeholder={`URLs of car pages on auto.ru
for example:
https://auto.ru/cars/used/sale/lamborghini/aventador/1116087097-7a1c0fc2/
https://auto.ru/cars/used/sale/lamborghini/huracan/1125035900-1b7e546c/
or any other one of an average ML engineer from ITMO
`}
        ></VeryNiceInput>
        {actionComponent}
      </CenteringContainer>
    </MainContainer>
  )
}