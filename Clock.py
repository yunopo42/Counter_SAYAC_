import time

def sayac(zaman):
    while zaman >= 0:
        dk , sn = divmod(zaman,60)
        print("{} : {}".format(dk,sn))
        time.sleep(1)
        zaman-=1
    print("süre bitti")

kullanici_input = int(input("zaman giriniz : "))
sayac(kullanici_input)