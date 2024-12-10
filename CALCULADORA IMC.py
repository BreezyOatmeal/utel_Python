print('************************************************************************************************************')
print('*                                BIENVENIDO A TU CALCULADORA DE IMC 3000                                   *')
print('************************************************************************************************************')

personas = int(input("Cuántas personas deseas ingresar? "))

while personas > 0:
    personas -= 1  

    n = ""
    while not n.strip():
        n = input('Ingresa tu nombre: ')
        if not n.strip():
            print('Ingresa un nombre porfavor!')

    ap = ""
    while not ap.strip():
        ap = input('Ingresa tu apellido paterno: ')
        if not ap.strip():
            print('Ingresa un apellido paterno porfavor!')

    am = ""
    while not am.strip():
        am = input('Ingresa tu apellido materno: ')
        if not am.strip():
            print('Ingresa un apellido materno porfavor!')

    while True:
        try:
            e = int(input('Ingresa tu edad en años: '))
            if e <= 0:
                print('Por favor, ingresa una edad válida.')
            else:
                break
        except ValueError:
            print('Por favor, ingresa un número válido para la edad.')

    while True:
        try:
            p = float(input('Ingresa tu peso en KG: '))
            if p <= 0:
                print('Ingresa tu peso porfavor!')
            else:
                break
        except ValueError:
            print('Por favor, ingresa un número válido para el peso.')

    while True:
        try:
            a = float(input('Ingresa tu altura en Mts: '))
            if a <= 0:
                print('Ingresa tu altura porfavor')
            else:
                break
        except ValueError:
            print('Por favor, ingresa un número válido para tu altura.')

    IMC = p / a**2

    print(f'\n*********************************************************************************************************')

    print(f"\nResumen para {n} {ap} {am}:")
    print(f"Edad: {e} años")
    print(f"Peso: {p} kg")
    print(f"Altura: {a} m")
    print(f"IMC: {IMC:.2f}")

    if IMC < 18.5:
        print("Saca la espinaca enclenque!")
    elif 18.5 <= IMC < 24.9:
        print("Eres promedio, sigue así!.")
    elif 25 <= IMC < 29.9:
        print("Una no es ninguna eh?")
    else:
        print("Que te pansó!?")

    print(f'\n*********************************************************************************************************')
    

    