print("Ingresar Texto en Python")

#solicitamos 
nombre = input("¿Cual es tu nombre?: ")
edad = int(input("¿Cuantos años tienes?: ")) #convertimos a entero
altura = float(input("¿Cuanto alto Eres?: "))
edad = edad + 1

print("Hola como estas! "+nombre+
       " tu edad es "+str(edad)+" años. Mides "
       +str(altura)+" cm.")