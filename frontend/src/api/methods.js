import axios from 'axios'
import {base64ToFile, getBase64} from "../helpers/b64";

const BASE_URL = 'http://localhost:5000'

export const sendPhoto = async photo => {
  let response
  const fileBase64 = await getBase64(photo)
  const img = fileBase64.split(',').slice(1, fileBase64.length)
  const b64_prefix = fileBase64.split(',')[0]
  const data = {
    img,
    b64_prefix,
  }

  try {
    response = axios.post(`${BASE_URL}/predict`, data)
  } catch (e) {
  }

  let fetchedImageBase64
  return response
    .then(r => fetchedImageBase64 = r.data.img).then(() => {
      return base64ToFile(fetchedImageBase64, "Image", "image/png")
  })
}