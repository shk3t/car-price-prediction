import MainContainer from "../components/containers/MainContainer"
import VeryNiceInput from "../components/inputs/VeryNiceInput"
import getCurlImg from "../assets/get-curl.png"
import SectionContainer from "../components/containers/SectionContainer"
import {hexColors} from "../consts/utils"

export default function ImportPage() {
  return (
    <MainContainer flexEnabled={false}>
      <SectionContainer>
        <h3>Paste your cURL here</h3>
        <VeryNiceInput rows={20} cols={80} placeholder="Your cURL code"></VeryNiceInput>
      </SectionContainer>
      <SectionContainer>
        <h3>What?</h3>
        <p>App need it to fake requests as it was done by a real human (you).</p>
        <p>Don't worry, app store your data only in browser session.</p>
      </SectionContainer>
      <SectionContainer>
        <p>You can copy cURL code from the following location:</p>
        <h5>
          DevTools (F12) {">"} Network {">"} Doc {">"} First request RMB {">"} Copy {">"} Copy as CURL
        </h5>
        <p>
          (Request entry looks like the end of URL path, e.g.{" "}
          <span style={{color: hexColors.gold}}>1116087097-7a1c0fc2/</span>)
        </p>
        <br />
        <img src={getCurlImg} />
      </SectionContainer>
    </MainContainer>
  )
}