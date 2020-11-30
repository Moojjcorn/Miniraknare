while True: 
    print('[1] Räkna med + \n[2] Räkna med - \n[3] Räkna med * \n[4] Räkna med / \n[5] Avsluta')
    choise = (input('Välj funktion 1 - 5: '))
    if choise in ('1', '2', '3', '4'):
        tal1 = float(input('Skriv ett tal: '))
        tal2 = float(input('Skriv ett andra tal: '))
    elif choise == 5:
        print('Stänger ned')
        break
