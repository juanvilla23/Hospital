def mergeSort(datos:list):
    if len(datos) <=1:
        return datos
    if len(datos)==2:
        return sorted(datos)
    mitad=len(datos)//2
    return merge(mergeSort(datos[:mitad]),mergeSort(datos[mitad:]))

def merge(datosA,datosB):
    resultado=[]
    while(len(datosA)!=0 and len(datosB)!=0):
        if datosA[0]<datosB[0]:
            resultado.append(datosA[0])
            datosA.pop(0)
        else:
            resultado.append(datosB[0])
            datosB.pop(0)
    resultado=resultado+datosA+datosB
    return resultado