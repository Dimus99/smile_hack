import axios from 'axios'

const BASE_URL = 'http://localhost:8080'

export const sendPhoto = photo => {
    console.log(photo);
    let response
    try {
        response = axios.post(`${BASE_URL}/send_photo`, photo)
    } catch (e) {
        console.log(e)
    }

    return response
}