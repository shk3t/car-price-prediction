import {Link} from "react-router-dom"
import NiceButton from "../components/buttons/NiceButton"
import {hexColors} from "../consts/utils"
import {IMPORT_PATH} from "../consts/pages"

export function buildActionComponents(
  buttonText: string,
  sendRequest: () => void,
  resetActionComponent: () => void,
) {
  return {
    button: <NiceButton onClick={() => sendRequest()}>{buttonText}</NiceButton>,
    loading: <h5 style={{color: hexColors.text}}>Loading...</h5>,
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
      <h5 style={{color: hexColors.love}} onClick={resetActionComponent}>
        cURL data was not specified. Please, go to{" "}
        <Link style={{textDecoration: "underline"}} to={IMPORT_PATH}>
          import
        </Link>{" "}
        page.
      </h5>
    ),
  }
}