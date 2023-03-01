from random import *
from Generador import *
class Paciente():
    Contador_Pacientes=0
    def __init__(self):
        Paciente.Contador_Pacientes=Paciente.Contador_Pacientes+1
        self._NEntrada= Paciente.Contador_Pacientes
        self._Nombre=DarNombre()
        self._TriajeClasificación=TipoDeUrgencia() #tiene metodos de get y set
        self._TiempodeEsperaEntrada=0   #tienen metodos de get y set
        self._Prediagnostico=0 #tiene metodos de get y set
        self._TiempoPre=0 #tiene metodos get y set
        self._ExamenesLaboratorio=0 #tiene metodos de get y set
        self._TiempoLab=0 #tiene metodos get y set
        self._Tratamiento=0 #tiene metodos de get set
        self._TiempoTra=0 #tiene metodos get y set
        self._Nivel=0 #tiene una funcion
        self._Estado= "Tratamiento"

    def __str__(self):
        return f"Paciente: {self._Nombre}/ Triaje: {self._TriajeClasificación}/ Nivel: {self._Nivel} " \
               f"/Tiempo-Entrada: {self._TiempodeEsperaEntrada} Minutos /Tiempo para entrar al Prediagnóstico: {self._TiempoPre} minutos/Tiempo-Examenes:{self._TiempoLab} minutos" \
               f"/Tiempo para Tratamiento: {self._TiempoTra} minutos/ El tiempo que estuvo en el hospital(Espera): {self._TiempodeEsperaEntrada+self._TiempoPre+self._TiempoLab+self._TiempoTra}" \
               f"/Estado: {self._Estado}"

    #Tiempo en la entrada
    @property
    def TiempoEsperaEntrada(self):
        return self._TiempodeEsperaEntrada
    @TiempoEsperaEntrada.setter
    def TiempoEsperaEntrada(self,Tiempo):
        self._TiempodeEsperaEntrada=Tiempo
    #Prediagnostico
    @property
    def Prediagnostico(self):
        return self._Prediagnostico
    @Prediagnostico.setter
    def Prediagnostico(self,prediacnostico):
        self._Prediagnostico=prediacnostico
    #Tiempo antes del Predianostico
    @property
    def TiempoPre(self):
        return self._TiempoPre
    @TiempoPre.setter
    def TiempoPre(self,tiempo):
        self._TiempoPre=tiempo

    @property
    def TriajeClasificacion(self):
        return self._TriajeClasificación
    @TriajeClasificacion.setter
    def TriajeClasificacion(self,Triaje):
        self._TriajeClasificación=Triaje

    @property
    def ExamenesLaboratorio(self):
        return self._ExamenesLaboratorio
    @ExamenesLaboratorio.setter
    def ExamenesLaboratorio(self,examenes):
        self._ExamenesLaboratorio=examenes
    @property
    def TiempoLab(self):
        return self._TiempoLab
    @TiempoLab.setter
    def TiempoLab(self,tiempo):
         self._TiempoLab=tiempo
    @property
    def Tratamiento(self):
        return self._Tratamiento
    @Tratamiento.setter
    def Tratamiento(self,tratamiento):
        self._Tratamiento=tratamiento
    @property
    def TiempoTra(self):
        return self._TiempoTra
    @TiempoTra.setter
    def TiempoTra(self,tiempoTra):
        self._TiempoTra=tiempoTra
    @property
    def Estado(self):
        return self._Estado
    @Estado.setter
    def Estado(self,estado):
        self._Estado=estado
    #Metodos de Comparacion
    def __gt__(self, other):#mayor
        return self._Nivel>other._Nivel
    def __lt__(self, other):#menor
        return self._Nivel<other._Nivel
    #Asignacion del nivel
    def Nivel(self):
        colores={"Rojo":1,"Naranja":2,"Amarillo":3,"Verde":4,"Azul":5}
        self._Nivel = colores.pop(self._TriajeClasificación)



def GeneradorPacientes(NPacientes:int):#NPaciente: numero de pacinetes que iran al hospital
    Pacientes=[]
    for i in range(NPacientes):
       persona=Paciente()
       Pacientes.append(persona)
    return Pacientes
def VerPacientes(Pacientes:list):#Pacientes:lista de pacientes
    i=1
    for Paciente in Pacientes:
      print(f"({i}) {Paciente}")
      i=i+1
if __name__=="__main__":
    pass
