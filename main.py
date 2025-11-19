 #se importa los archivos necesarios 
from figuras_geometricas import figura_geometrica
from Circulo import Circulo
from Cuadrado import cuadrado
from Triangulo import Triangulo
from Rectangulo import Rectangulo
from Cubo_perfecto import Cubo_perfecto
from Cilindro import Cilindro
from paralelograma import paralelograma
from Esfera import Esfera
# se crea un bucle con el menu y las opciones 
while True:
    print("menu")
    print("1. area rectangulo")
    print("2. Area Cuadrada")
    print("3. Area Triangulo")
    print("4. Area Circulo")
    print("5. Area Cubo")
    print("6. Area Cilindro")
    print("7. Area Paralelograma")
    print("0. salir")
    #se selecciona la opcion requerrida
    opcion=input("Que opcion deseas:")
    #se ejecutan  las funciones segun la opcion elegida 
    if opcion=="1":
        print("rectangulo")
        #se piden las caracteristicas
        alto=float(input())
        largo=float(input())
        #se crea el objeto
        objeto=Rectangulo(largo,alto)
        objeto.nombre="ractangulo"
        #llama a la instacia
        print(f"El area de ",objeto.nombre," es de ",objeto.area())
        #escribe cual quier tecla para seguir 
        menu=input()
    elif opcion=="2":
        print("Cuadrado")
        #se piden las caracteristicas
        lado=float(input())
        #se crea el objeto
        objeto=cuadrado(lado)
        objeto.nombre="Cuadrado"
        #llama a la instacia
        print(f"El area de ",objeto.nombre," es de ",objeto.area())
        menu=input()
    elif opcion=="3":
        print("Triangulo")
        #se piden las caracteristicas
        base=float(input())
        altura=float(input())
        #se crea el objeto
        objeto=Triangulo(base,altura)
        objeto.nombre="Triangulo"
        #llama a la instacia
        print(f"El area de ",objeto.nombre," es de ",objeto.area())
        menu=input()
    elif opcion=="4":
        print("Circulo")
        #se piden las caracteristicas
        radio=float(input())
        #se crea el objeto
        objeto=Circulo(radio)
        objeto.nombre="Circulo"
         #llama a la instacia
        print(f"El area de ",objeto.nombre," es de ",objeto.area())
        menu=input()
    elif opcion=="5":
        print("Cubo perfecto")
        #se piden las caracteristicas
        lado=float(input())
        #se crea el objeto
        objeto=Cubo_perfecto("cubo perfecto")
        objeto.lado=lado
         #llama a la instacia
        print(f"El area de ",objeto.nombre," es de ",objeto.area())
        menu=input()
    elif opcion=="6":
        print("Cilindro")
        radio=float(input("ingrese el radio: "))
        altura=float(input("ingrse la altura: "))
        objeto=Cilindro("Cilindro")
        objeto.altura=altura
        objeto.radio=radio
        print(f"El area de ",objeto.nombre, " es de: ",objeto.area())
        menu=input()
    elif opcion=="7":
        print("Paralelograma")
        altura=float(input("ingrese la altura: "))
        base=float(input("ingrese la altura: "))
        objecto=paralelograma("Paralelograma")
        objeto.altura=altura
        objeto.base=base
        print(f"el area de ",objeto.nombre," es de: ",objeto.area())
        menu=input()
    elif opcion=="8":
        print("Esfera")
        radio=float(input("Ingresa el radio"))
        objeto=Esfera("Esfera")
        objeto.radio=radio
        print(f"el area de ",objeto.nombre," es de: ",objeto.area())
        menu=input()
    elif opcion=="0":
        print("Adios")
        #cierra el bucle y se sale del menu
        break
    else:
        print("opcion no valida vuelve a intentarlo")   