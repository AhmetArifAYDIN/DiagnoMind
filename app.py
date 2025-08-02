# Vücut Kitle Endeksi Hesaplayıcı

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
