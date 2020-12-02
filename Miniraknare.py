while True: #Skapar en loop som kör automatiskt, för att det logiska uttrycket är true
    print('\n[1] Räkna med + \n[2] Räkna med - \n[3] Räkna med * \n[4] Räkna med / \n[5] Avsluta') #printar menyn vi skulle använda i uppgiften, använder \n istället för fler prints
    choise = input('Välj funktion 1 till 5: ') #En input där du väljer vilken funktion du vill använda
    if choise in ('1', '2', '3', '4'): # Om inputen var 1, 2, 3 eller 4 kommer den att fortsätta med sin kod annars hoppar den till elif där 5 är och breakar loopen.

      tal1 = float(input('Skriv ett tal: ')) #input för första talet
      tal2 = float(input('Skriv ett andra tal: ')) #input för andra talet
        
      if choise == '1': #logiskt uttryck om variabeln choise är 1 printa + funktionen
          print('{} + {} = '.format(tal1, tal2)) #använder .format där man kan säga vart en variabel ska vara med hjälp av mås-vingar.
          print(tal1 + tal2) #Gör uträkningen och printar svaret
      elif choise == '2': #logiskt uttryck om variabeln choise är 2 printa - funktionen
          print('{} - {} = '.format(tal1, tal2))
          print(tal1 - tal2)
      elif choise == '3': #logiskt uttryck om variabeln choise är 3 printa * funktionen
          print('{} * {} = '.format(tal1, tal2))
          print(tal1 * tal2)
      elif choise == '4': #logiskt uttryck om variabeln choise är 4 printa / funktionen
          print('{} / {} = '.format(tal1, tal2))
          print(tal1 / tal2)
    elif choise == '5': #Om choise variablen är samma som 5 kommer den att printa "Avslutar..." och breaka loopen
        print('Avslutar...')
        break
    else: #Else används om man skriver t.ex. funktion 6 eller högre
        print('Ogiltig funktion')
