def divinRec(a, b):
    if a < b:
        return 0
    else:
        return 1 + divinRec(a - b, a)
    

#2
#a) l'orsque la valuer de b est egale à 0
    
def fonction(a, b, count=0):
    if b == 0:
        return a, count
    else:
        count += 1
        return fonction(a * 10, b - 1, count)

# Si a=2 et b=3
valeurReel, nombre_appels = fonction(2,3)
print("Nombre d'appels récursifs :", nombre_appels)
'''
Appel 1: a=2, b=3
Appel 2: a=20, b=2
Appel 3: a=200, b=1
'''


