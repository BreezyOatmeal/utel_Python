# Proyecto Calculadora
Esta es una explicación de como llevé a cabo la programación de esta calculadora sencilla de IMC y las diferentes herramientas que se utilizaron para realizarla:

Lo primero fue asignar preguntas para recopilar los datos necesarios del usuario:

- Nombre completo
- Edad
- Peso
- Altura

Para evitar que el usuario ingresara datos inválidos y fueran correctos los datos ingresados, investigué que métodos me ayudarían y pude agregar los siguientes al código:

strip - Para los espacios en blanco 
try-except - Para asegurar que el número fuera int y fuera un carácter numérico
float: Para asegurar no tener problemas´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´.
Altura: Se realizó la misma validación que para el peso, asegurando que fuera un número positivo en formato decimal.
El proceso de validación para cada entrada fue repetido hasta que se proporcionara un valor adecuado. A continuación se presentan los fragmentos de código responsables de la recolección y validación de datos:

python
Copiar código
while not n.strip():
    n = input('Ingresa tu nombre: ')
    if not n.strip():
        print('Ingresa un nombre porfavor!')

while True:
    try:
        e = int(input('Ingresa tu edad en años: '))
        if e <= 0:
            print('Por favor, ingresa una edad válida.')
        else:
            break
    except ValueError:
        print('Por favor, ingresa un número válido para la edad.')
2. Cálculo del IMC
El Índice de Masa Corporal (IMC) se calcula utilizando la siguiente fórmula:

𝐼
𝑀
𝐶
=
𝑝
𝑒
𝑠
𝑜
𝑎
𝑙
𝑡
𝑢
𝑟
𝑎
2
IMC= 
altura 
2
 
peso
​
 
Donde:

peso es la masa corporal en kilogramos.
altura es la estatura en metros.
Para calcular el IMC, primero se recoge el peso y la altura del usuario, y luego se aplica la fórmula. En el código, esto se hace utilizando el siguiente cálculo:

python
Copiar código
IMC = p / a**2
Donde p es el peso en kilogramos y a es la altura en metros.

3. Clasificación del IMC
Una vez calculado el IMC, es útil clasificar los resultados de acuerdo con las categorías establecidas por la Organización Mundial de la Salud (OMS):

Bajo peso: IMC < 18.5
Peso normal: 18.5 ≤ IMC < 24.9
Sobrepeso: 25 ≤ IMC < 29.9
Obesidad: IMC ≥ 30
Esta clasificación fue añadida al código para proporcionar una interpretación de los resultados del IMC. Los resultados se imprimen de forma clara, proporcionando tanto el valor numérico del IMC como la categoría correspondiente.

python
Copiar código
if IMC < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= IMC < 24.9:
    print("Clasificación: Peso normal")
elif 25 <= IMC < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
4. Ciclo para múltiples personas
En el código, se permitió que el programa procesara múltiples personas en una misma ejecución. Para ello, se introdujo una variable llamada personas, que le pregunta al usuario cuántas personas desea ingresar. Luego, el ciclo while se ejecuta para cada persona, recolectando los datos de forma independiente para cada uno.

python
Copiar código
personas = int(input("Cuántas personas deseas ingresar? "))
while personas > 0:
    personas -= 1  # Decrease the count of personas as each one is processed
5. Salida del Programa
El programa imprime un resumen para cada persona ingresada, mostrando su nombre completo, edad, peso, altura y el IMC calculado. Además, se imprime la clasificación del IMC, proporcionando información sobre el estado de salud en función del resultado.

python
Copiar código
print(f"\nResumen para {n} {ap} {am}:")
print(f"Edad: {e} años")
print(f"Peso: {p} kg")
print(f"Altura: {a} m")
print(f"IMC: {IMC:.2f}")
6. Consideraciones y Mejoras
El programa está diseñado para ser sencillo de usar y entender, pero se podrían agregar algunas mejoras:

Manejo de errores más robusto: Actualmente, el programa asume que el usuario sigue las instrucciones y no hace uso de caracteres especiales, lo cual podría mejorarse con una validación más estricta.
Interfaz de usuario gráfica (GUI): En un futuro, se podría mejorar la interacción con el usuario utilizando una interfaz gráfica (por ejemplo, con Tkinter) para que la experiencia sea más amigable.
Manejo de unidades de peso y altura: Sería útil permitir que el usuario elija entre diferentes unidades para peso y altura (kilogramos/pounds y metros/pies).
Conclusión
La calculadora de IMC fue desarrollada para ser una herramienta simple y efectiva para calcular el índice de masa corporal y clasificar el estado de salud del usuario. Se emplearon técnicas básicas de recolección de datos, validación de entradas y cálculos matemáticos para implementar la funcionalidad deseada. Con futuras mejoras, podría convertirse en una herramienta aún más accesible y útil para el usuario.

