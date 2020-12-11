class Arma:

    #Constructor
    def __init__(self, modelo, tiempo_recarga, cantidad_municiones):
        self.modelo = modelo
        self.tiempo_recarga = tiempo_recarga
        self.cantidad_municiones = cantidad_municiones
        self.municion = cantidad_municiones
    
    #Metodo que sirve para imprimir informacion del arma
    #void
    def imprimir_informacion(self):
        print("El modelo es :"+ self.modelo + " y su tiempo de recarga es de " + self.tiempo_recarga)
    
    #Metodo que sirve para disparar
    #void
    def disparar(self):
        if(self.municion >= 1):
            self.municion -= 1
            print("pum pum " + str(self.municion))
        else:
            print("Ya no tiene muciones")

    #Metodo que sirve para regacar municiones
    #void
    def recargar_municion(self):
        self.municion = self.cantidad_municiones
        print("Tus municiones han sido recargadas")
