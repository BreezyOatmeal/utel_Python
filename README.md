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
float: Para asegurar no tener problemas al momento de ingresar decimales

Luego con los datos recopilados se buscaba conseguir el IMC con el siguiente código:

IMC = p / a**2

Después de ser calculado el IMC, también agregué un clasificado en base al mismo para determinar en donde se encuentra el usuario con respecto a su IMC:

if IMC < 18.5:
    print("Saca la espinaca enclenque!")
elif 18.5 <= IMC < 24.9:
    print("Eres promedio, sigue así!.")
elif 25 <= IMC < 29.9:
    print("Una no es ninguna eh?")
else:
    print("Que te pansó!?")

Cabe mencionar que al código se le agregó una variable para más de una persona en una sola ejecución, en donde en caso de solo ser 1 persona, al final de ingresar los datos de la misma, el programa se termine.

En general, fue muy divertido y destresante el realizar este proyecto, ahora si que en la práctica es donde uno se desenvuelve más, logré poner a prueba todo lo aprendido hasta ahora, incluso
pude aprender ciertas cosas adicionales para compensar ciertas necesidades en el código. Espero con ansias el próximo proyecto!!!

