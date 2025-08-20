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

 # Endpoints
1. Get/ Books
Açıklama: Kütüphanedeki tüm kitapları JSON formatında döndürür.
Response Örneği:
[
  {
    "title": "Ulysses",
    "author": "James Joyce",
    "isbn": "978-0199535675"
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "isbn": "978-0451524935"
  }

2.Post/ Books
Açıklama: POST isteğinde verilen ISBN numarasıyla Open Library API’den kitap bilgilerini çekip kütüphaneye ekle
Response Örneği:
json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "978-0321765723"
}
3.Delete/ Books(isbn)
Açıklama: Belirtilen ISBN numarasına sahip kitabı kütüphaneden siler.
Response Örneği:
{
  "message": "Book with ISBN 978-0321765723 was deleted successfully."
}
 


 # Dosya Yapısı
 project/
│
├── library_project.py   # Book ve Library sınıfları
├── api.py               # FastAPI endpoint'leri
├── library.json         # Kitapların saklandığı dosya (otomatik oluşur)
├── requirements.txt     # Gerekli paketler
└── README.md            # Proje açıklaması



