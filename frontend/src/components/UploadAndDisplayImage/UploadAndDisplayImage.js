import React, {useState} from "react";
import "../Button/Button.css";
import './UploadAndDisplayImage.css'
import {sendPhoto} from "../../api/methods";
import Loader from "../Loader/Loader";


const UploadAndDisplayImage = () => {
  const [selectedImages, setSelectedImages] = useState([]);
  const [fetchedImages, setFetchedImages] = useState([]);
  const [predict, setPredict] = useState(0);

  const [isLoading, setIsLoading] = useState(false)

  const sendPhotosHandler = (photos) => {
    setIsLoading(true)
    sendPhoto(photos).then(r => {
      setFetchedImages(r.imgs)
      setIsLoading(false)
      setSelectedImages([])
      setPredict(r.predict)
    })
  }

  if (selectedImages.length && !isLoading) {
    return (
      <div className='image_check'>
        {
          Array.from(Array(selectedImages.length).keys()).map((i) => {
              const image = selectedImages[i]
              return (
                <div>
                  <div className='image_check__reject' onClick={() => {
                    setSelectedImages([])
                  }}>x
                  </div>
                  <img className='image_check__img' alt="not fount" width={"500px"}
                       src={URL.createObjectURL(image)}/>
                </div>
              )
            }
          )
        }
        <div className='image_check__accept' onClick={() => sendPhotosHandler(selectedImages)}>Отправить фото</div>
      </div>
    )
  }

  if (fetchedImages.length && !isLoading) {
    return (
      <div className='image_check'>

        {
          Array.from(Array(fetchedImages.length).keys()).map((i) => {
              const image = fetchedImages[i]
              return (
                <div>
                  <div className='image_check__reject' onClick={() => {
                    setFetchedImages([])
                  }}>x
                  </div>
                  <img className='image_check__img' alt="not fount" width={"500px"}
                       src={URL.createObjectURL(image)}/>
                </div>
              )
            }
          )
        }
        <div className="predict">
          {
            predict <= 30
            ? 'Кариес не обнаружен, но не забывайте о профилактических осмотрах!'
            : `Мы уверены на ${predict}%, что вам стоит обратиться к стоматологу.`
          }
        </div>

      </div>
    )
  }

  return (
    <>
      <label htmlFor="upload-photo" className="button">
        {
          isLoading
            ? (
              <Loader/>
            ) : "Выбрать фото"
        }
      </label>
      <input
        className='input_file'
        type="file"
        name="photo"
        multiple
        id="upload-photo"
        onChange={(event) => {
          setSelectedImages(event.target.files);
        }}
      />
    </>
  );
};

export default UploadAndDisplayImage;