import React, {useState} from "react";
import "../Button/Button.css";
import './UploadAndDisplayImage.css'
import {sendPhoto} from "../../api/methods";
import Loader from "../Loader/Loader";


const UploadAndDisplayImage = () => {
  const [selectedImage, setSelectedImage] = useState(null);

  const [isLoading, setIsLoading] = useState(false)

  const onClick = (photo) => {
    setIsLoading(true)
    let res
    sendPhoto(photo).then(r => res = r)
    setIsLoading(false)
    setSelectedImage(null)
  }

  if (selectedImage) {
    return (
      <div className='image_check'>
        <div className='image_check__reject' onClick={() => {
          setSelectedImage(null)
          setIsLoading(false)
        }}>x</div>
        <img className='image_check__img' alt="not fount" width={"500px"} src={URL.createObjectURL(selectedImage)}/>
        <div className='image_check__accept' onClick={() => onClick(selectedImage)}>Отправить фото</div>
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
        id="upload-photo"
        onChange={(event) => {
          setSelectedImage(event.target.files[0]);
        }}
      />

    </>
  );
};

export default UploadAndDisplayImage;