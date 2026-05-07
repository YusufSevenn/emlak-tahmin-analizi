import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# 1. Veri setini yükleyelim
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df['Price'] = california.target  # Fiyat sütununu ekleyelim (Hedef değişken)

# 2. İlk 5 satıra bakalım
print("--- Veri Setinin İlk 5 Satırı ---")
print(df.head())

# 3. Veri seti hakkında genel bilgi
print("\n--- Veri Seti Özeti ---")
print(df.info())

# 4. Korelasyon Analizi (Sunum için harika bir görsel olur)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Değişkenler Arasındaki Korelasyon")
plt.show()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib 

# 1. Veriyi Özellikler (X) ve Hedef (y) olarak ayıralım
# Price bizim tahmin etmek istediğimiz değer, diğerleri girdi (input)
X = df.drop('Price', axis=1)
y = df['Price']

# 2. Veriyi %80 Eğitim, %20 Test olarak bölelim
# random_state=42 sayesinde her çalıştırdığımızda aynı sonucu alırız
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Modeli Oluştur ve Eğit
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Tahmin Yap ve Başarıyı Ölç
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Model Başarı Metrikleri ---")
print(f"Hata Payı (MSE): {mse:.4f}")
print(f"Başarı Skoru (R2): {r2:.4f}")

# 5. Modeli Dosya Olarak Kaydet (Canlıya almak için bu dosya lazım)
joblib.dump(model, 'emlak_model.pkl')
print("\n'emlak_model.pkl' dosyası başarıyla oluşturuldu!")