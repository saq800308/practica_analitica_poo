 #se importa los archivos necesarios 
from figuras_geometricas import figura_geometrica
from Circulo import Circulo
from Cuadrado import cuadrado
from Triangulo import Triangulo
from Rectangulo import Rectangulo
from Cubo_perfecto import Cubo_perfecto
# se crea un bucle con el menu y las opciones 
while True:
    print("menu")
    print("1. area rectangulo")
    print("2. Area Cuadrada")
    print("3. Area Triangulo")
    print("4. Area Circulo")
    print("5. Area Cubo")
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
   
    elif opcion=="0":
        print("Adios")
        #cierra el bucle y se sale del menu
        break
    else:
        print("opcion no valida vuelve a intentarlo")   