import time

def sayac(zaman):
    while zaman >= 0:
        dk , sn = divmod(zaman,60)
        #divmod sayısal bir değeri 60 a bölerek kalan hesabı yapan bir kod(dakika ve saniye hesabı yaparken kullandım)(
        print("{} : {}".format(dk,sn))
        time.sleep(1)
        zaman-=1
    print("süre bitti")

kullanici_input = int(input("zaman giriniz : "))
sayac(kullanici_input)
