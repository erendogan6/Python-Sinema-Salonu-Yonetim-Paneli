# EREN DOĞAN - 100220027

# Programın Çalışabilmesi İçin Gerekli Kütüphanelerin Kurulması Gerekmektedir.

import datetime
import biletIslem_100220027
from datetime import date
from fpdf import FPDF
from time import sleep
import random
import webbrowser
from pyfiglet import Figlet


class Salon:
    def __init__(self):
        self.salon_olustur()
        self.imdb_oku()
        self.dosya_oku()

    def imdb_oku(self):
        try:
            self.imdb = open("imdb_100220027.txt", "r")
        except:
            print("Film Bilgileri Okunamadı Program Kapatılıyor !")
            exit(0)
        self.rnd = random.randint(0, 251)
        self.liste = self.imdb.readlines()
        self.film = self.liste[self.rnd]

    def dosya_oku(self):
        try:
            self.dosya = open("indirim.txt", "r")
        except:
            print("İndirim Bilgileri Okunamadı Program Kapatılıyor !")
            exit(0)
        self.liste = []
        self.liste += self.dosya.read().split()
        for i in self.liste:
            i = i.strip()
        self.ucretler = []
        self.indirim = [0] * 12
        for i in range(12):
            self.indirim[i] = [0] * 3
        for i in range(0, len(self.liste), 1):
            if i == 0:
                carpan = 1
                self.maxBilet = 0
                for h in range(len(self.liste[i]) - 1, 1, -1):
                    self.maxBilet += int(self.liste[i][h]) * carpan
                    carpan *= 10
            elif 1 <= i <= 4:
                carpan = 1
                sayi = 0
                for h in range(len(self.liste[i]) - 1, 1, -1):
                    sayi += carpan * int(self.liste[i][h])
                    carpan *= 10
                self.ucretler.append(sayi)
            elif 5 <= i <= 16:
                self.indirim[i - 5][0] = int(self.liste[i][2]) * 10 + int(self.liste[i][3])
                if self.liste[i][5] == 'M':
                    self.indirim[i - 5][1] = 100
                else:
                    self.indirim[i - 5][1] = int(self.liste[i][5]) * 10 + int(self.liste[i][6])
                try:
                    self.indirim[i - 5][2] = int(self.liste[i][8]) * 10 + int(self.liste[i][9])
                except:
                    self.indirim[i - 5][2] = int(self.liste[i][7]) * 10 + int(self.liste[i][8])
        return

    def salon_yazdir(self):
        time = datetime.datetime.now()
        tarih = str(date.today())
        saat = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second) + "\n"
        print("\nVizyondaki Film:", self.film, end="")
        print("Tarih - Saat:", tarih, saat, end="")
        print("  ", end="")
        sleep(1)
        for i in range(20):
            if i < 9:
                print("0", end="")
            print(i + 1, "", end="")
        for i in range(20):
            print()
            sleep(0.2)
            for j in range(20):
                if j <= 0:
                    if i < 9:
                        print("0", end="")
                    print(i + 1, end="")
                if self.matris[i][j] == 0:
                    print(" - ", end="")
                else:
                    print(" X ", end="")
        print()
        sleep(1)

    def salon_olustur(self):
        self.ciro = [0, 0, 0, 0]
        self.kalan_koltuk = [100, 100, 100, 100]
        self.matris = [0] * 20
        for i in range(20):
            self.matris[i] = [0] * 20

    def adet_al(self):
        try:
            print("Adet Giriniz(0-", self.maxBilet, ")\n", end="", sep="")
            tmp = int(input())
            if tmp < 0:
                print("Adet Sayısı 1'den Küçük Olamaz !")
                sleep(0.5)
                tmp = 0
            if tmp > self.maxBilet:
                print("Adet Sayısı ", self.maxBilet, " Sayısından daha fazla olamaz !")
                tmp = 0
                return
        except:
            print("Adet Sayısını Yanlış Girdiniz")
            sleep(0.5)
            tmp = 0
        return tmp

    def yetersiz_koltuk(self, adett, n):
        if adett > self.kalan_koltuk[n]:
            print("Yeterli Koltuk Yok. Rezervasyon İşlemi Red Edildi!")
            sleep(0.5)
            return True

    def fiyat_hesapla(self, n, l1, l2, adett):
        sleep(0.7)
        for i in range(l1, l2, 1):
            if self.indirim[i][0] <= adett <= self.indirim[i][1]:
                fiyatt = self.ucretler[n] * adett - (self.ucretler[n] * adett) / 100 * self.indirim[i][2]
                print("\nBilet Adeti:", adett,
                      "\nBilet Tutarı: ", self.ucretler[n],
                      "\nToplam Tutar:", self.ucretler[n] * adett,
                      "\nYapılan İndirim:", (self.ucretler[n] * adett) / 100 * self.indirim[i][2],
                      "\nNet Tutar:", fiyatt)
                sleep(1.4)
                self.ciro[n] += fiyatt
                return
        print("İndirim Kampanyasından Faydalanamıyorsunuz.", end="1")
        fiyatt = self.ucretler[n] * adett
        print("\nBilet Adeti:", adett,
              "\nBilet Tutarı: ", self.ucretler[n],
              "\nNet Tutar:", fiyatt)
        sleep(1.4)
        self.ciro[n] += fiyatt
        print()
        return

    def iptal_fiyat(self, n, adett):
        fiyatt = (self.ucretler[n] * adett) / 2
        print("\nBilet İade Tutarı, Normal Bilet Ücretinin Yarısı Kadardır !"
              "\nBilet Adeti:", adett,
              "\nToplam Tutar:", self.ucretler[n] * adett,
              "\nİade Tutarı:", fiyatt)
        self.ciro[n] -= fiyatt
        sleep(0.5)
        return

    def ciro_hesapla(self):
        toplam = 0
        print()
        for i in range(0, len(self.ciro), 1):
            print("Kategori", i + 1, "Cirosu:", self.ciro[i])
            toplam += self.ciro[i]
            sleep(1)
        print("Toplam Ciro", toplam)
        sleep(1)

    def pdf_aktar(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=12)
        time = datetime.datetime.now()
        tarih = str(date.today())
        saat = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second) + "\n"
        tmp = "Tarih - Zaman: " + tarih + " " + saat
        pdf.write(5, tmp)
        tmp = "\nVizyondaki Film:" + str(self.film)
        pdf.write(6, tmp)
        pdf.cell(w=150, h=10, txt="SALON BILGILERI", border=1, ln=1, align='C')
        pdf.write(5, "\n    ")
        for i in range(20):
            if i < 9:
                pdf.write(5, "0")
            tmp = str(i + 1) + " "
            pdf.write(5, tmp)
        for i in range(20):
            pdf.write(5, "\n")
            for j in range(20):
                if j == 0:
                    if i < 9:
                        pdf.write(5, "0")
                    tmp = str(i + 1) + " "
                    pdf.write(5, tmp)
                if self.matris[i][j] == 0:
                    pdf.write(5, " - ")
                else:
                    pdf.write(5, " x ")
        pdf.write(10, "\n")
        toplam = 0
        pdf.cell(w=150, h=10, txt="CIRO BILGILERI", border=1, ln=1, align='C')
        for i in range(0, len(self.ciro), 1):
            tmp = "\nKategori " + str(i + 1) + " Cirosu:" + str(self.ciro[i])
            pdf.write(5, tmp)
            toplam += self.ciro[i]
        tmp = "\nToplam Ciro: " + str(toplam)
        pdf.write(7, tmp)
        pdf.output("Cikti.pdf")
        webbrowser.open_new('Cikti.pdf')

    def menu(self):
        self.secim = 1
        while self.secim != 0:
            print("**************")
            print("** ANA MENÜ **")
            print("**************")
            print("1. Rezervasyon Oluştur")
            print("2. Salonu Yazdır")
            print("3. Yeni Etkinlik Oluştur")
            print("4. Ciro Hesapla")
            print("5. Bilgileri PDF'e Aktar")
            print("6. Rezervasyon İptal Et")
            print("0. Çıkış")
            print("**************")
            print("\nİşlem Seçiminiz: ", end="")
            try:
                self.secim = int(input())
            except:
                self.secim = -1
            if self.secim == 1:
                self.kategori = 5
                while self.kategori != 0:
                    try:
                        self.kategori = int(input("Kategori Seçiminiz (1-4): "))
                    except:
                        pass
                    if self.kategori == 1:
                        self.adet = self.adet_al()
                        if self.adet == 0:
                            print("Ana Menüye Dönülüyor")
                            self.kategori = 0
                            break
                        if self.yetersiz_koltuk(self.adet, 0):
                            self.kategori = 0
                            break
                        biletIslem_100220027.bilet_olustur(0, 10, 5, 15, self.adet, 0, self.matris, self.kalan_koltuk)
                        self.fiyat_hesapla(0, 0, 3, self.adet)
                        self.kategori = 0
                        break
                    elif self.kategori == 2:
                        self.adet = self.adet_al()
                        if self.adet == 0:
                            print("Ana Menüye Dönülüyor")
                            self.kategori = 0
                            break
                        if self.yetersiz_koltuk(self.adet, 1):
                            self.kategori = 0
                            break
                        biletIslem_100220027.bilet_olustur2(0, 10, 4, -1, 15, 20, self.adet, 1, self.matris,
                                                            self.kalan_koltuk)
                        self.fiyat_hesapla(1, 3, 6, self.adet)
                        self.kategori = 0
                        break
                    elif self.kategori == 3:
                        self.adet = self.adet_al()
                        if self.adet == 0:
                            print("Ana Menüye Dönülüyor")
                            self.kategori = 0
                            break
                        if self.yetersiz_koltuk(self.adet, 2):
                            self.kategori = 0
                            break
                        biletIslem_100220027.bilet_olustur(10, 20, 5, 15, self.adet, 2, self.matris, self.kalan_koltuk)
                        self.fiyat_hesapla(2, 6, 9, self.adet)
                        self.kategori = 0
                        break
                    elif self.kategori == 4:
                        self.adet = self.adet_al()
                        if self.adet == 0:
                            print("Ana Menüye Dönülüyor")
                            self.kategori = 0
                            break
                        if self.yetersiz_koltuk(self.adet, 3):
                            self.kategori = 0
                            break
                        biletIslem_100220027.bilet_olustur2(10, 20, 4, -1, 15, 20, self.adet, 3, self.matris,
                                                            self.kalan_koltuk)
                        self.fiyat_hesapla(3, 9, 12, self.adet)
                        self.kategori = 0
                        break
                    elif self.kategori == 0:
                        break
                    else:
                        print("Yanlış Kategori Girdiniz")
                        sleep(1)
                if self.kategori == 0:
                    continue
            elif self.secim == 2:
                self.salon_yazdir()
                continue

            elif self.secim == 3:
                self.salon_olustur()
                self.imdb_oku()
                self.dosya_oku()
                self.salon_yazdir()
                continue

            elif self.secim == 4:
                self.ciro_hesapla()

            elif self.secim == 5:
                self.pdf_aktar()

            elif self.secim == 6:
                self.kategori = 5
                while self.kategori != 0:
                    try:
                        self.kategori = int(input("Kategori Seçiminiz (1-4): "))
                    except:
                        pass
                    if self.kategori == 1:
                        self.adet = self.adet_al()
                        if self.adet == 0:
                            print("Ana Menüye Dönülüyor")
                            self.kategori = 0
                            break
                        if self.adet > (100 - self.kalan_koltuk[0]):
                            print("İptal Etmeye Çalıştığınız Bilet Sayısı, Mevcut Bilet Sayısından Daha Fazladır !")
                            kategori = 0
                            break
                        biletIslem_100220027.bilet_iptal(0, 10, 5, 15, self.adet, 0, self.matris, self.kalan_koltuk)
                        self.iptal_fiyat(0, self.adet)
                        self.kategori = 0
                        break
                    if self.kategori == 2:
                        self.adet = self.adet_al()
                        if self.adet == 0:
                            print("Ana Menüye Dönülüyor")
                            self.kategori = 0
                            break
                        if self.adet > (100 - self.kalan_koltuk[1]):
                            print("İptal Etmeye Çalıştığınız Bilet Sayısı, Mevcut Bilet Sayısından Daha Fazladır !")
                            self.kategori = 0
                            break
                        biletIslem_100220027.bilet_iptal2(0, 10, 4, -1, 15, 20, self.adet, 1, self.matris,
                                                          self.kalan_koltuk)
                        self.iptal_fiyat(1, self.adet)
                        self.kategori = 0
                        break
                    if self.kategori == 3:
                        self.adet = self.adet_al()
                        if self.adet == 0:
                            print("Ana Menüye Dönülüyor")
                            self.kategori = 0
                            break
                        if self.adet > (100 - self.kalan_koltuk[2]):
                            print("İptal Etmeye Çalıştığınız Bilet Sayısı, Mevcut Bilet Sayısından Daha Fazladır !")
                            kategori = 0
                            break
                        biletIslem_100220027.bilet_iptal(10, 20, 5, 15, self.adet, 2, self.matris,
                                                         self.kalan_koltuk)
                        self.iptal_fiyat(2, self.adet)
                        self.kategori = 0
                        break
                    if self.kategori == 4:
                        self.adet = self.adet_al()
                        if self.adet == 0:
                            print("Ana Menüye Dönülüyor")
                            self.kategori = 0
                            break
                        if self.adet > (100 - self.kalan_koltuk[3]):
                            print("İptal Etmeye Çalıştığınız Bilet Sayısı, Mevcut Bilet Sayısından Daha Fazladır !")
                            self.kategori = 0
                            break
                        biletIslem_100220027.bilet_iptal2(10, 20, 4, -1, 15, 20, self.adet, 3, self.matris,
                                                          self.kalan_koltuk)
                        self.iptal_fiyat(3, self.adet)
                        self.kategori = 0
                        break
                    if self.kategori == 0:
                        break
                    else:
                        print("Yanlış Kategori Girdiniz")
                if self.kategori == 0:
                    continue
            elif self.secim == 0:
                print("Hoşçakalın. Program Kapanıyor")
                break
            else:
                print("Yanlış Seçim Girdiniz")
                sleep(1)


def kapak_yazdir():
    f = Figlet(font='slant')
    print(f.renderText('Eren Sinema'), end="")
    sleep(1)


def muzik_cal():
    webbrowser.open('piyano_100220027.mp3')

s1 = Salon()
kapak_yazdir()
muzik_cal()

s1.menu()
