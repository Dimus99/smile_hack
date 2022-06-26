import axios from 'axios'
import {getBase64} from "../helpers/b64";

const BASE_URL = 'http://localhost:5000'

export const sendPhoto = async photo => {
    let response
    const fileBase64 = await getBase64(photo)
    const data = {img: fileBase64}
    try {
        response = axios.post(`${BASE_URL}/predict`, data)
    } catch (e) {
    }

    return response
}