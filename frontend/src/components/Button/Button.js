import React, {useState} from 'react'
import {sendPhoto} from '../../api/methods'
import './Button.css'

const Button = () => {
    const [isLoading, setIsLoading] = useState(false)
    
    const onClick = (photo) => {
      setIsLoading(true)
      sendPhoto(photo).then(r => {
          console.log(r.data)
      })
    }

    return (
        <button
            className={`button ${isLoading ? 'button__loading' : ''}`}
            onClick={onClick}
        >
            {
                isLoading
                ? "..."
                : "Отправить фото"
            }
        </button>
    )
}

export default Button