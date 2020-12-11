#from utils.cadena import *

from src.Arma import Arma

arma_generica = Arma("k-47", "5 seg", 10)

salir = True
while salir:
    print("opcion 0) Salir")
    print("opcion 1) Obtener informacion")
    print("opcion 2) Disparar")
    print("opcion 3) Recargar municion")

    choice = input ("Seleccione una opcion :")

    if choice == "1":
        arma_generica.imprimir_informacion()
    elif choice == "2":
        arma_generica.disparar()
    elif choice == "3":
        arma_generica.recargar_municion()
    elif choice == "0":
        salir = False
        print("Vuelve pronto")
    else:
        print("Selecciona una opcion valida")


#saludar("Juan")
#saludar("Pedro")
#print(concatenar_nombre("Pedro", "Perez"))
