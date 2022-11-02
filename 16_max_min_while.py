max = float('-inf')
min = float('inf')
n_ins = 0
while True:
    n_ins = int(input('Inserisci un numero: '))
    if n_ins == 0:
        break
    if(n_ins >= max):
        max = n_ins
    if(n_ins <= min):
        min = n_ins
print('Il maggiore è: ' , max)
print('Il minore è: ' , min)