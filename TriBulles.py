from numpy import*
def saisie():
    n=int(input("Entrez la taille de tableau: ")) 
    while not(n>1):
        n=int(input("Entrez la taille de tableau: "))  
    return n

def remplir(t,n):
    for i in range(n):
        t[i] =int(input("Entrez un entier: "))

def affichage(t,n):
    for i in range(n):
        print(t[i],end=" ")

def Tribulles(t,n):
    echange=False
    while not((echange==True) or (n==1)):
        for i in range(n-1):
            if t[i]>t[i+1]:
                x=t[i]
                t[i]=t[i+1]
                t[i+1]=x
        n-=1


n=saisie()
t=array([int]*n)
remplir(t,n)
Tribulles(t,n)
print("Ici votre tableau trieé :")
affichage(t,n)


