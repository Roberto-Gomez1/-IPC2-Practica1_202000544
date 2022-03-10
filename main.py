from nose import menu
from help import Lista_Cola, Cola
totalingrediente = []
def main():
    tiempo = 0
    lista = Lista_Cola()
    opcion = menu()

    while opcion !=5:
        if opcion == 1:
            nombre = str(input("Ingrese los datos del Cliente: "))
            pizza= int(input("Cantidad de pizzas: "))
            for i in range(pizza): 
                print("Opciones de pizza ")
                print("Pepperoni")
                print("Salchicha")
                print("Carne")
                print("Queso")
                print("Piña")
                ingrediente = str(input("Ingrediente: ")).upper()
                totalingrediente.append(ingrediente) 
                aux = 0
                suma=0
                if ingrediente == "PEPPERONI":
                    #tiempo += 3
                    aux = 3
                elif ingrediente == "SALCHICHA":
                    #tiempo += 4
                    aux = 4
                elif ingrediente == "CARNE":
                    #tiempo += 10
                    aux = 10
                elif ingrediente == "QUESO":
                    #tiempo += 5
                    aux = 5
                elif ingrediente == "PIÑA":
                    #tiempo += 2
                    aux = 2
                #suma += aux * pizza
                tiempo += aux
            temporal  = Cola(nombre, pizza, totalingrediente, tiempo)
            lista.insertarCola(temporal)
        elif opcion ==2:
            lista.recorrer()
            #lista.graficar()
        elif opcion == 3:
            lista.desencolar()
            #lista.colaVacia()
        elif opcion == 4:
            print("Roberto Carlos Gómez Donis")
            print("202000544")
            print("IPC 2 Seccion E")
        elif opcion == 5:
            print("Terminando el programa")
        opcion = menu();


if __name__ == "__main__":
    main()