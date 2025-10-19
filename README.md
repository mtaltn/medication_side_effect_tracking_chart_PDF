# medication_side_effect_tracking_chart_PDF
İlaç kullanımına bağlı gelişebilecek yan etkilerin düzenli şekilde takip edilmesini sağlamak için geliştirilmiş basit bir PDF çizelgesi oluşturma aracıdır. Kullanıcılar tabloyu özelleştirerek kendi ihtiyaçlarına uygun çıktılar alabilir.


# 💊 İlaç Yan Etki Takip Çizelgesi

Bu proje, ilaç kullanımına bağlı olarak gelişebilecek yan etkilerin düzenli bir şekilde takip edilmesini sağlamak amacıyla geliştirilmiştir. Python kullanılarak oluşturulan bu uygulama, kullanıcılara tablo formatında PDF çıktısı üretme imkânı sunar. Böylece sağlık çalışanları, hastalar veya ilgili birimler ilaç yan etkilerini kolayca kaydedebilir ve takip edebilir.

## 🚀 Özellikler

- 📄 **PDF çıktısı üretir** — Varsayılan olarak yatay (landscape) yönlendirmede çalışır.  
- 🧩 **Kolay özelleştirme** — Tablo başlıkları ve satır sayısı düzenlenerek kurumlara veya kişilere özel çıktı alınabilir.  
- 📝 **Yapılandırılmış tablo görünümü** — 7 günlük takip çizelgesi otomatik olarak oluşturulur.  
- 🌐 **Açık kaynak** — Kod üzerinde kolayca değişiklik yapılarak farklı senaryolara uyarlanabilir.

## 🧱 Teknolojiler

- [Python 3](https://www.python.org/)  
- [fpdf](https://pypi.org/project/fpdf/) — PDF dosyaları oluşturmak için kullanılır.

## 📄 Kullanım

1. Gerekli bağımlılığı yükleyin:  
   ```bash
   pip install fpdf


Projeyi çalıştırın:

python IlacYanEtkiYakipCizelgesi.py


Çalıştırma sonucunda proje dizininde Ilac_Yan_Etki_Takip_Cizelgesi.pdf dosyası oluşacaktır.

📝 Özelleştirme

Tablo başlıklarını değiştirmek için dosya içindeki columns listesini düzenleyebilirsiniz.

Satır sayısını değiştirmek için rows yapısını istediğiniz gün sayısına göre güncellemeniz yeterlidir.

Kolon genişliklerini col_widths listesi üzerinden değiştirebilirsiniz.

↕️ Dikey (Portrait) Çıktı Alma

Varsayılan olarak PDF çıktısı yatay yönlendirmededir.
Dikey yapmak için aşağıdaki satırı:

pdf = FPDF(orientation='L')  # Landscape (yatay)


şu şekilde değiştirin:

pdf = FPDF(orientation='P')  # Portrait (dikey)


⚠️ Dikey formata geçerken tablo genişliklerinin toplamının sayfa genişliğini aşmamasına dikkat edin. Gerekirse col_widths değerlerini küçültebilirsiniz.

📌 Örnek Görünüm
Gün	Tarih	Bulantı / Kusma	Baş Ağrısı	Karın Ağrısı / Kramp	Göğüs Hassasiyeti	Adet Düzensizliği	Diğer Belirtiler	Notlar
1								
2								
🖼️ PDF Çıktısı Önizlemesi

Aşağıda oluşturulan PDF çizelgesine örnek bir görüntü yer almaktadır:

example-output.png görselini kendi proje klasörüne ekleyerek README'de önizlemeyi gösterebilirsiniz.

🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz!
Bir hata fark ettiyseniz veya yeni bir özellik eklemek istiyorsanız lütfen bir Pull Request açın ya da Issue oluşturun.

Bu projeyi forklayın.

Yeni bir branch oluşturun: git checkout -b feature/yenilik.

Değişikliklerinizi commit edin: git commit -m 'Yeni özellik eklendi'.

Branch'i gönderin: git push origin feature/yenilik.

Pull Request açın.

