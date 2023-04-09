# girilen 2 basamaklı sayıyı yazıya çevirme
birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(number):
    birinci = number % 10
    ikinci = number // 10
    
    return "Girdiğiniz sayı: " + onlar[ikinci] + " " + birler[birinci]


# Girilen iki sayının Ebob'unu bulma
def ebob_bulma(sayı1,sayı2):
    
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):      

        if ( not (sayı1 % i) and not (sayı2 % i)):    #  " if sayı1 % i == 0 and sayı2 % i == 0: "  olur
            ebob = i 
        i += 1
    return ebob


def ebob2(sayı1,sayı2):
    
    sayının_ebobu = ebob_bulma(sayı1, sayı2)
    ekok = (sayı1*sayı2)//sayının_ebobu
    return ekok





# Girilen iki sayının Ekok'unu bulma
def ekok_bulma(sayı1,sayı2):
    
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i ==  0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    
    return ekok



            
