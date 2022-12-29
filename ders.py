"""
def faktoriyel(n):
  if n == 0:
    return 1
  else:
    return n * faktoriyel(n-1)

print(faktoriyel(5))
"""
import datetime

"""
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

print(fib(5))
"""
"""
def ikili_arama(dizi, sol, sag, x):
  if sag >= sol:
    orta = sol + (sag - sol) // 2
    if dizi[orta] == x:
      return orta
    elif dizi[orta] > x:
      return ikili_arama(dizi, sol, orta - 1, x)
    else:
      return ikili_arama(dizi, orta + 1, sag, x)
  else:
    return -1
dizi = [10,9,25,35,21,56,83,100,5,2,8]
x = 21

sonuc = ikili_arama(dizi, 0, len(dizi) - 1, x)

if sonuc != -1:
  print("eleman",sonuc,". sırada bulunmaktadır")
else:
  print("elaman bulunamadı")
  

"""
#Eren DOĞAN - 100222027
def minimum_bul(dizi):
  if len(dizi) == 1:
    return dizi[0]
  else:
    if dizi[0] < dizi[1]:
      return minimum_bul(dizi[1:])
    else:
      return dizi[0]

def sel_siralama(dizi):
    print(dizi)
    if len(dizi) == 1:
        return dizi
    else:
        min_sayi = minimum_bul(dizi)
        min_index = dizi.index(min_sayi)
        tmp = dizi[0]
        dizi[0] = dizi[min_index]
        dizi[min_index] = tmp
        return [dizi[0]] + sel_siralama(dizi[1:])

dizi = [10, 9, 25, 35, 21, 56, 83, 100, 5, 2, 8]
result = sel_siralama(dizi)
print(result)

"""
min_index = 100
        for i in range(0, len(dizi), 1):
            if i == 0 or dizi[min_index] > dizi[i]:
                min_index = i
"""