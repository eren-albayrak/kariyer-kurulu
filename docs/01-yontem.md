# Yöntem

Kariyer Kurulu yedi aşamada çalışır. Her aşamanın çıktısı bir sonrakinin girdisidir; hiçbir aşama atlanmaz.

| Aşama | Girdi | Çıktı | Kontrol |
|---|---|---|---|
| 0. Girdiler | Mevcut CV, belgeler, amaç | Eksikler listesi, gerekirse kısa bilgi formu | Kitle ve amaç yazılı |
| 1. Kaynak envanteri | Belgeler | Olgu tablosu (belge, tarih, sayı, olgu) | Her olgu bir belgeye bağlı |
| 2. Tek kaynak içerik | Olgu tablosu | `content.py` (TR + EN) | Blok yapısı eşitliği (otomatik) |
| 3. Üretim | `content.py` | PDF (Typst) + DOCX | Sayfa sayısı, taşma, görsel kontrol |
| 4. Dil jürileri | PDF + içerik | Bulgu listesi | Her bulgu: uygulandı / reddedildi |
| 5. İşveren jürileri | PDF | 8 jüri raporu | Ortak puan kartı, simülasyon etiketi |
| 6. Doğrulama ve sentez | Raporlar + belgeler | Isı haritası, ortak bulgular, senaryolar | Her iddia kaynakla sınandı |
| 7. Teslim | Hepsi | Sunum, PDF rapor, kişiye mesaj | Kişinin üslubu, kişisel veri kontrolü |

## Neden tek kaynak?

Çevirmenle çalışılan CV'lerde iki dil zamanla birbirinden kopar: Türkçede düzeltilen tarih İngilizcede eski kalır. Kariyer Kurulu'nda iki dil aynı dosyadadır ve derleyici, iki dilin blok yapısı aynı değilse durur. Bir düzeltme her zaman iki dile birden işlenir.

## Neden belge önce gelir?

Jüri, işveren ve mülakatçı aynı soruyu sorar: "Bunu nereden biliyoruz?" CV'deki her rakamın arkasında imzalı bir yazı varsa CV, destekleyici belgelerle birlikte bir dosya olarak gönderilebilir. İngilizce pakette her belgenin çevirisi aslıyla birlikte durur.

## Neden jüriye de jüri?

Yapay zekâ jürileri hızlıdır ama yanılabilir. Gerçek bir çalışmada:

- Bir dil jürisi resmî bir proje adındaki yazımı "düzeltmek" istedi; imzalı belgedeki biçim korundu.
- Bir ATS jürisi PDF'teki özel karakterlerin bozuk olduğunu iddia etti; metin yeniden çıkarıldı, sorun jürinin kendi ekranındaydı.
- Bir jüri bir diploma unvanını abartılı buldu; kaynak belgeyle uyumlu olduğu için korundu.

Bu yüzden ana ajan her öneriyi kaynağa karşı test eder ve sonucu kaydeder.

## Puan artırma

Jüriler puan kırarken gerekçe yazar. Sentez aşamasında bu gerekçeler kriter bazında toplanır:

```
kriter → bugünkü ortalama → puanı kıran gerekçe → yapılacak iş → tahmini hedef
```

Sonra üç senaryo hesaplanır: **bugün**, **hızlı paket** (yeni bilgi gerektirmeyen düzeltmeler: e-posta, dil seviyesi, hedef başlık) ve **tam paket**. Değerler tahmindir ve öyle etiketlenir; hangi paketin uygulanacağına CV sahibi karar verir.
