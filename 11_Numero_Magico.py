numero_magico = 7
n_user = 0
i = 1
print ('Indovina il Numero Magico')
print ('Ti diam un Indizio: Il Numero Magico è Minore o Uguale a 10')
while i <= 10:
        i = i+1
        n_user = int(input('Inserisci il Tuono Numero: '))
        if(n_user == numero_magico):
                i = 11
                output = 'Complimenti!!! Hai Indovinato il Numero Magico.'
        else:
                output = 'Game Over! Mi Dispiace non hai Indovinato il Numero Magico'
print(output)