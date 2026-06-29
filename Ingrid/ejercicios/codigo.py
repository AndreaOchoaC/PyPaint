#numero = int(input("dame un número"))

#for i in range(5):
 #   numero = numero*2
  #  print(numero)



'''lista = ["Nicolas", "Cairo", "Estefania", "Merari", "Yade"]

for l in range(6):
    nombre = input("escribe el nombre")
    if nombre in lista:
        print("ya esta registrado")
    else:
        lista.append(nombre)


lista.append(lista)
print(lista)

print("el 2do alumno fue: ", lista[1])
lista.append("Ingrid")
print(lista)'''


#ej.3 comidas

'''lista = []

comida = input("dime una comida que te guste: ")
lista.append(comida)

while comida != "alto":
    comida = input("dime una comida que te guste: ")
    lista.append(comida)

del lista[-1]
print(lista)

print("top 3: ", lista[0:3])

'''

#guardar usuarios



'''lista = ["usuario1", "usuario2", "usuario3", "usuario4", "usuario5"]
lista2 = ["1", "2", "3", "4", "5"]

print(lista[2], lista2[2])

peticion = input("ingresa el nombre del usuario: ")
list.loc(peticion)

if peticion in lista:
    print("su contraseña es: ", )
else:
    print("no esta en la lista.")

'''

usuarios = dict()

usuarios = {
    "usuario1" : {
        "contrasena" : "1234",
        "edad" : 26 
    },
    "usuario2" : {
        "contrasena" : "123",
        "edad" : 16
    },
    "usuario3" : {
        "contrasena" : "124",
        "edad" : 22
    },
    "usuario4" : {
        "contrasena" : "14",
        "edad" : 11 
    },
    "usuario5" : {
        "contrasena" : "2406",
        "edad" : 37
    }

}

users_lista = []
contras_lista = []

for user in usuarios:
    print(user)
    users_lista.append(user)
    
    print(usuarios[user])

print(users_lista)
'''user = input("ingresa el usuario: ")

if user in users_lista:
    cont = usuarios[user]["contrasena"]
    edad = usuarios[user]["edad"]
    if edad >= 18:
        print("contraseña: ", cont, "edad: ", edad)
    else:
        print("este usuario es menor de edad")
    

else:
    print("no esta en la lista")'''

usuarios["usuario6"] = {
    "contraseña" : "hola",
    "edad" : 12
}


user_nuevo = input("ingresa el nuevo nombre de usuario: ")

while user_nuevo != "salir":

    if user_nuevo in usuarios:
        print("este usuario ya existe.")
    else:
        cont_nueva = input("ingresa la contraseña: ")
        edad_nueva = int(input("ingresa la edad nueva: "))
        usuarios[user_nuevo] = {
            "contrasena" : cont_nueva,
             "edad" : edad_nueva
            }
    
    user_nuevo = input("ingresa el nuevo nombre de usuario: ")


print(usuarios.keys())

