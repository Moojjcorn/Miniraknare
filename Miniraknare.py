while True: 
    print('\n[1] Räkna med + \n[2] Räkna med - \n[3] Räkna med * \n[4] Räkna med / \n[5] Avsluta')
    choise = input('Välj funktion 1 till 5: ')
    if choise in ('1', '2', '3', '4'):

      tal1 = float(input('Skriv ett tal: '))
      tal2 = float(input('Skriv ett andra tal: '))
      if choise == '1':
          print('{} + {} = '.format(tal1, tal2))
          print(tal1 + tal2)
      elif choise == '2':
          print('{} - {} = '.format(tal1, tal2))
          print(tal1 - tal2)
      elif choise == '3':
          print('{} * {} = '.format(tal1, tal2))
          print(tal1 * tal2)
      elif choise == '4':
          print('{} / {} = '.format(tal1, tal2))
          print(tal1 / tal2)
    elif choise == '5':
        print('Avslutar...')
        break
    else:
        print('Ogiltig funktion')
