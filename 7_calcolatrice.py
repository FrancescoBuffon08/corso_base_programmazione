n1=0
n2=0
operazione=0
risultato=0
n1=int(input('Inserisci il Primo Numero:'))
n2=int(input('Inserisci il Secondo Numero:'))
operazone=int(input('Inserisci il Numero Equivalente alla Operazione che Vuoi Eseguire: somma (1), sottrazione (2), divisione (3), moltiplicazione (4).'))
if(operazione==1):
    risultato=(n1+n2)
if (operazione==2):
    risultato=(n1-n2)
if (operazione==3):
    if (n2>0):
        risultato=(n1/n2)
    else:
        risulato='Non Puoi Dividere un Numero per 0'
if (operazione==4):
    risultato=(n1*n2)
print (risultato)
