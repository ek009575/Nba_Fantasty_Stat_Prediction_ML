from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler  
from sklearn.decomposition import PCA  
from xgboost import XGBRegressor
app = Flask(__name__)

# Modeli yükle
with open('nba_fantasy_model.pkl', 'rb') as f:
    saved_objects = pickle.load(f)
    model = saved_objects['model']
    scaler = saved_objects['scaler']
    pca = saved_objects['pca']

@app.route('/')
def home():
    return "Flask API çalışıyor! /predict rotasına POST isteği gönderin."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # JSON formatında gelen veriyi al
        data = request.get_json()  # JSON verisini al
        players = data['players']  # Oyuncu bilgilerini al

        predictions = []

        for player in players:
            name = player['name']
            date = player['date']
            features = player['features']

            # Özellikleri 2D array formatına dönüştür
            features = [features]  # Listeyi 2D array'e dönüştürmek için köşeli parantez ekleyin
            
            # Veri işleme
            features_scaled = scaler.transform(features)  # Standartlaştırma
            features_pca = pca.transform(features_scaled)  # PCA dönüşümü

            # Tahmin yapma
            prediction = model.predict(features_pca)

            # Tahmini ekle
            predictions.append({
                'name': name,
                'date': date,
                'prediction': prediction.tolist()  # Numpy array'i listeye çevir
            })

        # Tahminleri döndür
        return jsonify({"predictions": predictions})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)