#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Johana Rangel
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.2"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    numero_1 = float(input('Ingrese el primer número:\n'))
    numero_2 = float(input('Ingrese el segundo número:\n'))

    resultado = numero_1 - numero_2

    if resultado == 0:
        print('El resultado de la diferencia entre {} y {} es igual a cero'.format(numero_1, numero_2))
    
    elif resultado > 0:
        print('El resultado de la diferencia entre {} y {} es positivo'.format(numero_1, numero_2))
    
    else:
        print('El resultado de la diferencia entre {} y {} es negativo'.format(numero_1, numero_2))


def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    entero_1 = int(input('Ingrese primer número entero:\n'))
    entero_2 = int(input('Ingrese segundo número entero:\n'))
    entero_3 = int(input('Ingrese tercer número entero:\n'))

    if (entero_1 % 2 == 0): 
        print('El número {} es par'.format(entero_1))
    else:
        print('El número {} es impar'.format(entero_1))
        
    if (entero_2 % 2 == 0):
        print('El número {} es par'.format(entero_2))
    else:
        print('El número {} es impar'.format(entero_2))

    if (entero_3 % 2 == 0):
        print('El número {} es par'.format(entero_3))
    else:
        print('El número {} es impar'.format(entero_3))
          


def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    numero_uno = float(input('Ingrese un número: \n'))
    numero_dos = float(input('Ingrese otro número: \n'))
    simbolo_operacion = str(input('''Ingrese el simbolo de la operación a realizar (+ suma, - resta, * multiplicación, / división, **Potencia ): \n'''))

    if (simbolo_operacion == '+'):
        resultado = numero_uno + numero_dos
        print('El resultado de sumar {} y {} es {}'.format(numero_uno, numero_dos, resultado)) 

    elif (simbolo_operacion == '-'):
        resultado = numero_uno - numero_dos
        print('El resultado de restar {} y {} es {}'.format(numero_uno, numero_dos, resultado)) 

    elif (simbolo_operacion == '*'):
        resultado = numero_uno * numero_dos
        print('El resultado de multiplicar {} y {} es {}'.format(numero_uno, numero_dos, resultado)) 

    elif (simbolo_operacion == '/'):
        resultado = numero_uno / numero_dos
        print('El resultado de dividir {} y {} es {}'.format(numero_uno, numero_dos, resultado)) 

    elif (simbolo_operacion == '**'):
        resultado = numero_uno ** numero_dos
        print('El resultado de {} a la potencia {} es {}'.format(numero_uno, numero_dos, resultado)) 
    
    else:
        print('Simbolo no corresponde con los indicados')

def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    palabra_1 = str(input('Ingrese la primera palabra: \n'))
    palabra_2 = str(input('Ingrese la segunda palabra: \n'))
    palabra_3 = str(input('Ingrese la tercera palabra: \n'))
    
    consulta = str(input('Cómo quiere ordenar la palabras? \n Ingrese 1, si quiere ordenar por alfabético. \n Ingrese 2, si quiere ordenar por cantidad de palabras?: \n'))

    if consulta == '1':
        if palabra_1 > palabra_2 > palabra_3:
            print('Palabras de mayor a menor, por orden alfabético: {}, {}, {}'.format(palabra_1, palabra_2, palabra_3))
    
        elif palabra_2 > palabra_3 > palabra_1:
            print('Palabras de mayor a menor, por orden alfabético: {}, {}, {}'.format(palabra_2, palabra_3, palabra_1))
    
        elif palabra_3 > palabra_1 > palabra_2:
            print('Palabras de mayor a menor, por orden alfabético: {}, {}, {}'.format(palabra_3, palabra_1, palabra_2))
    
        elif palabra_1 > palabra_3 > palabra_2:
            print('Palabras de mayor a menor, por orden alfabético: {}, {}, {}'.format(palabra_1, palabra_3, palabra_2))

        elif palabra_2 > palabra_1 > palabra_3:
            print('Palabras de mayor a menor, por orden alfabético: {}, {}, {}'.format(palabra_2, palabra_1, palabra_3))
        
        else:
            print('Palabras de mayor a menor, por orden alfabético: {}, {}, {}'.format(palabra_3, palabra_2, palabra_1))

    if consulta == '2':
        if len(palabra_1) > len(palabra_2) > len(palabra_3):
            print('Palabras de mayor a menor, por cantidad de palabras: {}, {}, {}'.format(palabra_1, palabra_2, palabra_3))
    
        elif len(palabra_2) > len(palabra_3) > len(palabra_1):
            print('Palabras de mayor a menor, por cantidad de palabras: {}, {}, {}'.format(palabra_2, palabra_3, palabra_1))
    
        elif len(palabra_3) > len(palabra_1) > len(palabra_2):
            print('Palabras de mayor a menor, por cantidad de palabras: {}, {}, {}'.format(palabra_3, palabra_1, palabra_2))
    
        elif len(palabra_1) > len(palabra_3) > len(palabra_2):
            print('Palabras de mayor a menor, por cantidad de palabras: {}, {}, {}'.format(palabra_1, palabra_3, palabra_2))

        elif len(palabra_2) > len(palabra_1) > len(palabra_3):
            print('Palabras de mayor a menor, por cantidad de palabras: {}, {}, {}'.format(palabra_2, palabra_1, palabra_3))
        
        else:
            print('Palabras de mayor a menor, por cantidad de palabras: {}, {}, {}'.format(palabra_3, palabra_2, palabra_1))


def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

    temperatura_1 = float(input('Ingrese el primer valor de temperatura: \n'))
    temperatura_2 = float(input('Ingrese el segundo valor de temperatura: \n'))
    temperatura_3 = float(input('Ingrese el tercer valor de temperatura: \n'))

    promedio = (temperatura_1 + temperatura_2 + temperatura_3)/3
    
    if temperatura_1 > temperatura_2 > temperatura_3:
        print('La máxima temperatura es {}'.format(temperatura_1))
        print('La mínima temperatura es {}'.format(temperatura_3))
        print('El promedio de las temperaturas {}, {}, {} es {}'.format(temperatura_1, temperatura_2, temperatura_3, round(promedio,2)))

    elif temperatura_2 > temperatura_3 > temperatura_1:
        print('La máxima temperatura es {}'.format(temperatura_2))
        print('La mínima temperatura es {}'.format(temperatura_1))
        print('El promedio de las temperaturas {}, {}, {} es {}'.format(temperatura_1, temperatura_2, temperatura_3, round(promedio,2)))

    elif temperatura_3 > temperatura_1 > temperatura_2:
        print('La máxima temperatura es {}'.format(temperatura_3))
        print('La mínima temperatura es {}'.format(temperatura_2))
        print('El promedio de las temperaturas {}, {}, {} es {}'.format(temperatura_1, temperatura_2, temperatura_3, round(promedio,2)))

    elif temperatura_1 > temperatura_3 > temperatura_2:
        print('La máxima temperatura es {}'.format(temperatura_1))
        print('La mínima temperatura es {}'.format(temperatura_2))
        print('El promedio de las temperaturas {}, {}, {} es {}'.format(temperatura_1, temperatura_2, temperatura_3, round(promedio,2)))

    elif temperatura_2 > temperatura_1 > temperatura_3:
        print('La máxima temperatura es {}'.format(temperatura_2))
        print('La mínima temperatura es {}'.format(temperatura_3))
        print('El promedio de las temperaturas {}, {}, {} es {}'.format(temperatura_1, temperatura_2, temperatura_3, round(promedio,2)))

    else: 
        print('La máxima temperatura es {}'.format(temperatura_3))
        print('La mínima temperatura es {}'.format(temperatura_1))
        print('El promedio de las temperaturas {}, {}, {} es {}'.format(temperatura_1, temperatura_2, temperatura_3, round(promedio,2)))


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
