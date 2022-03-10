class Cola:
    def __init__(self, cliente, pizzas, ingredientes, tiempo):
        self.cliente = cliente
        self.pizzas = pizzas
        self.ingredientes = ingredientes
        self.tiempo = tiempo

class Lista_Cola:
    def __init__(self):
        self.cola = []
    
    def insertarCola(self,cliente):
        self.cola.append(cliente)
    
    def recorrer(self):
        if self.cola:
            for elemento in self.cola:
                print("Datos del Cliente : ", elemento.cliente, "Pizzas ordenadas: ", elemento.pizzas, "Ingredientes Utilizados: ", elemento.ingredientes, "Timpo de Espera: ", elemento.tiempo," minutos")    
        else:
            print("La cola esta vacia")     


    def desencolar(self):
        if self.cola:
            self.cola.pop(0)
        else: 
            print("No hay cola para entregar")
    def devolver_tamano(self):
        return len(self.cola)

    #def graficar(): 