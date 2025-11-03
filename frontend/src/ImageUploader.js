import React, { useState } from 'react';

function ImageUploader() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  // Handle image file selection
  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // Validate file type
    if (!file.type.startsWith('image/')) {
      setError('Only image files are allowed.');
      setSelectedImage(null);
      setPreviewUrl(null);
      return;
    }

    setError('');
    setSelectedImage(file);
    setPreviewUrl(URL.createObjectURL(file));
  };

  // Send image to backend for prediction
  const handlePredict = async () => {
    if (!selectedImage) return;
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const formData = new FormData();
      formData.append('file', selectedImage);

      // Send POST request to Django API
      const res = await fetch('/api/predict/', {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) {
        throw new Error('Failed to fetch prediction.');
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError('Prediction failed. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center space-y-4 p-4">
      {/* Upload input */}
      <label className="block text-gray-700 font-medium">
        Upload Image
        <input
          type="file"
          accept="image/*"
          onChange={handleImageChange}
          disabled={loading}
          className="block mt-2"
        />
      </label>

      {/* Error message */}
      {error && (
        <p role="alert" className="text-red-500 text-sm">
          {error}
        </p>
      )}

      {/* Image preview */}
      {previewUrl && (
        <img
          src={previewUrl}
          alt="uploaded preview"
          style={{
            width: '150px',
            height: '150px',
            objectFit: 'cover',
            borderRadius: '12px',
            border: '1px solid #ccc',
            opacity: loading ? 0.5 : 1
          }}
        />
      )}

      {/* Predict button */}
      <button
        onClick={handlePredict}
        disabled={!selectedImage || loading}
        className={`px-4 py-2 rounded-lg text-white font-medium ${
          loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700'
        }`}
      >
        {loading ? 'Predicting...' : 'Predict'}
      </button>

      {/* Loading indicator */}
      {loading && (
        <p className="text-gray-500 text-sm italic">Processing image...</p>
      )}

      {/* Prediction results */}
      {result && (
        <div className="mt-4 text-center space-y-1">
          <p className="font-semibold">Prediction Result:</p>
          <p>🐱 Cat: {(result.cat * 100).toFixed(1)}%</p>
          <p>🐶 Dog: {(result.dog * 100).toFixed(1)}%</p>
          <p>❓ Other: {(result.other * 100).toFixed(1)}%</p>
        </div>
      )}
    </div>
  );
}

export default ImageUploader;