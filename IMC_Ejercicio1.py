#Ejercicio 1: Indice de masa corporal (IMC)


def imc(estatura,peso):
    """
    Calcula tu inidice de masa corporal 
    """
    return peso/estatura**2

peso = float(input("Escriba su peso en (Kg):"))
estatura = float(input("Escribas su estaruea en (m):"))

Indice = imc(estatura,peso)  

print("Su indice de masa corporal es:{}".format(Indice))
