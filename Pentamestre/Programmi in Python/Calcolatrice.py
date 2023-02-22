def somma(x, y):
	risultato = numero_1 + numero_2
	return risultato
def differenza(x, y):
	risultato = numero_1 - numero_2
	return risultato
def moltiplicazione(x, y):
	risultato = numero_1 * numero_2
	return risultato
def divisione(x, y):
	risultato = numero_1 / numero_2
	return risultato
operazione:str
numero_1=0
numero_2=0
y_n:str
vuoi_fare_altri_conti:str
while True:
    operazione=str(input("Inserisci l'operazione che vuoi fare: "))
    numero_1=int(input('Inserisci il primo numero: '))
    numero_2=int(input('Inserisci il secondo numero che sia maggiore di 0: '))
    y_n=str(input('Vuoi continuare? Yes or No: '))
    if(y_n=='yes'):
        if(operazione=='somma'):
            print(somma(numero_1, numero_2))
        if(operazione=='differenza'):
            print(differenza(numero_1, numero_2))
        if(operazione=='moltiplicazione'):
            print(moltiplicazione(numero_1, numero_2))
        if(operazione=='divisione'):
            if(numero_2>0):
                print(divisione(numero_1, numero_2))
            else:
                print('non puoi dividere per 0!')
    else:
        print('fine')
    vuoi_fare_altri_conti=str(input('Vuoi fare altri calcoli? Yes or No: '))
    if(vuoi_fare_altri_conti=='yes'):
          continue
    else:
          break