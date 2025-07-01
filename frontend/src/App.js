import React, { useState } from 'react';

function App() {
  const [number, setNumber] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/api/double/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ number: parseFloat(number) }),
    });
    const data = await res.json();
    setResult(data.result);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Double a Number (React → Django API)</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          value={number}
          onChange={(e) => setNumber(e.target.value)}
          placeholder="Enter a number"
        />
        <button type="submit">Submit</button>
      </form>
      {result !== null && <p>Result: {result}</p>}
    </div>
  );
}

export default App;