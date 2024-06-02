print("METODO PARA CADENAS DE TEXTO")
#Metodo lengt para contar el numero de caracteres que hay en una variable de texto
nombre = "jhonatan Isai"
print(nombre)
print("Longitud de nuestra variable nombre: ",len(nombre))
print("")
#metodo de busqueda de un caracterer en una cadena de texto
buscar = "I"
print("Posicion en la que se encuentra el caracter '"+buscar+"' es :",nombre.find(buscar))
print("")
#Metodo para poner la primera letra de un cadena  de texto en Mayuscula
print(nombre)
print("Poniendo la primera letra en Mayuscula: ",nombre.capitalize())
print("")

#metodo para convertir toda la cadena a mayuculas
print("Convirtiendo a mayuculas todo el texto: ")
print(nombre.upper())
print("")
#metodo para convertir toda la cadena a mayuculas
print("Convirtiendo todo la cadena a minisculas")
print(nombre.lower())
print("")
#Metodo para saber si una cadena es un digito o no
edad = "18"
print("Metodo para saber si un cadena es un digito o no")
print(nombre.isdigit())
print(edad.isdigit())
print("")

#metodo para saber si una cadena contiene caracteres especiales
print("Metodo para saber si un cadena es alpha osea que si corrida")
print(nombre.isalpha())
print(edad.isalpha())
print("")

#metodo para cuantos caracteres de un determinado hay en la cadena
print("Método para saber cuantos caracteres de un determiando valor hay")
pais = "Rusiaa";
print(pais.count("a"))
print("")

#metodo para reemplazar caracteres dentro de una cadena
print("Método para reemplazar caracteres en una cadena")
mascota = "Simba"
print(mascota)
print("Variable modificada")
print(mascota.replace("i","v")) #reeemplazamos la i por la v
print("")

#metodo para mostrar una cadena varias veces
print("Método para mostrar una cadena varias veces")
print(mascota*4)