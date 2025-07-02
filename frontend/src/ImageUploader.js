import React, { useState } from 'react';

function ImageUploader() {
  const [image, setImage] = useState(null);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setError('');
    const file = e.target.files[0];
    if (!file) return;

    if (!file.type.startsWith('image/')) {
      setError('Only image files are allowed');
      setImage(null);
      return;
    }
    setImage(URL.createObjectURL(file));
  };

  return (
    <div>
      <input
        aria-label="upload image"
        type="file"
        accept="image/*"
        onChange={handleChange}
      />
      {error && <p role="alert">{error}</p>}
      {image && <img src={image} alt="uploaded preview" />}
    </div>
  );
}

export default ImageUploader;
