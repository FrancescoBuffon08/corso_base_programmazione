n=0
i=0
s=0
l=0
c=0
while True:
    n=str(input('Inserisci delle cifre: '))
    if(str.isdigit (n)):
        break
c=len(n)
while (i<c):
    l=n[i]
    i=i+1
    s=l
print (s)