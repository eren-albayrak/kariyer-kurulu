# Model ataması

Kariyer Kurulu kademeli model sistemiyle çalışır: her iş, onu güvenle yapabilen en uygun modele verilir. Ana ajan iş başlamadan bir atama tablosu yazar.

| İş | Model | Neden |
|---|---|---|
| Planlama, kaynak envanteri, çelişkileri uzlaştırma | Opus | Yüksek yargı; yanlış olgu CV'yi değersizleştirir |
| Türkçe ve İngilizce dil jürisi | Opus | Dil doğruluğu ve doğal üslup ince ayrım ister |
| 8 işveren jürisi | Sonnet, paralel | Çerçevesi belli değerlendirme; paralel çalışınca hızlı ve ucuz |
| Doğrulama, sentez, son kabul | Opus | Jürilerin çelişen görüşlerini belgeyle uzlaştırma |
| Dosya kopyalama, format kontrolü | Haiku (gerekirse) | Mekanik iş |

## İlkeler

- **Gerektiği kadar güçlü model.** Bir iş alt kademede güvenle yapılabiliyorsa üst kademe kullanılmaz.
- **Kalite riski varsa yükselt.** Örneğin dil jürisi Sonnet'te çeviri kokusunu kaçırabilir; bu yüzden Opus.
- **Paralel ve bağımsız.** İşveren jürileri birbirini görmez; aynı CV'yi aynı puan kartıyla ama farklı gözle okur.
- **Son söz ana ajanda.** Hiçbir alt ajan çıktısı doğrudan dosyaya yazılmaz; ana ajan doğrular ve uygular.

## Maliyet notu

Gerçek bir çalışmada sekiz işveren jürisi dört Sonnet ajanına ikişer persona olarak dağıtıldı. Her ajan yaklaşık 70–80 bin token kullandı ve 20–40 saniyede bitti. Tek bir Opus ajanının sekiz personayı sırayla oynaması hem daha yavaş hem daha pahalı olurdu ve personalar birbirinden etkilenirdi.
