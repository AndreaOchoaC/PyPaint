'''def lluvia():
    lluvia = input("está lloviendo?")
    if lluvia == "si":
        print("usa un paraguas")
    else:
        print("no necesitas paraguas")
        




def dia():
    dia = input("que dia es hoy?")
    if dia == "lunes" or dia == "martes":
        print("hoy tienes clase de python")
    elif dia == "miércoles":
        print("hoy tienes clase de guitarra")
    else:
        print("hoy tienes la tarde libre")


def calificacion():
    calif_M = int(input("dame tu calificacion de matematicas"))
    calif_C = int(input("dame tu calificacion de ciencias"))
    if calif_M >= 6 and calif_C >= 6:
        print("muy bien, puedes ir al cine")
    else:
        if calif_M >= 6 or calif_C >= 6:
            print("bien")
        else:
            print("castigada")



python = ["juan", "pepe", "lisa", "ana", "sara"]
roblox = ["nico", "diego", "juan", "sara", "josé"]



def alumnos():
    alumno = input("dime el nombre del alumno")
    alumno = alumno.lower()
    if alumno in python and alumno in roblox:
        print("estudie más")
    elif alumno in python or alumno in roblox:
        print("el alumno está inscrito")
    else:
        print("inscriba al alumno")
    if alumno in python:
        print("tienes tarea")
    if alumno in roblox:
        print("revisa tu proyecto")

    return alumno

def suma():
    num1 = int(input("dame 1 numero"))
    num2 = int(input("dame el segundo numero"))
    num3 = int(input("dame el 3er numero"))
    suma = num1 + num2 + num3
    
    return suma





def lluvia2(lluvia):
    if lluvia == "si":
        print("usa un paraguas")
    else:
        print("no necesitas paraguas")

lluvia2("si")
lluvia2("no")



python = ["juan", "pepe", "lisa", "ana", "sara"]
roblox = ["nico", "diego", "juan", "sara", "josé"]



def alumnos2(alumno):

    print(alumno)

    if alumno in python and alumno in roblox:
        print("estudie más")
    elif alumno in python or alumno in roblox:
        print("el alumno está inscrito")
    else:
        print("inscriba al alumno")
    if alumno in python:
        print("tienes tarea")
    if alumno in roblox:
        print("revisa tu proyecto")

    return alumno


def suma2(num1, num2, num3):
    suma = num1 + num2 + num3
    
    return suma

a = suma2(3,6,9)
print(a)
'''



class mascotas():
    def __init__(self, nombre, especie, edad, actividad, juguete):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.actividad = actividad
        self.tienda = "petco"
        self.juguete = juguete

    def datos(self):
        print("Los datos de tu mascota son: ")
        print(self.nombre, self.especie, self.edad, self.actividad, self.tienda)
    
    def jugar(self):
        print(self.nombre, "está jugando con", self.juguete)

    def comer(self,comida):
        print(self.nombre, "está comiendo", comida)

    def urgencia(self,urgencia):
        print(self.nombre)
        if urgencia == "chequeo":
            print("Agenda un chequeo general para ver su estado de salud")
        elif urgencia == "accidente":
            print("es necesario traer a", self.nombre, "a la clínica")
        elif urgencia == "enfermedad":
            print("trae a", self.nombre, "para darle tratamiento")
        else:
            print("bien,", self.nombre, "se encuentra sano") 

    def interactuar(self,amigo):
        print(self.nombre, "está jugando con", amigo.nombre)
        print(self.nombre, "lo invita a jugar con", amigo.juguete)
        if self.especie == amigo.especie:
            print("pueden comer la misma comida")
        else:
            print("cada quien come su alimento")

    def f_edad(self):
        if self.edad <= 5:
            print(self.nombre, "aún es joven")
        elif self.edad >= 8 and self.edad <= 9:
            print(self.nombre, "ya es adolescente")
        elif self.edad >= 10:
            print(self.nombre, "ya es mayor")


sky = mascotas("Sky", "gato", 8 , "jugar con pelotas", "pelota de unicel")
sky.datos()
sky.jugar()

reo = mascotas("Reo", "camaleón", 5 , "copiar colores y movimientos", "balón pequeño")
reo.datos()
reo.jugar()

misha = mascotas("Misha", "gato", 10 , "dormir", "ratón de tela")
misha.datos()
misha.jugar()


'''reo.comer("plantas")
reo.comer("palitos")'''

'''sky.comer("croquetas")
sky.comer("pollo")

reo.interactuar(sky)
misha.interactuar(sky)

sky.f_edad()
reo.f_edad()
misha.f_edad()'''

class gato(mascotas):
   def __init__(self, nombre, especie, edad, actividad, juguete):
       super().__init__(nombre, especie, edad, actividad, juguete)
       self.especie = "gato"

   def maullar(self):
       print("miau")
   def acicalar(self):
       print("limpiarse")

bigotes = gato("bigotes", "gato", 6, "comer", "juguete")

print(bigotes.datos())
       

bigotes.maullar()

class perro(mascotas):
   def __init__(self, nombre, especie, edad, actividad, juguete):
       super().__init__(nombre, especie, edad, actividad, juguete)
       self.especie = "perro"

   def ladrar(self):
       print("woof")
   def jugar(self):
       print(self.nombre, "está jugando")

kiro = perro("Kiro", "perro", 7, "correr", "juguete")

print(kiro.datos())

print(kiro.ladrar())

print(kiro.jugar())