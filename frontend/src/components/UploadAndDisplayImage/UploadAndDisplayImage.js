import React, {useState} from "react";
import  "../Button/Button.css";
import './UploadAndDisplayImage.css'


const UploadAndDisplayImage = () => {
  const [selectedImage, setSelectedImage] = useState(null);

  if (selectedImage) {
    return (
      <div className='image_check'>
        <div className='image_check__reject' onClick={()=>setSelectedImage(null)}>x</div>
        <img className='image_check__img' alt="not fount" width={"500px"} src={URL.createObjectURL(selectedImage)} />
        <div className='image_check__accept' onClick={()=>console.log("yes")}>Отправить фото</div>
      </div>
    )
  }

  return (
    <>


      <label htmlFor="upload-photo" className="button">Выбрать фото</label>
      <input
        className='input_file'
        type="file"
        name="photo"
        id="upload-photo"
        onChange={(event) => {
          console.log(event.target.files[0]);
          setSelectedImage(event.target.files[0]);
        }}
      />

    </>
  );
};

export default UploadAndDisplayImage;