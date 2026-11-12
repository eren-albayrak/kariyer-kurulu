---
name: kariyer-kurulu
description: "Bir kişinin bilgilerinden ve mevcut CV'sinden Türkçe ve İngilizce, belgeye dayalı, eşit kalitede CV üretir; CV'yi dil jürileri ve sektöre göre seçilen işveren jürilerinden (kamu, özel, uluslararası, headhunter, ATS) geçirir, jüri iddialarını kaynak belgeyle doğrular ve puan, karar, puan artırma senaryoları içeren sunum ve PDF rapor hazırlar. Kullan: CV hazırlama/çevirme/güncelleme, CV inceleme, işveren gözünden değerlendirme, kariyer yönlendirme. Kullanma: iş ilanına toplu başvuru, sahte deneyim/belge üretimi."
---

# Kariyer Kurulu: çok ajanlı CV hazırlama ve jüri sistemi

Bir CV'yi yazan kişi iyi görür; önemli olan onu okuyacak kurumun nasıl gördüğüdür. Bu skill CV'yi önce belgeye dayalı ve iki dilde eşit kalitede hazırlar, sonra farklı işverenlerin gözünden jüriye sokar.

## Temel kurallar

1. **Kaynak yoksa bilgi yok.** CV'ye giren her tarih, unvan ve rakam bir kaynağa dayanır: orijinal CV, imzalı kurum yazısı, diploma, sertifika ya da kişinin kendi beyanı. Kaynak olmayanı uydurma; kişiye sor ya da boş bırak.
2. **Belge ile beyan çelişirse imzalı belge esastır.** Çelişkiyi kişiye gösterip kararı ona bırak (örnek: kişi "2002" dedi, imzalı yazı "2003" diyor).
3. **Kişinin tercihi puandan önce gelir.** Kişi bir alanı bilerek boş bırakıyorsa (tarih, fotoğraf, kişisel bilgi), jüri ne derse desin zorlanmaz; yalnızca etkisi açıkça söylenir.
4. **Tek kaynak, iki dil.** TR ve EN aynı içerik dosyasından üretilir; blok yapısı eşitliği otomatik denetlenir. Bir dilde yapılan düzeltme diğerine de işlenir.
5. **Jüri de yanılabilir.** Hiçbir jüri önerisi kaynağı kontrol edilmeden uygulanmaz.
6. **Gizlilik.** TC kimlik, sicil numarası, ev adresi gibi veriler yalnızca kişinin onayıyla pakette kalır. Kişinin adı ve verisi dış servislere (arama, yayın) gönderilmez.
7. **Kişiye yazılan mesajlar** kişinin istediği hitap ve üslupla yazılır (ör. "siz" dili, emir kipi yok).

## Aşama 0: Girdiler (başlamadan topla)

- Mevcut CV (docx/pdf) ve fotoğraf (isteğe bağlı).
- İmzalı belgeler: çalışma belgesi, iş deneyim belgesi, görev yazısı, diploma, sertifikalar.
- CV'nin amacı ve kitlesi: Türkiye kamu, özel sektör, yurt dışı, danışmanlık, yönetim kurulu.
- Eksik bilgiler için kısa bir **bilgi formu** (Word, onay kutulu). Kitle teknoloji ile arası iyi değilse form kısa tutulur; kişi "çok detaylı" derse formdan vazgeçilir, mevcut bilgiyle ilerlenir.

## Aşama 1: Kaynak envanteri

Her belge için bir satır: belge adı, tarih, sayı, imzalayanlar, içerdiği olgular (tarih, unvan, tutar, kapasite). Rakamlar belgedeki gibi yazılır; yuvarlama CV aşamasında yapılır. Tarama PDF'leri görsel olarak okunur, OCR'a körü körüne güvenilmez.

## Aşama 2: İçerik (tek kaynak)

- `content.py` içinde `TR` ve `EN` sözlükleri, aynı blok sırası: `section`, `entry` (başlık, kurum, sağ sütun satırları), `bullet`, `para`, `labeled`.
- Yapı: Profil → Öne çıkan projeler (rakamlarla) → Mesleki deneyim → Eğitim → Uzmanlık → Sertifikalar → Kişisel bilgiler → Destekleyici belgeler.
- Proje maddeleri: kapsam + ölçek (tutar, kapasite, ekip) + kişinin rolü. "Görev aldı" yerine ne yaptığı.
- Halka açık kaynaktan eklenen proje bilgisi (ör. kapasite hedefi) kaynağıyla not edilir ve kişiye teyit ettirilir.

## Aşama 3: Üretim

- PDF: Typst (rendercv şablonu) ile; DOCX: python-docx ile aynı içerikten.
- Kontrol: her iki çıktının sayfa sayısı, taşma, yetim satır; DOCX Word'de PDF'e aktarılarak görsel kontrol edilir.
- Paket: CV + imzalı belgeler (EN pakette çeviri + orijinal). Çeviriler "aslı ektedir" düzeninde, tarih/sayı aynen.

## Aşama 4: Dil jürileri

| Jüri | Model | Bakar |
|---|---|---|
| Türkçe dil jürisi | Opus | TDK imla, ek ve tamlama hataları, resmî CV dili, kurum unvanları |
| İngilizce dil jürisi | Opus | Birebir çeviri kokusu (calque), sektör terimi, ABD/İngiliz yazım tutarlılığı, madde dilbilgisi |

Çıktı biçimi: önem (hata / iyileştirme), birebir mevcut metin, öneri, tek satır gerekçe. Ana ajan uygular; TR/EN eşitliğini korur. Resmî belgeyle çelişen öneri reddedilir (ör. resmî proje adı).

## Aşama 5: İşveren jürileri

Kişinin sektörüne göre 6-8 persona seç. Her persona gerçekçi bir işe alım komitesidir (İK + teknik yönetici + işe alan yönetici) ve **eleştireldir, övmez**. Persona havuzu:

- Türkiye kamu kurumu (kişinin geçmiş işverenlerinin profilinde)
- Türkiye özel sektör grubu (aynı sektör)
- Uluslararası yüklenici / danışmanlık firması
- Körfez veya başka bölgeden ulusal şirket
- Avrupa'da aynı alanda operatör
- Komşu sektör (ör. ağır sanayi, madencilik)
- Uluslararası yönetici arama firması (headhunter)
- ATS + 7 saniyelik ön eleme (PDF metni gerçekten çıkarılır, anahtar kelime eşleşmesi raporlanır)

Kurum adı persona profilini tarif etmek için kullanılabilir ("X tipi kamu kurumu"), ama çıktılar her zaman **simülasyon** diye etiketlenir; gerçek kurum görüşü gibi sunulmaz, logo kullanılmaz.

### Ortak puan kartı (1-10, 10 nadir)

1. İlk 7 saniye etkisi
2. Rol uyumu
3. Kanıt ve ölçülebilirlik
4. Güncellik ve kariyer sürekliliği
5. Teknik derinlik
6. Liderlik ve yönetim kapsamı
7. Sunum ve dil kalitesi

Her jüri döner: persona, değerlendirdiği rol, 7 puan + ortalama, karar (Mülakata çağır / Beklemeye al / Ele), 3 güçlü yön (somut kanıtla), 3 risk, 3 mülakat sorusu, kuruma özel 2 ince ayar, tek cümlelik jüri alıntısı. Ajanlara kişinin adını internette aratmaları yasaklanır.

## Aşama 6: Doğrulama ve sentez (Opus)

- Her jüri iddiasını kaynakla sına: belge, PDF metni, kişinin beyanı. Sonuç: uygulandı / reddedildi (gerekçe) / yanlış alarm.
- Puanları ısı haritasında topla (jüri × kriter), panel ortalamasını ve kriter ortalamalarını hesapla.
- Ortak bulgular: kaç jüri aynı konuya değindi.
- **Puan artırma:** her kriter için kaybedilen puanın gerekçesi → yapılacak iş → tahmini hedef puan. Üç senaryo: bugün / hızlı paket (yeni bilgi gerektirmeyen) / tam paket. Tahmin olduğunu yaz.
- Ölçülemeyen kriteri unutma: sektördeki itibar, referanslar.

## Aşama 7: Teslim

- Sunum (16:9, 20-22 slayt): kapak, sonuç tek bakışta, sistem, puan kartı, dil jürileri (önce/sonra), jüriye de jüri, panel tablosu, jüri başına slayt, ısı haritası, ortak bulgular, puan artırma, senaryolar, öneriler, itibar, kapanış.
- PDF: sunumdan üretilir, her sayfa görsel olarak kontrol edilir.
- Kişiye mesaj: kısa, kişinin üslubuyla; istenirse mizahi. Ne yaptık, neden yaptık, sonuç, karar kimde.
- Dosyalar: `01_Kaynaklar`, `02_Soru_Cevap`, `03_Paylasima_Hazir/{Turkce,English}`, `04_Juri_Degerlendirmesi`.

## Model ataması

| İş | Model | Neden |
|---|---|---|
| Planlama, kaynak uzlaştırma, sentez, son kabul | Opus | Yüksek yargı ve risk |
| TR ve EN dil jürisi | Opus | Dil doğruluğu |
| İşveren jürileri (paralel) | Sonnet | Çerçevesi belli değerlendirme |
| Dosya kopyalama, format kontrolü | Haiku (gerekirse) | Mekanik iş |

Bir iş alt kademede güvenle yapılabiliyorsa üst kademe kullanılmaz; kalite riski varsa bir üst kademeye çıkılır.

## Öğrenilen tuzaklar

- Jüri "PDF'te karakterler bozuk" dedi; neden kendi terminalinin kodlamasıydı. Metni UTF-8 ile yeniden çıkarıp doğrula.
- Jüri resmî proje adındaki yazımı "düzeltmek" istedi; resmî belgedeki biçim korunur.
- Kişinin beyanı ile imzalı yazı çelişti; kişi imzalı yazıyı esas aldı. Çelişkiyi her zaman göster.
- Uzun bilgi formu kitleyi yorar; kısa tut ya da hiç kullanma.
- Tarihsiz girişler her jürinin ortak sorusu olur; kişi boş bırakmayı seçerse mülakat için iki cümlelik sözlü özet öner.
- E-posta yoksa birçok ATS kaydı tamamlayamaz.

## Tamamlanma kontrolleri

- TR ve EN aynı blok yapısında, ikisi de görsel olarak kontrol edildi.
- Her rakam ve tarih bir kaynağa bağlı; çelişkiler kişiye gösterildi.
- Jüri önerilerinin her biri için uygulandı/reddedildi/yanlış alarm kaydı var.
- Simülasyon etiketi her jüri çıktısında var.
- Kişisel veriler kişinin onayı olmadan pakette değil.
