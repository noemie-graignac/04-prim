""" Ce fichier sert à afficher le nombre s'il est premier"""
# from math import sqrt

#### Fonction secondaire
def isprime(p):
    """On cherche à savoir si le nombre est premier"""

    if p < 2:
        return False

    for d in range(2,p):
        if p%d==0:
            return False
    # votre code ici

    return True


#### Fonction principale

def main():
    """on affiche le nombre premier n"""

    # vos appels à la fonction secondaire ici
    isprime(14)
    isprime(3)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
