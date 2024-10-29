import MainContainer from "../components/containers/MainContainer"
import CenteringContainer from "../components/containers/CenteringContainer"
import VeryNiceInput from "../components/inputs/VeryNiceInput"
import getCurlImg from "../assets/get-curl.png"
import StringSpan from "../components/text/String"

// TODO: extact sections to section containers
export default function ImportPage() {
  return (
    <MainContainer flexEnabled={false}>
      <section>
        <CenteringContainer vertical={true}>
          <h3>Paste your cURL here</h3>
          <VeryNiceInput placeholder="Your cURL code"></VeryNiceInput>
        </CenteringContainer>
      </section>
      <section>
        <CenteringContainer vertical={true}>
          <h3>What?</h3>
          <p>App need it to fake requests as it was done by a real human (you).</p>
          <p>Don't worry, app store your data only in browser session.</p>
        </CenteringContainer>
      </section>
      <section>
        <CenteringContainer vertical={true}>
          <p>You can copy cURL code from the following location:</p>
          <h5>
            DevTools (F12) {">"} Network {">"} Doc {">"} First request RMB {">"} Copy {">"} Copy as
            CURL
          </h5>
          <p>
            (Request entry looks like the end of URL path, e.g.{" "}
            <StringSpan>1116087097-7a1c0fc2/</StringSpan>)
          </p>
          <br />
          <img src={getCurlImg} />
        </CenteringContainer>
      </section>
    </MainContainer>
  )
}