# Jüri paneli

## Dil jürileri

| Jüri | Bakar | Tipik bulgu |
|---|---|---|
| Türkçe | TDK imla, ek ve tamlama, büyük harf, resmî CV dili, kurum unvanları | "Onay ve sorumluluğunda" → "Onayı ve sorumluluğu altında" |
| İngilizce | Birebir çeviri (calque), sektör terimi, tutarlı yazım, madde dilbilgisi | "Under his approval" → "Approved and was responsible for" |

## İşveren jürileri

Persona seçimi kişinin sektörüne göre yapılır. Her persona gerçekçi bir komitedir: İK, teknik yönetici, işe alan yönetici. Persona havuzu:

| Persona | Neye bakar |
|---|---|
| Türkiye kamu kurumu | Belgeyle kanıt, mevzuat bilgisi, imza yetkisi, kariyer sürekliliği |
| Türkiye özel sektör grubu | Ticari sonuç, ölçek, ekip, regülasyon |
| Uluslararası yüklenici | Sertifika güncelliği, standartlar, ATS anahtar kelimeleri, saha deneyimi |
| Körfez / başka bölge ulusal şirketi | Deneyim yılı, diploma tasdiki, dil seviyesi, referanslar |
| Avrupa operatörü | İSG ve Avrupa standartları, dil seviyesi (CEFR), Avrupa CV normları |
| Komşu sektör | Aktarılabilir yetkinlik, o sektöre özgü kanıt |
| Uluslararası headhunter | Konumlandırma, üst yönetim anlatısı, kâr-zarar sorumluluğu |
| ATS + 7 saniye | Metin çıkarılabilirliği, tarih ayrıştırma, e-posta, anahtar kelime eşleşmesi |

## Puan kartı

| Kriter | Soru |
|---|---|
| İlk 7 saniye | Hızlı taramada ne kalıyor? |
| Rol uyumu | Açık pozisyona ne kadar oturuyor? |
| Kanıt ve ölçülebilirlik | Rakam, ölçek, belgelenebilir sonuç var mı? |
| Güncellik ve süreklilik | Tarihler okunuyor mu, boşluk var mı? |
| Teknik derinlik | Uzmanlık ve sertifikalar ikna ediyor mu? |
| Liderlik kapsamı | Ekip, bütçe, karar yetkisi ne büyüklükte? |
| Sunum ve dil | Düzen ve dil profesyonel mi? |

Ölçek 1–10, 10 nadiren verilir. Karar: **Mülakata çağır**, **Beklemeye al** ya da **Ele**.

## Jüri çıktısı

Her jüri aynı biçimde döner (bkz. [prompts/isveren-jurisi.md](../prompts/isveren-jurisi.md)):

- Persona ve değerlendirdiği rol
- 7 puan + ortalama
- Karar + tek cümle gerekçe
- 3 güçlü yön (CV'deki somut kanıtla), 3 risk
- 3 mülakat sorusu
- Kuruma özel 2 ince ayar
- Tek cümlelik jüri alıntısı

## Etiket

Kurum adları persona profilini tarif etmek için kullanılabilir ("X tipi kamu kurumu"). Tüm çıktılar "simülasyon; gerçek kurum görüşü değildir" notunu taşır ve logo kullanılmaz.
