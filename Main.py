from Paciente import *
from Ordenamiento import *
from collections import deque
from queue import PriorityQueue
from Doctor import *


if __name__=="__main__":
    #NumeroPacientes = int(input("Cantidad de Pacientes que Ingresaron al Hospital: "))
    NumeroPacientes = 140
    Lista = GeneradorPacientes(NumeroPacientes)#Pacientes que Ingresaron al Hospital
    MinutosDeEspera=0
#-------------------------------Los pacientes son resgistrados y se les dara su prioridad-------------------------------
    for paciente in Lista:
        paciente.Nivel()
        paciente.TiempoEsperaEntrada=MinutosDeEspera
        MinutosDeEspera=MinutosDeEspera+2
        if MinutosDeEspera==10:
            MinutosDeEspera=0


#-------------------------------Ordenamos Los pacientes por nivel-------------------------------------------------------
ListaOrdenada=mergeSort(Lista)
#-------------------------------Luego los Ingresamos a una Fila---------------------------------------------------------
fila=deque()

for paciente in ListaOrdenada:
    fila.appendleft(paciente)
#---------------------------------Pasamos los Clientes a un Prediagnostico----------------------------------------------
print("Pasamos los Pacientes a prediagnóstico".center(100,"-"))
DoctoresDisponibles=PriorityQueue()
#------------------------------------Decidimos cuantos Doctores Tendra el hospital---------------------------------------
n=35
for i in range(n):
    DoctoresDisponibles.put(Doctor())
DoctoresOcupados=PriorityQueue()
while len(fila)!=0 :
    if DoctoresDisponibles.empty():
        for i in range(n):
            DoctoresDisponibles.put(DoctoresOcupados.get())
    else:
        doctor=DoctoresDisponibles.get()
        atentido=fila.pop()
        atentido.TiempoPre=doctor.Tiempo
        atentido.Prediagnostico=DarPredianostico(atentido.TriajeClasificacion)
        doctor.Tiempo=atentido.Prediagnostico
        DoctoresOcupados.put(doctor)
#Pasamos los Pacientes a los Examenes de Laboratorio
print("Pasamos los Pacientes a los Examenes de Laboratorio".center(100,"-"))
fila2=deque()
for paciente in ListaOrdenada:
    fila2.appendleft(paciente)

DoctoresDisponibles=PriorityQueue()
#------------------------------------Decidimos cuantos Doctores Tendran los laboratorios---------------------------------------
n1=15
for i in range(n1):
    DoctoresDisponibles.put(Doctor())
DoctoresOcupados=PriorityQueue()
while len(fila2)!=0 :
    if DoctoresDisponibles.empty():
        for i in range(n1):
            DoctoresDisponibles.put(DoctoresOcupados.get())
    else:
        doctor=DoctoresDisponibles.get()
        atentido=fila2.pop()
        atentido.TiempoLab=doctor.Tiempo
        atentido.ExamenesLaboratorio=DarExamenesLaboratorio(atentido.TriajeClasificacion)
        doctor.Tiempo=atentido.ExamenesLaboratorio
        DoctoresOcupados.put(doctor)
#---------------------------Pasamos los paciente a tratamiento--------------------------------------
print("Pasamos los paciente a tratamiento".center(100,"-"))
fila3=deque()
for paciente in ListaOrdenada:
    fila3.appendleft(paciente)

DoctoresDisponibles=PriorityQueue()
#------------------------------------Decidimos cuantos Doctores estaran en Urgencias---------------------------------------
n2=70
for i in range(n2):
    DoctoresDisponibles.put(Doctor())
DoctoresOcupados=PriorityQueue()
while len(fila3)!=0 :
    if DoctoresDisponibles.empty():
        for i in range(n2):
            DoctoresDisponibles.put(DoctoresOcupados.get())
    else:
        doctor=DoctoresDisponibles.get()
        atentido=fila3.pop()
        atentido.TiempoTra=doctor.Tiempo
        if 1000<atentido.TiempoTra<2000:
            atentido.TiempoTra=atentido.TiempoTra-200
        elif 2000<atentido.TiempoTra<3000:
            atentido.TiempoTra = atentido.TiempoTra - 1000
        elif 3000<atentido.TiempoTra<4000:
            atentido.TiempoTra = atentido.TiempoTra - 2000
        elif 4000<atentido.TiempoTra<5000:
            atentido.TiempoTra=atentido.TiempoTra - 3000
        elif 5000 < atentido.TiempoTra < 6000:
            atentido.TiempoTra = atentido.TiempoTra - 4000
        elif 6000 < atentido.TiempoTra < 7000:
            atentido.TiempoTra = atentido.TiempoTra - 5000
        elif 7000 < atentido.TiempoTra < 8000:
            atentido.TiempoTra = atentido.TiempoTra - 6000


        atentido.Tratamiento=DarTratamiento(atentido.TriajeClasificacion)
        doctor.Tiempo=atentido.Tratamiento
        DoctoresOcupados.put(doctor)

#------------------Procedemos a hacer el Analisis de los datos generados---------------------------------------------
#Analizar cuantas personas murieron por falta de condiciones
Riesgocantidad=0
RiesgoPacientes=[]
for paciente in ListaOrdenada:
    factores=paciente.TiempoEsperaEntrada+paciente.TiempoTra+paciente.TiempoLab+paciente.TiempoPre
    if paciente.TriajeClasificacion=="Rojo" and paciente.TiempoTra>20:
        paciente.Estado="Muerto"
        Riesgocantidad=Riesgocantidad+1
        RiesgoPacientes.append(paciente)
    if paciente.TriajeClasificacion=="Naranja" and paciente.TiempoTra>20:
        Riesgocantidad=Riesgocantidad+1
        paciente.Estado = "Muerto"
        RiesgoPacientes.append(paciente)
    if paciente.TriajeClasificacion=="Rojo" and factores>20:
        Riesgocantidad=Riesgocantidad+1
        paciente.Estado = "Muerto"
        RiesgoPacientes.append(paciente)
    if paciente.TriajeClasificacion=="Naranja" and factores>20:
        paciente.Estado = "Muerto"
        RiesgoPacientes.append(paciente)
if Riesgocantidad==0:
    print("En el hospital no muerieon pacientes")
else:
    print(f"En el Hospital {Riesgocantidad} muerieron por falta de condiciones")
#Prediagnostico-----------------------
Servicio=0
ServicioPacientes=[]
for paciente in ListaOrdenada:
    if paciente.TriajeClasificacion=="Rojo"and paciente.TiempoPre>2:
        Servicio=Servicio+1
        ServicioPacientes.append(paciente)
    if paciente.TriajeClasificacion=="Naranja" and paciente.TiempoPre>15:
        Servicio = Servicio + 1
        ServicioPacientes.append(paciente)
    if paciente.TriajeClasificacion == "Amarillo" and paciente.TiempoPre>40:
        Servicio = Servicio + 1
        ServicioPacientes.append(paciente)
    if paciente.TriajeClasificacion == "Verde" and paciente.TiempoPre > 160:
        Servicio = Servicio + 1
        ServicioPacientes.append(paciente)
    if paciente.TriajeClasificacion == "Azul" and paciente.TiempoPre > 260:
        servicio=Servicio+1
        ServicioPacientes.append(paciente)
print(f"En el tiempo prediagnóstico hubieron {Servicio} personas que esperaron mas de lo normal")

#Examenes laboratorio-------------------------------------------------
Servicio2=0
ServicioPacientes2=[]
for paciente in ListaOrdenada:
    if paciente.TriajeClasificacion=="Rojo"and paciente.TiempoLab>4:
        Servicio2=Servicio2+1
        ServicioPacientes2.append(paciente)
    if paciente.TriajeClasificacion=="Naranja" and paciente.TiempoLab>15:
        Servicio2 = Servicio2 + 1
        ServicioPacientes2.append(paciente)
    if paciente.TriajeClasificacion == "Amarillo" and paciente.TiempoLab>70:
        Servicio2 = Servicio2 + 1
        ServicioPacientes2.append(paciente)
    if paciente.TriajeClasificacion == "Verde" and paciente.TiempoLab > 180:
        Servicio2 = Servicio2 + 1
        ServicioPacientes2.append(paciente)
    if paciente.TriajeClasificacion == "Azul" and paciente.TiempoLab > 180:
        servicio2=Servicio2+1
        ServicioPacientes2.append(paciente)
print(f"En el  tiempo de los examenes de laboratorio hubieron {Servicio2} que esperaron mas de lo normal")
#Tratamiento----------------------------------------
Servicio3=0
ServicioPacientes3=[]
for paciente in ListaOrdenada:
    if paciente.TriajeClasificacion=="Rojo"and paciente.TiempoTra>1:
        Servicio3=Servicio3+1
        ServicioPacientes3.append(paciente)
    elif paciente.TriajeClasificacion=="Naranja" and paciente.TiempoTra>15:
        Servicio3=Servicio3+1
        ServicioPacientes3.append(paciente)
    elif paciente.TriajeClasificacion == "Amarillo" and paciente.TiempoTra>60:
        Servicio3=Servicio3+1
        ServicioPacientes3.append(paciente)
    elif paciente.TriajeClasificacion == "Verde" and paciente.TiempoTra > 360:
        Servicio3=Servicio3+1
        ServicioPacientes3.append(paciente)
    elif paciente.TriajeClasificacion == "Azul" and paciente.TiempoTra > 420:
        Servicio3=Servicio3+1
        ServicioPacientes3.append(paciente)
print(f"En el tiempo del tratamiento {Servicio3} esperaron  mas de lo normal para ser tratadas")
VerPacientes(ListaOrdenada)





































