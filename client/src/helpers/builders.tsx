import NiceButton from "../components/buttons/NiceButton"
import {hexColors} from "../consts/utils"

export function buildActionComponents(buttonText: string, sendRequest: () => void, resetActionComponent: () => void) {
  return {
    button: <NiceButton onClick={sendRequest}>{buttonText}</NiceButton>,
    loading: <h5 style={{color: hexColors.text}}>Loading...</h5>, // TODO: add animation
    done: (
      <h5 style={{color: hexColors.foam}} onClick={resetActionComponent}>
        Done!
      </h5>
    ),
    requestError: (
      <h5 style={{color: hexColors.love}} onClick={resetActionComponent}>
        Something went wrong :(
      </h5>
    ),
    curlError: (
      <h5
        style={{color: hexColors.love}}
        onClick={resetActionComponent}
      >{`cURL data was not specified. Please, go to import page.`}</h5>
    ),
  }
}