# In questo programma ho voluto ricreare il gioco televisivo ‘Reazione a Catena’, condotto da Marco Liorni. In questo gioco ci sono due squadre composte ciascuna da 3 persone. Esse hanno un capitano e un nome della squadra. Il gioco si suddivide in tre giochi, in cui partecipano entrambe le squadre, e due, in cui partecipa solo la squadra con il monte premi più alto. Nel programma la prima squadra ad iniziare è quella che ha gareggiato, arrivando in finale, la sera precedente. Non potendo scegliere la squadra che ha già gareggiato, ho scelto di chiedere le età dei capitani e far iniziare la squadra con il capitano più anziano.
import random  
saldo_squadra_1=0 
saldo_squadra_2=0 
numero_prove=0 
numero_canzone_precedente=0
numero_parola_precedente=0
numero_2=0
numero_3=0
variabile_scambio_squadre:str
variavile_scambio_saldo=0
#liste necessarie
lista_parole=['ciao', 'cane', 'gatto','topo','penna','matita','computer','telefono','quaderno','carta','pasta','pizza','bello','lampada','alfabeto','vocali'] 
lista_indizi=['saluto','animale','animale','roditore','scrittura','grafite','informatica','chiamate','carta','alberi','alimento che si cuoce in acqua','alimento con pomodoro e mozzarella', 'aggettivo','fa luce','lettere','no consonanti'] 
lista_parole_2=['c--o','c--e','g---o','t--o','p---a','m----a','c------r','t------o','q------o','c---a','p---a','p---a','b---o','l-----a','a------o','v----i'] 
lista_testo_canzoni=['non volano farfalle, non stò più nella pelle...',"gloria, manchi tu nell'aria, chiesa di campania...","fatti mandare dalla mamma, a prendere il latte...","Un bicchiere di vino, con un panino...",'Camminerò ad un passo da te e fermeremo il vento...','La vita senza amore dimmi tu che vita è, oh dove sei andata...','Ma quanto è bello andare il giro con le ali sotto i piedi...','Perfavore non piangere e non ci rimanere male che noi due ci conosciamo bene...',"Ho guardato dentro un'emozione e ci ho visto tanto amore e ho capito perchè non si comanda il cuore"] 
lista_indizi_canzoni=['San Givanni','Umberto Tozzi','Gianni Morandi','Albano Carrisi e Romina Power','Mr.Rain','Fedez','Lunapop','Pinguini Tattici Nucleari','Vasco Rossi'] 
lista_nome_canzoni=['farfalle','gloria','fatti mandare dalla mamma','felicità','supereroi','la dolce vita','vespa 50 special','pastello bianco','senza parole'] 
lista_terzo_gioco_risposte=['pollicino', 'gong', 'partecipazione', 'materasso' ]
lista_terzo_gioco_domande=['Al momento di tornare a casa; al bivio, seduto su un sasso; disperato insieme ai fratelli; perché gli uccellini hanno mangiato tutte le sue briciole.'," All'alba, prima della preghiera; nel tempio buddista; pronto alla bastonata; perché è così che si suona."," Due mesi prima dell’evento; tra bollette e volantini; molto raffinata; perché è l’invito ufficiale al matrimonio."," Quando nonna non si fidava di nessuno; in camera da letto; pieno di bitorzoli; perché lei ci nascondeva dentro i soldi."]
quarto_gioco_1='Amico'
quarto_gioco_2='i---------o'
quarto_gioco_3='c--------o'
quarto_gioco_4='a-------o'
quarto_gioco_5='l---o'
quarto_gioco_6='s--------a'
quarto_gioco_7='Strada'
risposta_2='immaginario'
risposta_3='collettivo'
risposta_4='artistico'
risposta_5='liceo'
risposta_6='secondaria'
ultimo_1=['Presidente','r---------','Italia']
ultimo_2=['Italia','v---','Voce']
ultimo_3=['Voce','f---','Interdentale']
ultimo_4=['Interdentale','s-----','Tempo']
ultimo_5=['Tempo','b------','Denti']
ultimo_6=['Denti','g-------','Esatto']
ultimo_1_risposta='repubblica'
ultimo_2_risposta='viva'
ultimo_3_risposta='filo'
ultimo_4_risposta='spazio'
ultimo_5_risposta='battere'
ultimo_6_risposta='giudizio'
fine_gioco=['Esatto','CO      O','???']
fine_gioco_indizio=['Esatto','CO      O','Visto']
fine_gioco_risposta='corretto'
i=0  
#inizio
print('Benvenuti a Reazione a Catena, in questo gioco si può giocare solo in 6 persone, vi dovrete dividere in due squadre e scegliere un nome! Per decidere, chi inizierà il gioco, scegliete un capitano e inserite la sua età, partirà la squadra che ha il capitano più anziano.')  
#domando i nomi delle squadre
nome_1=str(input('Inserisci il nome della prima squadra: '))  
nome_2=str(input('Inserisci il nome della seconda squadra: '))  
#domando l'età del capitano per poi scegliere chi inizierà
età_1=int(input("Inserisci l'età del capitano della prima squadra: "))  
età_2=int(input("Inserisci l'età del capitano della seconda squadra: "))  
#inizio primo gioco
print("Bene, iniziamo. Io sono Marco Liorni, il conduttore di Reazione a Catena. Il primo gioco è una sorta di impiccato solo che dovrete inserire non lettere ma parole, ad ogni parola sbagliata il turno passerà all'altra squadra. Se anche essa sbaglierà toccherà di nuovo alla squadra precedente ma avrà un indizio. Ogni parola azzeccata vale 2000 euro. Ci saranno quattro manche. Se indovinerete la parola il turno sarà ancora vostro. P.S. inserisci le parole con le lettere minuscole.")  
#controllo chi dovrà iniziare
if(età_1>età_2):  
    print('Inizieranno i/gli '+nome_1)  
    squadra_1=nome_1  
    squadra_2=nome_2  
else:  
    print('Inizieranno i/gli '+nome_2)  
    squadra_1=nome_2  
    squadra_2=nome_1 
while True: 
    while True:
        #decido in modo casuale la parola da domandare
        numero_parola:int=random.randrange(0,15) 
        parola=lista_parole[numero_parola] 
        parola_2:str=lista_parole_2[numero_parola] 
        indizio:str=lista_indizi[numero_parola] 
        i=0 
        #controllo che non sia già uscita
        if(numero_parola==numero_parola_precedente and numero_parola==numero_2 and numero_parola==numero_3):
            continue
        else:
            break
    while True:  
        #mostro la parola da indovinare
        print('La parola da trovare è: '+parola_2)  
        #mostro l'indizio se non è stata indovinata da entrambe le squadre
        if(i>=2):  
            print('Avrete un suggerimento, esso è: '+indizio)
        #chiedo la parola che secondo loro è giusta  
        prova=str(input('Inserisci la parola giusta: ')) 
        #controllo se è giusta 
        if(prova==parola):  
            break  
        else:  
            print('Mi spiace, hai sbagliato. Ora tocca alla squadra avversaria.')  
            i=i+1  
    print('Bravi, avete indovinato')  
    #controllo chi l'ha indovinata
    if(i%2==0):  
        #aggiorno i montepremi
        saldo_squadra_1=saldo_squadra_1+2000 
    else:  
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre
        saldo_squadra_2=saldo_squadra_2+2000 
        variabile_scambio_squadre=squadra_1
        squadra_1=squadra_2
        squadra_2=variabile_scambio_squadre
        variavile_scambio_saldo=saldo_squadra_1
        saldo_squadra_1=saldo_squadra_2
        saldo_squadra_2=variavile_scambio_saldo
    #mostro i monte premi
    print(squadra_1+' siete a: ')
    print(saldo_squadra_1) 
    print(squadra_2+' siete a: ')
    print(saldo_squadra_2) 
    #salvo le parale precedenti così da non richiedere le stesse
    numero_parola_precedente=numero_parola
    numero_2=numero_parola_precedente
    numero_3=numero_2
    #ontrollo il numero di manche effettuato
    if(numero_prove==3): 
        break 
    #aggiorno il numero di manche
    numero_prove=numero_prove+1 
#inizio secondo gioco
print("Perfetto, siamo giunti al seondo gioco, questo consisterà nel trovare il titolo della canzone dato il testo. Avrete come prima una possibilità a squadra senza indizi. Una volta provato entrambe le squadre senza ottenere risultati, apparirà come suggerimento l'autore della canzone. Ora inizierà la squadra che ha un monte premi più alto, nel caso sia pari inizierà la squadra con il capitano più anziano. Possiamo partire. P.S. inserisci le parole con le lettere minuscole.") 
#controllo chi debba iniziare
if(saldo_squadra_1==saldo_squadra_2): 
    if(età_1>età_2):  
        print('Inizieranno i/gli '+squadra_1)  
    else:  
        print('Inizieranno i/gli '+squadra_2)  
        variabile_scambio_squadre=squadra_1
        squadra_1=squadra_2
        squadra_2=variabile_scambio_squadre
        variavile_scambio_saldo=saldo_squadra_1
        saldo_squadra_1=saldo_squadra_2
        saldo_squadra_2=variavile_scambio_saldo
else: 
    if(saldo_squadra_1>saldo_squadra_2):  
        print('Inizieranno i/gli '+squadra_1)  
    else:  
        print('Inizieranno i/gli '+squadra_2)  
        variabile_scambio_squadre=squadra_1
        squadra_1=squadra_2
        squadra_2=variabile_scambio_squadre
        variavile_scambio_saldo=saldo_squadra_1
        saldo_squadra_1=saldo_squadra_2
        saldo_squadra_2=variavile_scambio_saldo
#inizializzo le variabili
prove=0
i=0
numero_prove=0
numero_canzone_precedente=0
numero_canzone_2=0
numero_canzone_3=0
while True: 
    while True:
        #decido in modo casuale la canzone da domandare
        numero_canzone:int=random.randrange(0,8) 
        canzone=lista_testo_canzoni[numero_canzone] 
        canzone_titolo:str=lista_nome_canzoni[numero_canzone] 
        indizio:str=lista_indizi_canzoni[numero_canzone] 
        i=0 
        #controllo che non sia già uscita
        if(numero_canzone==numero_canzone_precedente and numero_canzone==numero_canzone_2 and numero_canzone==numero_canzone_3):
            continue
        else:
            break
    while True:  
        #mostro la canzone da indovinare
        print('Il testo della canzone che bisogna trovare è: '+canzone)  
        #mostro l'indizio se non è stata indovinata da entrambe le squadre
        if(i>=2):  
            print('Avrete un suggerimento, esso è: '+indizio)  
        #chiedo la canzone che secondo loro è giusta 
        prova=str(input('Inserisci la parola giusta: '))  
        #controllo se è giusta
        if(prova==canzone_titolo):  
            break  
        else:  
            print('Mi spiace, hai sbagliato. Ora tocca alla squadra avversaria.')  
            i=i+1  
    print('Bravi, avete indovinato')  
    #controllo chi abbia indovinato
    if(i%2==0):  
        #aggiorno i monte premi
        saldo_squadra_1=saldo_squadra_1+6000 
    else:
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre  
        saldo_squadra_2=saldo_squadra_2+6000 
        variabile_scambio_squadre=squadra_1
        squadra_1=squadra_2
        squadra_2=variabile_scambio_squadre
        variavile_scambio_saldo=saldo_squadra_1
        saldo_squadra_1=saldo_squadra_2
        saldo_squadra_2=variavile_scambio_saldo
    #mostro i monte premi
    print(squadra_1+' siete a: ')
    print(saldo_squadra_1) 
    print(squadra_2+' siete a: ')
    print(saldo_squadra_2) 
    #salvo le parale precedenti così da non richiedere le stesse
    numero_canzone_precedente=numero_canzone
    numero_canzone_2=numero_canzone_precedente
    numero_canzone_3=numero_canzone_2
    #controllo il numero di manche
    if(numero_prove==2): 
        break 
    #aggiorno il numero di manche
    numero_prove=numero_prove+1 
if(saldo_squadra_1>saldo_squadra_2): 
    squadra_1=squadra_1
else: 
    variabile_scambio_squadre=squadra_1
    squadra_1=squadra_2
    squadra_2=variabile_scambio_squadre
    variavile_scambio_saldo=saldo_squadra_1
    saldo_squadra_1=saldo_squadra_2
    saldo_squadra_2=variavile_scambio_saldo
#inizio terzo gioco
print("Siamo arriati all'ultimo gioco in cui giocheranno entrambe le squadre. Dovrete trovare la parola che collega quelle date.")
#controllo chi debba iniziare
if(saldo_squadra_1>saldo_squadra_2):
    print('Inizieranno i/gli/le '+squadra_1)
else:
    print('Inizieranno i/gli/le '+saldo_squadra_2)
    variabile_scambio_squadre=squadra_1
    squadra_1=squadra_2
    squadra_2=variabile_scambio_squadre
    variavile_scambio_saldo=saldo_squadra_1
    saldo_squadra_1=saldo_squadra_2
    saldo_squadra_2=variavile_scambio_saldo
#mostro le domande
print(quarto_gioco_1)
print(quarto_gioco_2)
print(quarto_gioco_3)
print(quarto_gioco_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
#domando la risposta
prova_quarto_gioco=str(input(squadra_1+' Inserisci la tua parola: '))
#controllo se sia giusta
if(prova_quarto_gioco==risposta_2):
    #aggiorno i monte premi
    saldo_squadra_1=saldo_squadra_1+2000
    print('Bravi, avete indovinato')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
else:
    #aggiorno i monte premi
    saldo_squadra_2=saldo_squadra_2+2000
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre  
    variabile_scambio_squadre=squadra_1
    squadra_1=squadra_2
    squadra_2=variabile_scambio_squadre
    variavile_scambio_saldo=saldo_squadra_1
    saldo_squadra_1=saldo_squadra_2
    saldo_squadra_2=variavile_scambio_saldo
    print('Mi spiace, ora vedrete la risposta!')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
#mostro le domande con la risposta precedente
print(quarto_gioco_1)
print(risposta_2)
print(quarto_gioco_3)
print(quarto_gioco_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
#omando la risposta
prova_quarto_gioco=str(input(squadra_1+' Inserisci la tua parola: '))
#controllo se sia giusta
if(prova_quarto_gioco==risposta_3):
    #aggiorno i monte premi
    saldo_squadra_1=saldo_squadra_1+2000 
    squadra_1=squadra_1
    saldo_squadra_1=saldo_squadra_1
    squadra_2=squadra_2
    saldo_squadra_2=saldo_squadra_2
    print('Bravi, avete indovinato')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
else:
    #aggiorno il monte premi
    saldo_squadra_2=saldo_squadra_2+2000
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre  
    variabile_scambio_squadre=squadra_1
    squadra_1=squadra_2
    squadra_2=variabile_scambio_squadre
    variavile_scambio_saldo=saldo_squadra_1
    saldo_squadra_1=saldo_squadra_2
    saldo_squadra_2=variavile_scambio_saldo
    print('Mi spiace, ora vedrete la risposta!')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
#mostro le omande con la risposta precedente
print(quarto_gioco_1)
print(risposta_2)
print(risposta_3)
print(quarto_gioco_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
#domnado la risposta
prova_quarto_gioco=str(input(squadra_1+'Inserisci la tua parola: '))
#controllo se sia giusta
if(prova_quarto_gioco==risposta_4):
    #aggiorno il montepremi
    saldo_squadra_1=saldo_squadra_1+2000
    squadra_1=squadra_1
    saldo_squadra_1=saldo_squadra_1
    squadra_2=squadra_2
    saldo_squadra_2=saldo_squadra_2
    print('Bravi, avete indovinato')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
else:
    #aggiorno i monte premi
    saldo_squadra_2=saldo_squadra_2+2000
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre  
    variabile_scambio_squadre=squadra_1
    squadra_1=squadra_2
    squadra_2=variabile_scambio_squadre
    variavile_scambio_saldo=saldo_squadra_1
    saldo_squadra_1=saldo_squadra_2
    saldo_squadra_2=variavile_scambio_saldo
    print('Mi spiace, ora vedrete la risposta!')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
#mostro le domande e la risposta precedente
print(quarto_gioco_1)
print(risposta_2)
print(risposta_3)
print(risposta_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
#domando la risposta
prova_quarto_gioco=str(input(squadra_1+'Inserisci la tua parola: '))
#controllo che sia giusta
if(prova_quarto_gioco==risposta_5):
    #aggiorno i monte premi
    saldo_squadra_1=saldo_squadra_1+2000
    squadra_1=squadra_1
    saldo_squadra_1_8=saldo_squadra_1
    squadra_2=squadra_2
    saldo_squadra_2=saldo_squadra_2
    print('Bravi, avete indovinato')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
else:
    #aggiorno i monte premi
    saldo_squadra_2=saldo_squadra_2+2000
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre  
    variabile_scambio_squadre=squadra_1
    squadra_1=squadra_2
    squadra_2=variabile_scambio_squadre
    variavile_scambio_saldo=saldo_squadra_1
    saldo_squadra_1=saldo_squadra_2
    saldo_squadra_2=variavile_scambio_saldo
    print('Mi spiace, ora vedrete la risposta!')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
    #mostro le domande e la risposta precedente
print(quarto_gioco_1)
print(risposta_2)
print(risposta_3)
print(risposta_4)
print(risposta_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
#domando la risposta
prova_quarto_gioco=str(input(squadra_1+'Inserisci la tua parola: '))
#controllo che sia giusta
if(prova_quarto_gioco==risposta_6):
    #aggiorno i montepremi
    saldo_squadra_1=saldo_squadra_1+2000
    squadra_1=squadra_1
    saldo_squadra_1=saldo_squadra_1
    squadra_2=squadra_2
    saldo_squadra_2=saldo_squadra_2
    print('Bravi, avete indovinato')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
else:
    #aggiorno i monte premi
    saldo_squadra_2=saldo_squadra_2+2000
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre  
    variabile_scambio_squadre=squadra_1
    squadra_1=squadra_2
    squadra_2=variabile_scambio_squadre
    variavile_scambio_saldo=saldo_squadra_1
    saldo_squadra_1=saldo_squadra_2
    saldo_squadra_2=variavile_scambio_saldo
    print('Mi spiace, ora vedrete la risposta!')
    #mostro i monte premi
    print(squadra_1+' siete a:')
    print(saldo_squadra_1)
    print(squadra_2+' siete a:')
    print(saldo_squadra_2)
    #mostro le risposte
print(quarto_gioco_1)
print(risposta_2)
print(risposta_3)
print(risposta_4)
print(risposta_5)
print(risposta_6)
print(quarto_gioco_7)
#controllo chi è la squadra vincente
if(saldo_squadra_2>saldo_squadra_1):
    #stampo la squadra vincente
    print('Passano i/gli: '+squadra_2)
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre 
    squadra_finale=squadra_2
    saldo_finale=saldo_squadra_2
else:
    #stampo la squadra vincente
    print('Passano i/gli: '+squadra_2)
    #inverto le variabili SQUADRA_1 e _2 così che chi abbia indovinato ha ancora il turno
    #inverto le variabili SALDO_SQUADRA_1 e _2 in modo da mantenere i giusti monte premi alle dovute squadre 
    squadra_finale=squadra_1
    saldo_finale=saldo_squadra_1
    #inizio gioco finale
print("Siamo giunti all'ultimo gioco, dovrete trovare una parola che accumuna le parole date. Avete una sola possibilità. Se sbagliate il monte premi si dimezzerà.")
#mostro la domanda
print(ultimo_1)
#chiedo la risposta
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
#controllo che sia giusta 
if(prova_ultimo==ultimo_1_risposta):
    print('Hai indovinato')
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    #aggiorno il monte premi
    saldo_finale=saldo_finale/2
    #mostro la soluzione
    print(ultimo_1_risposta)
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
#mostro la domanda
print(ultimo_2)
#domando la rsposta
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
#controllo se sia esatta
if(prova_ultimo==ultimo_2_risposta):
    print('Hai indovinato')
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    #aggiorno il monte premi
    saldo_finale=saldo_finale/2
    #mostro la soluzione
    print(ultimo_2_risposta)
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
#mostro la domanda
print(ultimo_3)
#domando la ripsosta
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
#controllo che sia giusta
if(prova_ultimo==ultimo_3_risposta):
    print('Hai indovinato')
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    #aggiorno il monte premi
    saldo_finale=saldo_finale/2
    #mostro la risposta
    print(ultimo_3_risposta)
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
#mostro la domanda
print(ultimo_4)
#domando la risposta
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
#controllo che sia giusta
if(prova_ultimo==ultimo_4_risposta):
    print('Hai indovinato')
    #mostro il risultato
    print('Il vostro saldo è: '+saldo_finale)
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    #aggiorno il monte premi
    saldo_finale=saldo_finale/2
    #mostro la risposta
    print(ultimo_4_risposta)
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
#mostro la domnda
print(ultimo_5)
#domando la risposta
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
#controllo che sia giusta
if(prova_ultimo==ultimo_5_risposta):
    print('Hai indovinato')
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    #aggiorno il monte premi
    saldo_finale=saldo_finale/2
    #mostro la risposta
    print(ultimo_5_risposta)
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
#mostro la domanda  
print(ultimo_6)
##chiedo la risposta
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
#controllo che sia giusta
if(prova_ultimo==ultimo_6_risposta):
    print('Hai indovinato')
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    #aggiorno il monte premi
    saldo_finale=saldo_finale/2
    #mostro la risposta
    print(ultimo_6_risposta)
    #mostro il monte premi
    print('Il vostro saldo è: '+saldo_finale)
#gioco finale
print("Ora dovrete trovare l'ultima parola, avrete però solo una parola data. Potrete chiedere l'altra parola ma il monte premi si dimezzerà. Se volete comprare il terzo elemento, scrivete 'Aquisto'")
#mostro la domanda
print(fine_gioco)
#chiedo se vogliono acquistare il terno elemento
indizio_finale_si_no=str(input("Inserisci si o no per aquistare il terzo elemento: "))
#controllo la risposta
if(indizio_finale_si_no=='si'):
    #mostro l terzo elemento
    print(fine_gioco_indizio)
#chiedo la risposata
prova_finale=str(input("Inserisci l'ultima parola corretta per vincere: "))
#controllo se è giusta
if(prova_finale==fine_gioco_risposta):
    #stampo il monte premi vinto
    print('Bravi! Avete vinto: '+saldo_finale)
else:
    print('Mi spiace, avete perso')