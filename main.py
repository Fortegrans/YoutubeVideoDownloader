from pytubefix import YouTube

url = input("enter youtube URL: ")

print("Video bilgileri alınıyor...")

# client='ANDROID' ekleyerek YouTube'un mobil yayınlarına erişiyoruz
#neden mobil? çünkü youtube videoları pc de seperateliyor yani ses ve video olarak ayırıyor  ama telefonda bir veriyor
yt = YouTube(url, client='ANDROID')

# En yüksek kaliteli tek parça videoyu alıyoruz
ys = yt.streams.get_highest_resolution()

if ys:
    print(f"İndiriliyor: {yt.title}")
    ys.download()
    print("İndirme başarıyla tamamlandı!")
else:
    print("Uygun akış bulunamadı, alternatif aranıyor...")
    # Progressive bulunamazsa mevcut ilk mp4 akışını indirir
    yt.streams.filter(file_extension='mp4').first().download()
    print("İndirme tamamlandı!")