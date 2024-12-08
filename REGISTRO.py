print("****************************************************************************************************************")
print("*                                            REGISTRO DE DATOS                                                 *")
print("****************************************************************************************************************")

while True:

    name = input('Ingresa tu nombre: ')
    edad = input("Ingresa tu edad: ")
    telefono = input('Ingresa tu teléfono: ')
    email = input('Ingresa tu correo electrónico: ')

    print('\n '+name+' de '+edad+' años de edad, tus datos han sido registrados exitosamente!')

    print("****************************************************************************************************************")

    with open('Registro.txt','a') as file: #En el apartado con la "a" esta significa "append" que nos permite modificar y agregar datos, otras variables son: "w" que es write, que lo abre en modo de escritura y "r" que es read, que solo nos permite leer
        file.write(f' Nombre:{name}')
        file.write(f' Edad:{edad}')
        file.write(f' Teléfono:{telefono}')
        file.write(f' Correo Electrónico:{email}')

    opc = input('Quieres agregar otro registro?')

    if opc=='n':
        break