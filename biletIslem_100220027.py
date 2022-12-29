# EREN DOĞAN - 100220027

from time import sleep


def bilet_olustur(t1, t2, y1, y2, adett, n, matris, kalan_koltuk):
    print("Rezerve Edilen Koltuklar (Sira-Koltuk): ")
    for i in range(t1, t2, 1):
        for j in range(y1, y2, 1):
            if matris[i][j] == 1:
                continue
            matris[i][j] = 1
            adett -= 1
            kalan_koltuk[n] -= 1
            sleep(0.2)
            print(i + 1, " - ", j + 1, ", ", end="", sep="")
            if adett == 0:
                print()
                return 0
        print()


def bilet_iptal(t1, t2, y1, y2, adett, n, matris, kalan_koltuk):
    print("İptal Edilen Koltuklar (Sira-Koltuk): ", end="")
    for i in range(t1, t2, 1):
        print()
        for j in range(y1, y2, 1):
            if matris[i][j] == 0:
                continue
            matris[i][j] = 0
            adett -= 1
            kalan_koltuk[n] += 1
            sleep(0.2)
            print(i + 1, " - ", j + 1, ", ", end="", sep="")
            if adett == 0:
                print()
                return 0


def bilet_iptal2(t1, t2, y1, y2, y3, y4, adett, n, matris, kalan_koltuk):
    print("İptal Edilen Koltuklar (Sira-Koltuk): ", end="")
    for i in range(t1, t2, 1):
        print()
        for j in range(y1, y2, -1):
            if matris[i][j] == 0:
                continue
            matris[i][j] = 0
            adett -= 1
            kalan_koltuk[n] += 1
            sleep(0.2)
            print(i + 1, " - ", j + 1, ", ", end="", sep="")
            if adett == 0:
                print()
                return

        for h in range(y3, y4, 1):
            if matris[i][h] == 0:
                continue
            matris[i][h] = 0
            adett -= 1
            kalan_koltuk[n] += 1
            sleep(0.2)
            print(i + 1, " - ", h + 1, ", ", end="", sep="")
            if adett == 0:
                print()
                return


def bilet_olustur2(t1, t2, y1, y2, y3, y4, adett, n, matris, kalan_koltuk):
    print("Rezerve Edilen Koltuklar (Sira-Koltuk): ")
    for i in range(t1, t2, 1):
        for j in range(y1, y2, -1):
            if matris[i][j] == 1:
                continue
            matris[i][j] = 1
            adett -= 1
            kalan_koltuk[n] -= 1
            sleep(0.2)
            print(i + 1, " - ", j + 1, ", ", end="", sep="")
            if adett == 0:
                print()
                return


        for h in range(y3, y4, 1):
            if matris[i][h] == 1:
                continue
            matris[i][h] = 1
            adett -= 1
            kalan_koltuk[n] -= 1
            sleep(0.2)
            print(i + 1, " - ", h + 1, ", ", end="", sep="")
            if adett == 0:
                print()
                return
        print()
