# Raspberry Pi 4 Kamera Canlı Yayın Sistemi

Bu proje, Raspberry Pi 4 ve resmi kamera modülü kullanılarak geliştirilmiş, düşük gecikmeli canlı video yayın sistemidir. Flask tabanlı web arayüzü sayesinde yerel ağ üzerinden veya port yönlendirme ile internet üzerinden erişim sağlanabilir.

## 📌 Temel Özellikler

- **Gerçek Zamanlı Akış**: Picamera2 kütüphanesi ile optimize edilmiş 640x480 çözünürlükte akış
- **Güvenlik**: HTTP Basic Authentication ile korumalı erişim
- **Multi-Threading**: Ayrı thread'lerde kamera okuma ve sunucu işlemleri
- **Responsive Tasarım**: Mobil cihazlardan da erişime uygun web arayüzü
- **Hata Yönetimi**: Kamera bağlantı sorunlarında otomatik hata mesajı

## 🛠 Kurulum Adımları

### 1. Ön Gereksinimler
- Raspberry Pi 4 (4GB+ RAM önerilir)
- Raspberry Pi Kamera Modülü veya HQ Kamera
- Raspberry Pi OS (64-bit önerilir)
- Python 3.9+

### 2. Kamera Etkinleştirme
```bash
sudo raspi-config
# Interface Options > Camera > Enable
sudo reboot
