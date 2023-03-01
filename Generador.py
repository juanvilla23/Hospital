from Datos import *
import random
def TipoDeUrgencia():
   Color=random.choice(Triaje)
   return Color

def DarNombre():
   Sexo=random.choice(Genero)
   cantidad=[1,2]
   cantidad=random.choice(cantidad)
   if Sexo=="Mujeres" and cantidad==1:
      nombre=random.choice(NombresMujeres)
      apellido=random.choice(Apellidos)
      apellido2=random.choice(Apellidos)
      return f"{nombre} {apellido} {apellido2}"
   if Sexo=="Mujer" and cantidad==2:
      nombre=random.choice(NombresMujeres)
      nombre2=random.choice(NombresMujeres)
      apellido=random.choice(Apellidos)
      apellido2=random.choice(Apellidos)
      return f"{nombre} {nombre2} {apellido} {apellido2}"
   if Sexo=="Hombre" and cantidad==1:
      nombre = random.choice(NombreHombres)
      apellido = random.choice(Apellidos)
      apellido2 = random.choice(Apellidos)
      return f"{nombre} {apellido} {apellido2}"
   else:
      nombre=random.choice(NombreHombres)
      nombre2=random.choice(NombreHombres)
      apellido = random.choice(Apellidos)
      apellido2 = random.choice(Apellidos)
      return f"{nombre} {nombre2} {apellido} {apellido2}"
def DarPredianostico(color):
   if color!="Rojo" and color!="Naranja":
      minutos=[16,17,18,19,20,21,22,23,24,25,25,25,20,20]
   else:
      minutos=[4,5,6,7,8,9,10]
   return random.choice(minutos)
def DarExamenesLaboratorio(color):
   if color=="Rojo"or color=="Naranja":
      minutos=[3,4,5,6,7,8,9,10]
   else:
      minutos=[5,6,7,8,9,10,11,12,13,14,15]
   return random.choice(minutos)
def DarTratamiento(color):
   if color=="Rojo"or color=="Naranja":
      minutos=[1440,1380,1320,1260,1200,2880,2820,2760,2700,2640,2580,2520,4320,7200]
   else:
      minutos=[0,1440,280,290,300,310,320,330,340,350,360,
               370,380,390,400,410,420,430,440,450,460,
               470,480,490,500,510,520,530,540,550,560,
               570,580,590,600,610,620,630,640,650,660,670,
               680,690,700,710,720]
   return random.choice(minutos)








