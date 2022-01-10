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
        print(t[i],end=" | ")

def TriInsertion(t,n):
    for i in range(n):
        x=t[i]
        j=i
        while(t[j-1]>x)and(j>0):
            t[j]=t[j-1]
            j=j-1
        t[j]=x

n=saisie()
t=array([int]*n)
remplir(t,n)
print("Ici votre tableau non trieé :")
affichage(t,n)
TriInsertion(t,n)
print("\n"+"Ici votre tableau trieé :")
affichage(t,n)


