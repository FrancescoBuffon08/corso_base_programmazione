n_vocali=0
i=0
frase=0
c=0
l=0
frase=str(input('Inserisci una frase: '))
c=len(frase)
while(i<c):
    l=frase[i]
    if(l=='a' or l=='e' or l=='i' or l=='o' or l=='u'):
        n_vocali=n_vocali+1
    i=i+1
print(n_vocali)