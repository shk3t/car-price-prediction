import MainContainer from "../components/containers/MainContainer"
import CenteringContainer from "../components/containers/CenteringContainer"
import VeryNiceInput from "../components/inputs/VeryNiceInput"
import {buildActionComponents} from "../helpers/builders"
import {useState} from "react"

export default function FitPage() {
  const actionComponents = buildActionComponents("Fit", sendRequest, resetActionComponent)

  const [curActionComponent, setActionComponent] = useState<JSX.Element>(actionComponents.button)

  function sendRequest() {
    if (localStorage.getItem("curlData")) {
      setActionComponent(actionComponents.loading)
      alert("Your request was sent! (TODO)") // TODO: send request
      setActionComponent(actionComponents.done)
    } else {
      setActionComponent(actionComponents.curlError)
    }
  }

  function resetActionComponent() {
    setActionComponent(actionComponents.button)
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
        {curActionComponent}
      </CenteringContainer>
    </MainContainer>
  )
}