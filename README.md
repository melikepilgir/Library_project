# Kütüphane Yönetim Sistemi
Bu proje bir **Kütüphane Yönetim Sistemi** uygulamasıdır.
Kullanıcılar kitap ekleyebilir, silebilir, listeleyebilir ve ISBN numarası ile kitap arayabilir.
Kitaplar "library.json" dosyasında saklanır ve **FastAPI** ile REST API üzerinden erişilir.

# Özellikler
Kitap Ekleme (ISBN ile veriler OpenLibrary API'den çekilir.
Kitap Silme (ISBN ile)
Kitapları Listeleme (JSON Formatında)
FASTAPI ile interaktif API dokümantasyonu
JSON dosyası kullanılarak kalıcı veri saklama

# Gereksinimler
-Python 3.9 veya üstü
-Paketler:
 -fastapi
 -uvicorn
 -requests

# Kurulum
1. Depoyu klonla:
   git clone https://github.com/kullanici/library-system.git
   cd library-system

2. Gerekli paketleri yükle.
   pip install -r requirements.txt
3. requirements.txt içeriği:
   fastapi
   uvicorn
   requests
   
# Kullanım 
API'yi başlatmak için 
   uvicorn api:app --reload
   Tarayıcıdan:
   http://127.0.0.1:8000/books

 # Dosya Yapısı
 project/
│
├── library_project.py   # Book ve Library sınıfları
├── api.py               # FastAPI endpoint'leri
├── library.json         # Kitapların saklandığı dosya (otomatik oluşur)
├── requirements.txt     # Gerekli paketler
└── README.md            # Proje açıklaması



