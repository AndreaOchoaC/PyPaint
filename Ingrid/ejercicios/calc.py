
    
print("hola, bienvienido a la calculadora, puede hacer esto")
print("1 - suma \n 2 - resta \n 3 - multiplicación \n 4 - división \n 5 - potencia \n 0 - salir")
seleccion = int(input("cuál eliges?: "))

while seleccion != 0:
    
    print("hola, bienvienido a la calculadora, puede hacer esto")
    print("1 - suma \n 2 - resta \n 3 - multiplicación \n 4 - división \n 5 - potencia \n 0 - salir")
    seleccion = int(input("cuál eliges?: "))

    if seleccion == 1:
        numero1 = int(input("dame un número"))
        numero2 = int(input("dame otro número"))

        print(numero1 + numero2)

    if seleccion == 2:
        numero1 = int(input("dame un número"))
        numero2 = int(input("dame otro número"))

        print(numero1 - numero2)

    if seleccion == 3:
        numero1 = int(input("dame un número"))
        numero2 = int(input("dame otro número"))

        print(numero1 * numero2)

    if seleccion == 4:
        numero1 = int(input("dame un número"))
        numero2 = int(input("dame otro número"))

        print(numero1 // numero2)

    if seleccion == 5:
        numero1 = int(input("dame un número"))
        numero2 = int(input("dame el número al que va a estar elevado"))

        print(numero1 ** numero2)

   
