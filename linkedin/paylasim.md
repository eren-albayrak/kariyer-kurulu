# LinkedIn paylaşımı

Ek: `kariyer-kurulu-karusel.pdf` (LinkedIn'de "Belge ekle" ile yükleyin; 8 sayfalık karusel olarak görünür).

---

Bir CV'yi yazan kişi her zaman iyi görür. Peki onu okuyacak kurum nasıl görüyor?

Bu soruyla yola çıkıp, kıdemli bir mühendis-yönetici CV'si üzerinde çok ajanlı bir yapay zekâ sistemi kurdum ve adını **Kariyer Kurulu** koydum.

🔹 Önce CV'yi belgeye dayalı hâle getirdik. CV'deki her tarih ve rakam imzalı bir kurum yazısına bağlandı. Türkçe ve İngilizce sürüm aynı kaynak dosyadan üretildi, iki dilin yapısı otomatik olarak denetlendi.

🔹 Sonra CV'yi on jüriye soktuk:
• İki dil jürisi: Türkçe imla ve resmî dil; İngilizcede "çeviri kokan" cümle avı.
• Sekiz işveren jürisi: kamu kurumu, özel sektör grubu, uluslararası yüklenici, Körfez ulusal şirketi, Avrupa operatörü, komşu sektör holdingi, headhunter ve ATS taraması.

Her jüri aynı yedi kriterle puanladı: ilk 7 saniye, rol uyumu, kanıt, güncellik, teknik derinlik, liderlik, sunum. Sonunda "çağır, beklet ya da ele" kararı verdi.

🔹 En sevdiğim katman "jüriye de jüri" oldu. Yapay zekâ jürileri de yanılıyor:
• Biri "PDF'te karakterler bozuk" dedi. Test ettik; sorun jürinin kendi ekranındaymış.
• Biri resmî bir proje adını "düzeltmek" istedi. İmzalı belgeye baktık; öneriyi reddettik.
Hiçbir öneri kaynağa bakılmadan uygulanmadı.

📊 Sonuç (anonim):
• 34 dil bulgusundan 27'si uygulandı.
• 8 işveren jürisinin 5'i mülakata çağırdı, 3'ü beklemeye aldı, eleyen olmadı.
• En güçlü kriter teknik derinlik, en zayıfı kariyer sürekliliği.
• Puanı 6,5'ten yaklaşık 7,9'a çıkarmanın yolu da kriter kriter çıktı.

⚙️ Model ataması da sistemin parçası: yönetim, dil jürileri ve doğrulama Claude Opus'ta; sekiz işveren jürisi paralel çalışan Claude Sonnet ajanlarında. Her işe gerektiği kadar güçlü model.

Skill dosyasını, jüri istemlerini, tek kaynaktan PDF ve Word üreten derleyiciyi ve kurgusal bir örnek raporu açık kaynak olarak paylaştım:
👉 github.com/ferrariW368/kariyer-kurulu

CV'nizin hazırlanmasını ya da hedeflediğiniz kurumların gözünden değerlendirilmesini isterseniz mesaj atmanız yeterli.

#yapayzeka #kariyer #cv #insankaynaklari #claude #ajanlar #açıkkaynak

---

## Kısa sürüm

CV'yi yazan iyi görür; asıl soru onu okuyanın nasıl gördüğü. Bir CV'yi on yapay zekâ jürisine soktum: 2 dil jürisi ve kamu kurumundan headhunter'a, ATS'ye kadar 8 işveren jürisi. Jürilerin iddialarını da belgeyle sınadım, çünkü onlar da yanılıyor. Sistemin adı Kariyer Kurulu ve açık kaynak: github.com/ferrariW368/kariyer-kurulu

## English version

A CV always looks good to the person who wrote it. The real question is how the reader sees it.

I built **Kariyer Kurulu (Career Board)**, a multi-agent AI system. It writes an evidence-based CV in Turkish and English from a single source, then puts it in front of ten simulated juries: two language juries and eight employer panels (public utility, private group, international EPC contractor, Gulf NOC, European operator, adjacent industry, executive search, ATS screen). Every jury scores the CV on the same seven criteria and decides: interview, hold or reject. Then a "jury of the jury" checks every claim against the signed source documents, because AI juries make mistakes too.

Open source: github.com/ferrariW368/kariyer-kurulu
