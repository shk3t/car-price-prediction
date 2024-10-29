import axios from "axios"
import {GATEWAY_URL} from "../consts/api"

export const gwCfg = axios.create({
  baseURL: GATEWAY_URL,
})