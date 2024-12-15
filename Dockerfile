# Python 3.9 slim tabanlı bir Docker imajı kullan
FROM python:3.9-slim

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# Gereksinim dosyasını ve uygulama dosyalarını kopyala
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY nba_fantasy_model.pkl nba_fantasy_model.pkl

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Flask uygulamasını çalıştır
CMD ["python", "app.py"]