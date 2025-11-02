import React, { useState } from 'react';

function ImageUploader() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [error, setError] = useState('');
  const [prediction, setPrediction] = useState('');

  const handleChange = (e) => {
    setError('');
    setPrediction('');
    const file = e.target.files[0];
    if (!file) return;

    if (!file.type.startsWith('image/')) {
      setError('Only image files are allowed');
      setImage(null);
      setPreview(null);
      return;
    }

    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  const handleUpload = async () => {
    if (!image) {
      setError('Please select an image first');
      return;
    }

    const formData = new FormData();
    formData.append('file', image);

    try {
      const res = await fetch('http://localhost:8000/api/predict/', {
        method: 'POST',
        body: formData, // Content-Type is set automatically with FormData
      });

      const data = await res.json();

      if (res.ok) {
        setPrediction(data.prediction);
      } else {
        setError(data.error || 'Prediction failed');
      }
    } catch (err) {
      setError('Error connecting to backend');
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Upload Image for Prediction</h2>
      <input
        aria-label="upload image"
        type="file"
        accept="image/*"
        onChange={handleChange}
      />
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {preview && (
        <div>
          <img
            src={preview}
            alt="uploaded preview"
            style={{ width: 200, marginTop: '1rem', borderRadius: 8 }}
          />
          <div>
            <button
              style={{ marginTop: '1rem' }}
              onClick={handleUpload}
            >
              Send to Backend
            </button>
          </div>
        </div>
      )}

      {prediction && (
        <p style={{ marginTop: '1rem', fontWeight: 'bold' }}>
          Prediction: {prediction}
        </p>
      )}
    </div>
  );
}

export default ImageUploader;
