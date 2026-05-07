from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# 1. FastAPI Uygulamasını ve Eğittiğimiz Modeli Yükleyelim
app = FastAPI()
model = joblib.load('emlak_model.pkl')

# 2. CORS Ayarları (React frontend'imizden istek atabilmek için şart)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Geliştirme aşamasında her yerden gelen isteğe izin veriyoruz
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Request Gövdesini (Body) Tanımlayalım
# Hatırlarsan modelimizde 8 tane girdi vardı
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def read_root():
    return {"status": "API calisiyor", "model": "California Housing Regression"}

@app.post("/predict")
def predict_price(data: HouseFeatures):
    # Gelen veriyi modelin beklediği 2D array formatına çeviriyoruz
    input_data = np.array([[
        data.MedInc, data.HouseAge, data.AveRooms, 
        data.AveBedrms, data.Population, data.AveOccup, 
        data.Latitude, data.Longitude
    ]])
    
    # Tahmin yapalım
    prediction = model.predict(input_data)
    
    # Sonucu döndürelim (100.000$ birimiyle çarparak daha gerçekçi hale getirebilirsin)
    predicted_value = float(prediction[0])
    return {
        "prediction": round(predicted_value, 4),
        "estimated_price_usd": round(predicted_value * 100000, 2)
    }