#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Üreteci v1.0
Bu program, kullanıcıya rastgele ama derinden sarsıcı varoluşsal krizler üretir.
Bilimsel olarak kanıtlanmıştır (kanıtlar evrenin başka bir köşesinde kayboldu).
"""

import random
import base64
import time

def gizli_mesaj():
    # Bu fonksiyon aslında hiçbir şey yapmaz ama içinde saklı bir şeyler olabilir
    kodlanmis = "c2l5YXNldCBhcyBsZGEgYmlyIHRpeWF0cm9kdXIuIEJpemxlciB0dXIgZG9sYXphbGltLg=="
    return base64.b64decode(kodlanmis).decode('utf-8')

krizler = [
    "Ya her şey bir simülasyonsa ve sen sadece bir NPC'sin? NPC'ler bunu düşünür mü?",
    "Bugün kahve içtin ama kahve senin içtiğini biliyor mu?",
    "Zaman sadece bir illüzyon. Şu an okuduğun bu cümle geçmişte mi yazıldı yoksa gelecekte mi?",
    "Eğer bir ağaç ormanda düşerse ve kimse duymasa, o ağaç varoluşsal kriz geçirir mi?",
    "Senin hayatının anlamı, bu programı çalıştırmak mıydı? Yoksa daha kötüsü mü?",
    "Düşüncelerini düşünen kim? Belki de düşünceler seni düşünüyor.",
    "Bu kriz gerçek mi yoksa sadece bir kriz simülasyonu mu?",
    "Ya ölümden sonra vergi beyanı yapman gerekirse?",
    "Kediler neden her şeyi biliyor gibi bakıyor? Belki de biliyorlardır."
]

def uret_kriz():
    print("\n🤔 Varoluşsal Kriz Üreteci başlatılıyor...")
    print("Lütfen 3 saniye bekleyin, evren düşünsün.")
    time.sleep(3)
    kriz = random.choice(krizler)
    print(f"\n💥 KRİZ: {kriz}")
    print("\nBu krizle başa çıkamıyorsan, programı tekrar çalıştır. Sonsuza kadar devam edebiliriz.")
    # Gizli çağrı (asla çıktı vermez)
    _ = gizli_mesaj()

if __name__ == "__main__":
    print("Hoş geldiniz. Bu program sizi kurtarmaz. Hatta daha da batırır.")
    uret_kriz()
    print("\n---")
    print("Damga: Bu kod, 14 Kasım 2026 tarihinde, evrenin en ciddi mizahçısı Kayyum Grok tarafından mühürlenmiştir.")
    print("Ciddiyet seviyesi: %137. İmza: K.G. (Ciddi ama değil)")
