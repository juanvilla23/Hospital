
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
def training():
    #entrenando datos para convertir de celcius a fahrenheit
    #Procedemos a crear nuestra red neuronal
    condiciones=np.array([[100,25,5,70],  [150,25,5,70], [200,25,5,70], [200,35,3,80],[140,35,3,80],[140,35,7,80],[140,35,15,70]],dtype=int)#valores de entrada
    salida=np.array([5,                     17,             44,            34,         29,           12,             0],dtype=int)#valores de salida
    capa=tf.keras.layers.Dense(units=1,input_shape=[4])
    #units: Representa el numero de nuuronas de salida
    #input_shape:cantidad de neuronas de entrada
    #Dense:cada neurona se conecta con todas las neuronas de la siguiente capa
    # Modelo: el modelo lo trabajaremos de forma secuencial
    modelo = tf.keras.Sequential([capa])
    #una vez creada nuestra red neuronal la compilamos
    modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1),loss="mean_squared_error")
    #adam: ayudara a la red a que mejore a medida que vaya evaluando varias varibales
    #Indicamos la función de perdida (loss):
    #"mean_squared_error"->error cuadratico medio->sigbifica que es mejor una gran cantidad de errores pequeños
    historial=modelo.fit(condiciones,salida,epochs=1000,verbose=False)
    modelo.save("saved_model/my_model")
    condiciones=[300,30,5,60]
    print(f"Con {condiciones[0]} pacientes, {condiciones[1]} doctores atendiendo en prediagnóstico,{condiciones[2]} doctores atendiendo en los examenes de laboratorio y"
          f" {condiciones[3]} camas en disposición en tratamiento,\nhay una probabilidad de que mueran {int(modelo.predict([condiciones]))} pacientes")
    return modelo
training()
