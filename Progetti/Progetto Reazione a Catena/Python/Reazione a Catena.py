import random  
saldo_squadra_1=0 
saldo_squadra_2=0 
numero_prove=0 
numero_canzone_precedente=0
numero_parola_precedente=0
numero_2=0
numero_3=0
lista_parole=['ciao', 'cane', 'gatto','topo','penna','matita','computer','telefono','quaderno','carta','pasta','pizza','bello','lampada','alfabeto','vocali'] 
lista_indizi=['saluto','animale','animale','roditore','scrittura','grafite','informatica','chiamate','carta','alberi','alimento che si cuoce in acqua','alimento con pomodoro e mozzarella', 'aggettivo','fa luce','lettere','no consonanti'] 
lista_parole_2=['c--o','c--e','g---o','t--o','p---a','m----a','c------r','t------o','q------o','c---a','p---a','p---a','b---o','l-----a','a------o','v----i'] 
lista_testo_canzoni=['non volano farfalle, non stò più nella pelle...',"gloria, manchi tu nell'aria, chiesa di campania...","fatti mandare dalla mamma, a prendere il latte...","Un bicchiere di vino, con un panino...",'Camminerò ad un passo da te e fermeremo il vento...','La vita senza amore dimmi tu che vita è, oh dove sei andata...','Ma quanto è bello andare il giro con le ali sotto i piedi...','Perfavore non piangere e non ci rimanele male che noi due ci conosciamo bene...',"Ho guardato dentro un'emozione e ci ho visto tanto amore e ho capito perchè non si comanda il cuore"] 
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
print('Benvenuti a Reazione a Catena, in questo gioco si può giocare solo in 6 persone, vi dovrete dividere in due squadre e scegliere un nome! Per decidere chi inizierà il gioco scegliete un capitano e inserite la loro età, partirà la squadra che ha il capitano più vecchio')  
nome_1=str(input('Inserisci il nome della prima squadra: '))  
nome_2=str(input('Inserisci il nome della seconda squadra: '))  
età_1=int(input("Inserisci l'età del capitano della prima squadra: "))  
età_2=int(input("Inserisci l'età del capitano della seconda squadra: "))  
print("Bene, iniziamo. Io sono Marco Liorni, il conduttore di Reazione a Catena. Il primo gioco è una sorta di impiccato solo che dovrete inserire non lettere ma parole, ogni parola provata e sbagliata il turno passerà all'altra squadra. Se anche essa sbaglierà toccherà di nuovo alla squadra precedente ma avranno un indizio. Ogni parola azzeccata vale 2000 euro. Ci saranno quatrto manche. Chiunque indovinerà il turno passerà alla squadra che ha iniziato per primo. P.S. inserisci le parole con le lettere minuscole.")  
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
        numero_parola:int=random.randrange(0,15) 
        parola=lista_parole[numero_parola] 
        parola_2:str=lista_parole_2[numero_parola] 
        indizio:str=lista_indizi[numero_parola] 
        i=0 
        if(numero_parola==numero_parola_precedente and numero_parola==numero_2 and numero_parola==numero_3):
            continue
        else:
            break
    while True:  
        print('La parola da trovare è: '+parola_2)  
        if(i>=2):  
            print('Avrete un suggerimento, esso è: '+indizio)  
        prova=str(input('Inserisci la parola giusta: '))  
        if(prova==parola):  
            break  
        else:  
            print('Mi spiace, hai sbagliato. Ora tocca alla squadra avversaria.')  
            i=i+1  
    print('Bravi, avete indovinato')  
    if(i%2==0):  
        saldo_squadra_1=saldo_squadra_1+2000 
    else:  
        saldo_squadra_2=saldo_squadra_2+2000 
    print(squadra_1+' siete a: ')
    print(saldo_squadra_1) 
    print(squadra_2+' siete a: ')
    print(saldo_squadra_2) 
    numero_parola_precedente=numero_parola
    numero_2=numero_parola_precedente
    numero_3=numero_2
    if(numero_prove==3): 
        break 
    numero_prove=numero_prove+1 
print("Perfetto, siamo giunti al seondo gioco, questo consisterà nel trovare il titolo della canzone dato il testo. Avrete come prima una possibilità a squadra senza indizi. Una volta provato entrame le squadre senza ottenere risultati, apparirà un suggerimento che sarà l'autore della canzone. Ora inizierà la squadra che ha un monte premi più basso, nel caso sia pari inizierà la squadra con il capitano più anziano. Possiamo partire. P.S. inserisci le parole con le lettere minuscole.") 
if(saldo_squadra_1==saldo_squadra_2): 
    if(età_1>età_2):  
        print('Inizieranno i/gli '+squadra_1)  
        squadra_1=squadra_1 
        squadra_2=squadra_2
        saldo_squadra_1=saldo_squadra_1
        saldo_squadra_2=saldo_squadra_2
    else:  
        print('Inizieranno i/gli '+squadra_2)  
        squadra_1_2=squadra_2
        squadra_2_2=squadra_1
        saldo_squadra_1_2=saldo_squadra_2
        saldo_squadra_2_2=saldo_squadra_1
else: 
    if(saldo_squadra_1>saldo_squadra_2):  
        print('Inizieranno i/gli '+squadra_1)  
        squadra_1_2=squadra_1  
        squadra_2_2=squadra_2  
        saldo_squadra_1_2=saldo_squadra_1
        saldo_squadra_2_2=saldo_squadra_2
    else:  
        print('Inizieranno i/gli '+squadra_2)  
        squadra_1_2=squadra_2  
        squadra_2_2=squadra_1 
        saldo_squadra_1_2=saldo_squadra_2
        saldo_squadra_2_2=saldo_squadra_1
prove=0
i=0
numero_prove=0
numero_canzone_precedente=0
numero_canzone_2=0
numero_canzone_3=0
while True: 
    while True:
        numero_canzone:int=random.randrange(0,8) 
        canzone=lista_testo_canzoni[numero_canzone] 
        canzone_titolo:str=lista_nome_canzoni[numero_canzone] 
        indizio:str=lista_indizi_canzoni[numero_canzone] 
        i=0 
        if(numero_canzone==numero_canzone_precedente and numero_canzone==numero_canzone_2 and numero_canzone==numero_canzone_3):
            continue
        else:
            break
    while True:  
        print('Il testo della canzone che bisogna trovare è: '+canzone)  
        if(i>=2):  
            print('Avrete un suggerimento, esso è: '+indizio)  
        prova=str(input('Inserisci la parola giusta: '))  
        if(prova==canzone_titolo):  
            break  
        else:  
            print('Mi spiace, hai sbagliato. Ora tocca alla squadra avversaria.')  
            i=i+1  
    print('Bravi, avete indovinato')  
    if(i%2==0):  
        saldo_squadra_1_2=saldo_squadra_1_2+6000 
    else:  
        saldo_squadra_2_2=saldo_squadra_2_2+6000 
    print(squadra_1_2+' siete a: ')
    print(saldo_squadra_1_2) 
    print(squadra_2_2+' siete a: ')
    print(saldo_squadra_2_2) 
    numero_canzone_precedente=numero_canzone
    numero_canzone_2=numero_canzone_precedente
    numero_canzone_3=numero_canzone_2
    if(numero_prove==3): 
        break 
    numero_prove=numero_prove+1 
if(saldo_squadra_1_2>saldo_squadra_2_2): 
    squadra_1_3=squadra_1_2 
    squadra_2_3=squadra_2_2 
    saldo_squadra_1_3=saldo_squadra_1_2 
    saldo_squadra_2_3=saldo_squadra_2_2 
else: 
    squadra_1_3=squadra_2_2 
    squadra_2_3=squadra_1_2 
    saldo_squadra_2_3=saldo_squadra_2_2 
    saldo_squadra_1_3=saldo_squadra_2_2 
print("Siamo arriati all'ultimo gioco in cui potrete giocare entrambe le squadre, Dovrete trovare una parola che collega qulle che saranno date")
if(saldo_squadra_1_3>saldo_squadra_2_3):
    print('Inizieranno i/gli/le '+squadra_1_3)
    squadra_1_4=squadra_1_3
    squadra_2_4=squadra_2_3
    saldo_squadra_1_4=saldo_squadra_1_3
    saldo_squadra_2_4=saldo_squadra_2_3
else:
    print('Inizieranno i/gli/le '+saldo_squadra_2_3)
    squadra_1_4=squadra_2_3
    squadra_2_4=squadra_1_3
    saldo_squadra_2_4=saldo_squadra_2_3
    saldo_squadra_1_4=saldo_squadra_2_3
print(quarto_gioco_1)
print(quarto_gioco_2)
print(quarto_gioco_3)
print(quarto_gioco_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
prova_quarto_gioco=str(input(squadra_1_4+'Inserisci la tua parola: '))
if(prova_quarto_gioco==quarto_gioco_2):
    saldo_squadra_1_4=saldo_squadra_1_4+2000
    squadra_1_5=squadra_1_4
    saldo_squadra_1_5=saldo_squadra_1_4
    squadra_2_5=squadra_2_4
    saldo_squadra_2_5=saldo_squadra_2_4
    print('Bravi, avete indovinato')
    print(squadra_1_4+'siete a:')
    print(saldo_squadra_1_4)
    print(squadra_2_4+'siete a:')
    print(saldo_squadra_2_4)
else:
    saldo_squadra_2_5=saldo_squadra_2_4+2000
    saldo_squadra_2_5=saldo_squadra_1_4
    saldo_squadra_1_5=saldo_squadra_2_4
    squadra_2_5=squadra_1_4
    squadra_1_5=squadra_2_4
    print('Mi spiace, ora vedrete la risposta!')
    print(squadra_1_4+'siete a:')
    print(saldo_squadra_1_5)
    print(squadra_2_4+'siete a:')
    print(saldo_squadra_2_5)
print(quarto_gioco_1)
print(risposta_2)
print(quarto_gioco_3)
print(quarto_gioco_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
prova_quarto_gioco=str(input(squadra_1_5+'Inserisci la tua parola: '))
if(prova_quarto_gioco==quarto_gioco_3):
    saldo_squadra_1_5=saldo_squadra_1_5+2000
    squadra_1_6=squadra_1_5
    saldo_squadra_1_6=saldo_squadra_1_5
    squadra_2_6=squadra_2_5
    saldo_squadra_2_6=saldo_squadra_2_5
    print('Bravi, avete indovinato')
    print(squadra_1_6+'siete a:')
    print(saldo_squadra_1_6)
    print(squadra_2_6+'siete a:')
    print(saldo_squadra_2_6)
else:
    saldo_squadra_2_5=saldo_squadra_2_5+2000
    saldo_squadra_2_6=saldo_squadra_1_5
    saldo_squadra_1_6=saldo_squadra_2_5
    squadra_2_6=squadra_1_5
    squadra_1_6=squadra_2_5
    print('Mi spiace, ora vedrete la risposta!')
    print(squadra_1_6+'siete a:')
    print(saldo_squadra_1_6)
    print(squadra_2_6+'siete a:')
    print(saldo_squadra_2_6)
print(quarto_gioco_1)
print(risposta_2)
print(risposta_3)
print(quarto_gioco_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
prova_quarto_gioco=str(input(squadra_1_6+'Inserisci la tua parola: '))
if(prova_quarto_gioco==quarto_gioco_4):
    saldo_squadra_1_6=saldo_squadra_1_6+2000
    squadra_1_7=squadra_1_6
    saldo_squadra_1_7=saldo_squadra_1_6
    squadra_2_7=squadra_2_6
    saldo_squadra_2_7=saldo_squadra_2_6
    print('Bravi, avete indovinato')
    print(squadra_1_7+'siete a:')
    print(saldo_squadra_1_7)
    print(squadra_2_7+'siete a:')
    print(saldo_squadra_2_7)
else:
    saldo_squadra_2_6=saldo_squadra_2_6+2000
    saldo_squadra_2_7=saldo_squadra_1_6
    saldo_squadra_1_7=saldo_squadra_2_6
    squadra_2_7=squadra_1_6
    squadra_1_7=squadra_2_6
    print('Mi spiace, ora vedrete la risposta!')
    print(squadra_1_7+'siete a:')
    print(saldo_squadra_1_7)
    print(squadra_2_7+'siete a:')
    print(saldo_squadra_2_7)
print(quarto_gioco_1)
print(risposta_2)
print(risposta_3)
print(risposta_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
prova_quarto_gioco=str(input(squadra_1_7+'Inserisci la tua parola: '))
if(prova_quarto_gioco==quarto_gioco_5):
    saldo_squadra_1_7=saldo_squadra_1_7+2000
    squadra_1_8=squadra_1_7
    saldo_squadra_1_8=saldo_squadra_1_7
    squadra_2_8=squadra_2_7
    saldo_squadra_2_8=saldo_squadra_2_7
    print('Bravi, avete indovinato')
    print(squadra_1_8+'siete a:')
    print(saldo_squadra_1_8)
    print(squadra_2_8+'siete a:')
    print(saldo_squadra_2_8)
else:
    saldo_squadra_2_7=saldo_squadra_2_7+2000
    saldo_squadra_2_8=saldo_squadra_1_7
    saldo_squadra_1_8=saldo_squadra_2_7
    squadra_2_8=squadra_1_7
    squadra_1_8=squadra_2_7
    print('Mi spiace, ora vedrete la risposta!')
    print(squadra_1_8+'siete a:')
    print(saldo_squadra_1_8)
    print(squadra_2_8+'siete a:')
    print(saldo_squadra_2_8)
print(quarto_gioco_1)
print(risposta_2)
print(risposta_3)
print(risposta_4)
print(quarto_gioco_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
prova_quarto_gioco=str(input(squadra_1_8+'Inserisci la tua parola: '))
if(prova_quarto_gioco==quarto_gioco_6):
    saldo_squadra_1_8=saldo_squadra_1_8+2000
    squadra_1_9=squadra_1_8
    saldo_squadra_1_9=saldo_squadra_1_8
    squadra_2_9=squadra_2_8
    saldo_squadra_2_9=saldo_squadra_2_8
    print('Bravi, avete indovinato')
    print(squadra_1_9+'siete a:')
    print(saldo_squadra_1_9)
    print(squadra_2_9+'siete a:')
    print(saldo_squadra_2_9)
else:
    saldo_squadra_2_8=saldo_squadra_2_8+2000
    saldo_squadra_2_9=saldo_squadra_1_8
    saldo_squadra_1_9=saldo_squadra_2_8
    squadra_2_9=squadra_1_8
    squadra_1_9=squadra_2_8
    print('Mi spiace, ora vedrete la risposta!')
    print(squadra_1_9+'siete a:')
    print(saldo_squadra_1_9)
    print(squadra_2_9+'siete a:')
    print(saldo_squadra_2_9)
print(quarto_gioco_1)
print(risposta_2)
print(risposta_3)
print(risposta_4)
print(risposta_5)
print(quarto_gioco_6)
print(quarto_gioco_7)
if(saldo_squadra_2_9>saldo_squadra_1_9):
    print('Passano i/gli: '+squadra_2_9)
    squadra_finale=squadra_2_9
    saldo_finale=saldo_squadra_2_9
else:
    print('Passano i/gli: '+squadra_1_9)
    squadra_finale=squadra_1_9
    saldo_finale=saldo_squadra_1_9
print("Siamo giunti all'ultimo gioco, dovrete trovare una parola che accumuna le parole date. Avete una sola possibilità. Se sbagliate il monte premi si dimezzerà.")
print(ultimo_1)
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
if(prova_ultimo==ultimo_1_risposta):
    print('Hai indovinato')
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    saldo_finale=saldo_finale/2
    print(ultimo_1_risposta)
    print('Il vostro saldo è: '+saldo_finale)
print(ultimo_2)
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
if(prova_ultimo==ultimo_2_risposta):
    print('Hai indovinato')
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    saldo_finale=saldo_finale/2
    print(ultimo_2_risposta)
    print('Il vostro saldo è: '+saldo_finale)
print(ultimo_3)
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
if(prova_ultimo==ultimo_3_risposta):
    print('Hai indovinato')
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    saldo_finale=saldo_finale/2
    print(ultimo_3_risposta)
    print('Il vostro saldo è: '+saldo_finale)
print(ultimo_4)
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
if(prova_ultimo==ultimo_4_risposta):
    print('Hai indovinato')
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    saldo_finale=saldo_finale/2
    print(ultimo_4_risposta)
    print('Il vostro saldo è: '+saldo_finale)
print(ultimo_5)
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
if(prova_ultimo==ultimo_5_risposta):
    print('Hai indovinato')
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    saldo_finale=saldo_finale/2
    print(ultimo_5_risposta)
    print('Il vostro saldo è: '+saldo_finale)
print(ultimo_6)
prova_ultimo=str(input('Inserisci la parole che accomuna le parole date: '))
if(prova_ultimo==ultimo_6_risposta):
    print('Hai indovinato')
else:
    print('Hai sbagliato, ora ti mostro la soluzione. Il vostro montepremi di dimezzerà.')
    saldo_finale=saldo_finale/2
    print(ultimo_6_risposta)
    print('Il vostro saldo è: '+saldo_finale)
print("Ora dovrete trovare l'ultima parola, avrete però solo una parola data. Potrete chiedere l'altra parola ma il monte premi si dimezzerà. Se volete comprare il terzo elemento, scrivete 'Aquisto'")
print(fine_gioco)
indizio_finale_si_no=str(input("Inserisci si o no per aquistare il terzo elemento: "))
if(indizio_finale_si_no=='si'):
    print(fine_gioco_indizio)
prova_finale=str(input("Inserisci l'ultima parola corretta per vincere: "))
if(prova_finale==fine_gioco_risposta):
    print('Avete vinto: '+saldo_finale)
else:
    print('Mi spiace, avete perso')