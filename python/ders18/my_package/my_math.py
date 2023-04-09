def find_fact(x):
    """Girilen sayinin factoriyelini dondurur.""" 
    çarpım_değeri = 1
    for i in range(x,0,-1):
        çarpım_değeri *= i
    return çarpım_değeri


def find_hypo(x,y):
    return (x ** 2 + y ** 2) ** 0.5

pi = 3.14

e = 2.7182

