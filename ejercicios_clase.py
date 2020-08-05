#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Johana Rangel
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.2"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if numero_1 > numero_2:
        print('El {} es mayor que {}'.format(numero_1, numero_2))

    else:
        print('El {} es mayor que {}'.format(numero_2, numero_1))

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 > 0:
        print('El {} es un número positivo'.format(numero_1))
    
    elif numero_1 == 0:
        print('El {} es un número igual a cero'.format(numero_1))

    else:
        print('El {} es un número negativo'.format(numero_1))
        
    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if 0 < numero_1 < 100:
        print('El {} es mayor a cero y menor a cien'.format(numero_1))

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 < 10):
        print('El {} es menor a 10'.format(numero_1))

    if (numero_2 > -2):
        print('El {} es mayor que -2'.format(numero_2))


def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
       print('{} es mayor que {}'.format(texto_1, texto_2))
    
    elif texto_2 > texto_1:
        print('{} es mayor que {}'.format(texto_2, texto_1)) 

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    if len(texto_1) > len(texto_2):
        print('{} tiene mayor cantidad de letras que {}'.format(texto_1, texto_2))

    elif len(texto_1) < len(texto_2):
        print('{} tiene mayor cantidad de letras que {}'.format(texto_2, texto_1))

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    
    if (texto_1[0] > texto_2[0]):
        print('La primera letra de {} es mayor a la primera letra de {}'.format(texto_1, texto_2))
    
    elif (texto_1[0] < texto_2[0]):
        print('La primera letra de {} es mayor a la primera letra de {}'.format(texto_2, texto_1))

    else:
        print('Las primeras letras de {} y {}, son iguales'.format(texto_1, texto_2))

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    
    if (copia_texto_1==texto_1):
        print('Entonces, la copia del texto uno ({}) es igual a {}'.format(copia_texto_1, texto_1)) 

    else:
        print('No son iguales {} y {}'.format(copia_texto_1, texto_1)) 


    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    if copia_texto_1 != texto_2:
        print('{} es diferente de {}'.format(copia_texto_1, texto_2))
    
    else:
        print('{} es igual a {}'.format(copia_texto_1, texto_2))



def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados-
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > 5:
        print("Afirmativo, {} es mayor a cinco".format(numero_1))
    elif numero_2 > 0:
        print('Resp=1, {} es mayor a 5 y {} es positivo'.format(numero_1, numero_2))
    else:
        print('Resp=2, 5 es mayor a {} y {} es negativo'.format(numero_1, numero_2))

    if (not(numero_1 > 5)):
        print("Negativo, {} no es mayor a cinco".format(numero_1))
    elif numero_2 > 5:
        print('Resp=3, {} no es mayor a 5 y {} es mayor a 5'.format(numero_1, numero_2))
    else:
        print('Resp=4, 5 no es mayor a {} y 5 es mayor a {}'.format(numero_1, numero_2))

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if puntaje == 70:
        if puntaje >= 90:
            print('La calificación del estudiante de puntaje {} es A'.format(puntaje))
        
        elif puntaje >= 80:
            print('La calificación del estudiante de puntaje {} es B'.format(puntaje))
        
        elif puntaje >= 70:
            print('La calificación del estudiante de puntaje {} es C'.format(puntaje))

        elif puntaje >= 60:
            print('La calificación del estudiante de puntaje {} es D'.format(puntaje))

        else:
            print('La calificación del estudiante de puntaje {} es F'.format(puntaje))
    

def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print('{} es mayor alfabeticamente que {}'.format(texto_1, texto_2))
    else: 
        print('{} es mayor alfabeticamente que {}'.format(texto_2, texto_1))

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)

    numerica_1 = 5
    numerica_2 = 7

    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    if numerica_1  > numerica_2 :
        print('{} es mayor que {}'.format(numerica_1 , numerica_2))
    else: 
        print('{} es mayor que {}'.format(numerica_2 , numerica_1))

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
    
    #Respuesta:
    #texto 2 es mayor que texto 1, esto se debe al codigo unicode que le corresponde a cada uno. 
    #Por ejemplo, para saber el código de ambos se usa la función ord(), y así saber quien es mayor, al
    #corroborar esto, arroja los siguientes resultados.
    #print('El código que le coorresponde a texto 2 es', ord('7'))
    #print('El código que le coorresponde a texto 1 es',ord('5'))

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    #ej2()
    #ej3()
    #ej4()
