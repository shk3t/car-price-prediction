import MainContainer from "../components/containers/MainContainer"
import CenteringContainer from "../components/containers/CenteringContainer"
import NiceButton from "../components/buttons/NiceButton"
import NiceInput from "../components/inputs/NiceInput"

export default function StartPage() {
  return (
    <MainContainer>
      <CenteringContainer vertical={true}>
        <NiceInput placeholder="auto.ru URL"></NiceInput>
        <NiceButton>Nice!</NiceButton>
      </CenteringContainer>
    </MainContainer>
  )
}