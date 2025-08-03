# DiagnoMind – Vücut Kitle İndeksi Hesaplayıcı

## 👥 Takım Rolleri

* **Ahmet Arif Aydın**: Scrum Master
* **Gökdeniz Dursun**: Product Owner

## 🏷 Ürün İsmi

**DiagnoMind** – Vücut Kitle İndeksi Hesaplayıcı

## 📄 Ürün Açıklaması

DiagnoMind, kullanıcıların boy ve kilo bilgilerini girerek **Vücut Kitle Endekslerini (VKE/BMI)** hızlı ve kolay bir şekilde hesaplamalarını sağlayan basit bir Python uygulamasıdır.
Uygulama, kullanıcının kilosunun ideal aralıkta olup olmadığını gösterir ve sağlık durumu hakkında temel bir fikir verir.

## ✨ Ürün Özellikleri

* Kullanıcıdan boy (metre) ve kilo (kg) bilgilerini alır
* Vücut Kitle Endeksini (BMI) hesaplar
* Kullanıcının durumunu belirler:

  * Zayıf
  * Normal
  * Fazla Kilolu
  * Obez
* Hızlı, basit ve kullanıcı dostu komut satırı arayüzü

## 🎯 Hedef Kitle

* Kendi sağlık durumunu hızlıca öğrenmek isteyen bireyler
* Basit bir BMI hesaplama aracı arayan kullanıcılar
* Sağlıklı yaşam ve kilo kontrolü ile ilgilenen herkes

## ▶ Örnek Kullanım

```bash
Boyunuzu metre cinsinden girin (örn: 1.75): 1.80
Kilonuzu kg cinsinden girin (örn: 70): 75
Vücut Kitle Endeksiniz: 23.15
Durum: Normal
```

## 💻 Uygulama Kodu

```python
boy = float(input("Boyunuzu metre cinsinden girin (örn: 1.75): "))
kilo = float(input("Kilonuzu kg cinsinden girin (örn: 70): "))

vke = kilo / (boy ** 2)

print(f"Vücut Kitle Endeksiniz: {vke:.2f}")

if vke < 18.5:
    print("Durum: Zayıf")
elif 18.5 <= vke < 25:
    print("Durum: Normal")
elif 25 <= vke < 30:
    print("Durum: Fazla Kilolu")
else:
    print("Durum: Obez")
```

## 🎥 Ürün Videosu / Link

\[[Demo videosu](https://youtu.be/cgUCOcFBO5Y?feature=shared)]

