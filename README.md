cat <<EOF > README.md
# 🏠 Emlak Fiyat Tahmin Analizi

Bu proje, **California Housing** veri seti kullanılarak geliştirilmiş bir makine öğrenmesi uygulamasıdır. 

### 🚀 Özellikler
- **Model:** Çoklu Doğrusal Regresyon (Multiple Linear Regression).
- **Backend:** FastAPI (Python).
- **Frontend:** React.js.
- **Analiz:** Korelasyon ısı haritası ve model performans metrikleri (R², MSE).

### 🛠️ Kurulum ve Çalıştırma

**1. Backend Kurulumu (Python)**
\`\`\`bash
# Sanal ortam oluşturma ve aktif etme (Mac/Linux)
python3 -m venv venv
source venv/bin/activate

# Gerekli kütüphanelerin yüklenmesi
pip install -r requirements.txt

# Sunucuyu başlatma
uvicorn main:app --reload
\`\`\`

**2. Frontend Kurulumu (React)**
\`\`\`bash
# Yeni bir terminal sekmesinde:
cd emlak-frontend
npm install
npm start
\`\`\`
EOF
