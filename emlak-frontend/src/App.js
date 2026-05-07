import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  // Modelin beklediği 8 parametre ve varsayılan değerleri
  const [formData, setFormData] = useState({
    MedInc: 3.87,     // Medyan Gelir
    HouseAge: 28.0,   // Bina Yaşı
    AveRooms: 5.4,    // Ort. Oda Sayısı
    AveBedrms: 1.1,   // Ort. Yatak Odası
    Population: 1425, // Nüfus
    AveOccup: 3.0,    // Evdeki Kişi Sayısı
    Latitude: 34.05,  // Enlem
    Longitude: -118.24 // Boylam
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: parseFloat(e.target.value) });
  };

  const handlePredict = async () => {
    setLoading(true);
    try {
      // FastAPI backend'imize istek atıyoruz
      const response = await axios.post('http://127.0.0.1:8000/predict', formData);
      setPrediction(response.data.estimated_price_usd);
    } catch (error) {
      console.error("Hata:", error);
      alert("Backend sunucusu (main.py) çalışıyor mu? Kontrol et!");
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🏠 Emlak Fiyat Tahmin Botu</h1>
        
        <div className="form-grid">
          {Object.keys(formData).map((key) => (
            <div key={key} className="input-group">
              <label>{key}</label>
              <input 
                type="number" 
                name={key} 
                step="0.01"
                value={formData[key]} 
                onChange={handleChange} 
              />
            </div>
          ))}
        </div>

        <button className="predict-btn" onClick={handlePredict} disabled={loading}>
          {loading ? "Hesaplanıyor..." : "Fiyatı Tahmin Et"}
        </button>

        {prediction && (
          <div className="result-card">
            <h3>Tahmin Edilen Fiyat</h3>
            <h2 className="price">${prediction.toLocaleString()}</h2>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;