# LinkedIn paylaşımı

## Paylaşım planı

| Ne | Nasıl |
|---|---|
| Biçim | Metin + tanıtım videosu (`kariyer-kurulu-tanitim.mp4`, 4:5, ~40 sn, sessiz). Alternatif: video yerine `kariyer-kurulu-karusel.pdf` belge olarak. |
| Video ayarı | Altyazı gerekmez; metin videonun içinde. Kapak karesi olarak ilk sahne kullanılabilir. |
| Linkler | Gövdeye değil, **ilk yoruma** (aşağıda hazır). Gövdedeki dış link gönderinin erişimini düşürebilir. |
| Zaman | Salı–Perşembe, 08.00–10.00 ya da 12.00–13.00 |
| Etiket | 3–5 hashtag |

---

## Gönderi metni (kopyala-yapıştır)

Bir CV'yi 10 jüriye soktum.
Hiçbiri elemedi. Ama 8'inden 6'sı aynı soruyu sordu.

Bir CV'yi yazan kişi onu hep iyi görür. Asıl soru şu: Okuyan kurum nasıl görüyor?

Bunu ölçmek için yapay zekâ ajanlarıyla bir sistem kurdum. Adı Kariyer Kurulu.

Nasıl çalışıyor?

→ CV önce belgeye dayalı hâle geliyor: her tarih ve rakam imzalı bir kurum yazısına bağlanıyor.
→ Türkçe ve İngilizce sürüm aynı kaynaktan çıkıyor, iki dil birbirinden kopmuyor.
→ İki dil jürisi imlayı ve "çeviri kokan" cümleleri ayıklıyor.
→ Sekiz işveren jürisi CV'yi kendi masasından okuyor: kamu kurumu, özel sektör, uluslararası yüklenici, Körfez şirketi, Avrupa operatörü, komşu sektör, headhunter ve otomatik başvuru tarama sistemi (ATS).
→ Hepsi aynı 7 kriterle puanlıyor ve karar veriyor: çağır, beklet ya da ele.

En sevdiğim kısım "jüriye de jüri" oldu.
Bir jüri "PDF'te karakterler bozuk" dedi. Test ettim: sorun jürinin kendi ekranındaymış.
Bir başkası resmî bir proje adını "düzeltmek" istedi. İmzalı belgeye baktım, öneriyi reddettim.
Yapay zekâ jürisi de yanılıyor; bu yüzden hiçbir öneri kaynağa bakılmadan uygulanmıyor.

Kıdemli bir mühendis-yönetici CV'sinde sonuç:
• 34 dil bulgusu, 27 düzeltme
• 8 işveren jürisinden 5'i "mülakata çağır", 3'ü "beklet", eleyen yok
• Puanı 6,5'ten yaklaşık 7,9'a çıkaracak yol kriter kriter belli

Model ataması da sistemin parçası: yönetim, dil jürileri ve doğrulama Claude Opus'ta; sekiz işveren jürisi paralel çalışan Claude Sonnet ajanlarında.

Hepsi açık kaynak. Kendi CV'nizde denemek isterseniz kurulum da gerekmiyor: tek bir MD dosyasını kullandığınız yapay zekâ asistanına yükleyip CV'nizi eklemeniz yeterli. Link ilk yorumda.

Sizce bir CV'de ilk 7 saniyede ne görünmeli?

#yapayzeka #kariyer #cv #açıkkaynak #claude

---

## İlk yorum (gönderiden hemen sonra)

🔗 Kaynak kod, skill ve örnek rapor: https://github.com/eren-albayrak/kariyer-kurulu
🧩 Tek dosyalık sürüm (kendi yapay zekânıza yükleyin): https://github.com/eren-albayrak/kariyer-kurulu/blob/main/KARIYER-KURULU.md
📄 Kullanım rehberi (neler hazırlanmalı, neye dönüşür): https://github.com/eren-albayrak/kariyer-kurulu/blob/main/docs/kariyer-kurulu-basvuru-rehberi.pdf

---

## Kısa sürüm

Bir CV'yi 10 yapay zekâ jürisine soktum: 2 dil jürisi ve kamu kurumundan headhunter'a, ATS'ye kadar 8 işveren jürisi. Jürilerin iddialarını da belgeyle sınadım, çünkü onlar da yanılıyor. Sistemin adı Kariyer Kurulu ve açık kaynak.

## English version

I put one CV in front of 10 juries.
None rejected it. But 6 of the 8 employer panels asked the same question.

Kariyer Kurulu (Career Board) is a multi-agent AI system. It turns a CV into an evidence-based document in Turkish and English from a single source, then runs it past two language juries and eight simulated employer panels: public utility, private group, international EPC contractor, Gulf NOC, European operator, adjacent industry, executive search and an ATS screen. Every panel scores the same seven criteria and decides: interview, hold or reject. A "jury of the jury" then checks every claim against the signed source documents, because AI juries make mistakes too.

Open source. No setup needed to try it: upload a single Markdown file to your own AI assistant together with your CV. Link in the first comment.

#ai #careers #resume #opensource
