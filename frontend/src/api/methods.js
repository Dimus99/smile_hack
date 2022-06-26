import axios from 'axios'
import {base64ToFile, getBase64} from "../helpers/b64";

const BASE_URL = 'http://185.93.110.39:5000'

export const sendPhoto = async photos => {
  let response
  const photos_data_list = []
  for (let i = 0; i < photos.length; i++) {
    const photoBase64 = await getBase64(photos[i])
    const img = photoBase64.split(',').slice(1, photoBase64.length)
    const b64_prefix = photoBase64.split(',')[0]
    const data = [
      b64_prefix,
      img,
    ]

    photos_data_list.push(data)
  }


  try {
    response = axios.post(`${BASE_URL}/predict`, {imgs: photos_data_list})
  } catch (e) {
  }


  return await response
    .then(r => {
      return r.data
    }).then(async (data) => {
      const files = []
      for (let i = 0; i < data.imgs.length; i++) {
        const b64 = data.imgs[i]
        const file = await base64ToFile(b64, "Image", "image/png")
        files.push(file)
      }

      return {imgs:files, predict: data.predict}
    })
}