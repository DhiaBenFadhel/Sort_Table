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

def calcul_pas(n):
    pas=1
    while (pas*3+1)<n:
        pas=pas*3+1
    return pas

def Trishell(t,n):
   pas=calcul_pas(n)
   while not(pas<1):
    for i in range(pas,n):
        tmp=t[i]
        j=i
        while(j-pas>-1) and(t[j-pas]>tmp):
            t[j]=t[j-pas]
            j=j-pas 
        t[j]=tmp
    pas=pas//3
        

n=saisie()
t=array([int]*n)
remplir(t,n)
Trishell(t,n)
print("Ici votre tableau trieé :")
affichage(t,n)


