def somma(x, y):
	risultato = numero_1 + numero_2
	return risultato
def differenza(x, y):
	risultato = numero_1 - numero_2
	return risultato
def moltiplicazione(x, y):
	risultato = numero_1 + numero_2
	return risultato
def divisione(x, y):
	risultato = numero_1 + numero_2
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
    if(numero_2>0):
        if(y_n=='yes'):
            print(operazione(numero_1, numero_2))
        else:
            print('fine')
    else:
        print('fine')
    vuoi_fare_altri_conti=str(input('Vuoi fare altri calcoli? Yes or No: '))
    if(vuoi_fare_altri_conti=='yes'):
          continue
    else:
          break
