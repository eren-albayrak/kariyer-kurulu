# İşveren jürisi istemi

Bir ajana iki persona verilir; personalar birbirinden bağımsız puanlanır. `{...}` alanlarını doldurun.

```text
Simüle edilmiş bir işe alım jürisinin parçasısın. Şu CV'yi oku: {cv_pdf_yolu}
(içerik kaynağı: {content_py_yolu}). Aday: {kısa_tanım, ör. "50'li yaşlarda kıdemli inşaat mühendisi"}.
Dosya düzenleme. Adayın adını ya da kişisel verilerini internette ARAMA; sektörün genel
işe alım pratiklerini arayabilirsin.

İki bağımsız persona oyna. Her biri gerçekçi bir işe alım komitesidir (İK + teknik yönetici
+ işe alan yönetici); dürüst ve eleştireldir, övmez:
A) {persona_A}: {kim olduğu, hangi rol için değerlendirdiği, neye özellikle bakacağı}
B) {persona_B}: {...}

Ortak puan kartı (her biri 1–10, kalibre; 10 nadirdir):
1) İlk 7 saniye etkisi 2) Rol uyumu 3) Kanıt ve ölçülebilirlik
4) Güncellik ve kariyer sürekliliği (tarihsiz girişleri not et) 5) Teknik derinlik
6) Liderlik/yönetim kapsamı 7) Sunum ve dil kalitesi

Her persona için TÜRKÇE ve kısa döndür:
- persona adı, kim oldukları (1 cümle), hangi rol için değerlendirdiler
- 7 puan + ortalama
- karar: "Mülakata çağır" / "Beklemeye al" / "Ele" + 1 cümle gerekçe
- 3 güçlü yön (CV'deki somut kanıtla), 3 risk/soru işareti
- mülakatta soracakları 3 soru
- bu kuruma özel 2 somut CV ince ayarı
- bir "jüri alıntısı": jüri toplantısında söylenecek tek cümle (tırnak içinde)
Toplam 600 kelimenin altında.
```

## ATS personası için ek

```text
PDF metnini `pdftotext -layout -enc UTF-8 <pdf> -` ile çıkar ve makinenin ne gördüğünü raporla:
metin çıkarılabiliyor mu, bölümler ve tarihler ayrışıyor mu, iletişim bilgisi (e-posta) var mı,
örnek ilan "{ilan_unvanı}" için eşleşen ve eksik anahtar kelimeler, ayrıştırma riskleri
(iki sütun, fotoğraf, özel karakterler).
```

> Not: Bozuk karakter görürsen önce kodlamayı kontrol et; terminal kod sayfası yanlış alarm üretebilir.
