"""KURGUSAL ÖRNEK ADAY. Kişi, kurumlar ve rakamlar uydurmadır; gerçek biriyle ilgisi yoktur.
FICTIONAL SAMPLE CANDIDATE. Person, organizations and figures are invented.

Block types:
  ("section", title)
  ("entry", bold, rest, [right lines])
  ("bullet", text)
  ("para", text)
  ("labeled", label, text)
Both languages must keep the same block sequence (checked by build_cv.py).
"""

EN = {
    "lang": "en",
    "file": "Ornek_Aday_CV_EN",
    "name": "Deniz Örnek",
    "headline": "Civil Engineer (MSc) · Water Infrastructure Project Director",
    "location": "Türkiye",
    "phone": "+90 500 000 00 00",
    "email": "deniz.ornek@example.com",
    "blocks": [
        ("section", "Executive Profile"),
        ("para", "Civil engineer with 18 years of experience in water supply, wastewater and dam projects. Held positions ranging from site engineer to project director in public utilities and international contractors."),
        ("section", "Selected Projects"),
        ("entry", "Regional Drinking Water Transmission Line", "Sample Water Utility", ["2019 – 2023"]),
        ("bullet", "86 km of DN1200 steel transmission line and 3 pumping stations serving approx. 900,000 residents"),
        ("bullet", "Contract value approx. EUR 140 million; 650 contractor site personnel"),
        ("bullet", "Role: owner's project director for design review, site supervision and commissioning"),
        ("section", "Professional Experience"),
        ("entry", "Sample Water Utility", "Project Director", ["Türkiye", "2019 – 2023"]),
        ("bullet", "Led a 24-person owner's team across design, procurement and construction"),
        ("entry", "Sample International Contractor", "Site Manager", ["Türkiye", "2010 – 2019"]),
        ("bullet", "Delivered 4 wastewater treatment plants on schedule"),
        ("section", "Education"),
        ("entry", "MSc – Sample Technical University", "", ["2008"]),
        ("bullet", "Hydraulics"),
    ],
}

TR = {
    "lang": "tr",
    "file": "Ornek_Aday_CV_TR",
    "name": "Deniz Örnek",
    "headline": "İnşaat Yüksek Mühendisi · Su Altyapısı Proje Direktörü",
    "location": "Türkiye",
    "phone": "+90 500 000 00 00",
    "email": "deniz.ornek@example.com",
    "blocks": [
        ("section", "Yönetici Profili"),
        ("para", "İçme suyu, atık su ve baraj projelerinde 18 yıllık deneyime sahip inşaat mühendisi. Kamu kuruluşlarında ve uluslararası yüklenicilerde şantiye mühendisliğinden proje direktörlüğüne kadar görevlerde bulunmuştur."),
        ("section", "Öne Çıkan Projeler"),
        ("entry", "Bölgesel İçme Suyu İsale Hattı", "Örnek Su İdaresi", ["2019 – 2023"]),
        ("bullet", "Yaklaşık 900.000 kişiye hizmet eden 86 km DN1200 çelik isale hattı ve 3 pompa istasyonu"),
        ("bullet", "Sözleşme bedeli yaklaşık 140 milyon €; yüklenici bünyesinde 650 saha personeli"),
        ("bullet", "Görevi: tasarım kontrolü, saha denetimi ve devreye alma süreçlerinde idare adına proje direktörlüğü"),
        ("section", "Mesleki Deneyim"),
        ("entry", "Örnek Su İdaresi", "Proje Direktörü", ["Türkiye", "2019 – 2023"]),
        ("bullet", "Tasarım, satın alma ve yapım süreçlerinde 24 kişilik idare ekibini yönetmiştir"),
        ("entry", "Örnek Uluslararası Yüklenici", "Şantiye Şefi", ["Türkiye", "2010 – 2019"]),
        ("bullet", "4 atık su arıtma tesisini takvimine uygun olarak teslim etmiştir"),
        ("section", "Eğitim"),
        ("entry", "Yüksek Lisans – Örnek Teknik Üniversitesi", "", ["2008"]),
        ("bullet", "Hidrolik"),
    ],
}
