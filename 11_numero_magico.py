numero_magico = 7
numero_inserito = 0
output = "Game Over!"
i = 0
numero_inserito = int(input("Prova ad indovinare il numero magico: "))
while i < 10:    
    if(numero_inserito == numero_magico):
        output = "Complimenti, hai indovinato!"        
        break
    else:
        numero_inserito = int(input("hai sbagliato, riprova: "))        
    i = i + 1
print(output)