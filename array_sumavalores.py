
def suma_array(mi_array): #DEFINO LA FUNCION Y LE PASO COMO PARAMETRO mi_array
    resu = 0                #INICIALIZO resu EN 0
    for elemento in mi_array:    #BUCLE for: elemento ES COMO i EN JAVA (AQUI TAMBIEN LO PEUDO LLAMAR i); EN (in) mi_array
        if type(elemento == int and elemento == float): #COMO PARSE EN JAVA; QUE SI ENCUENTRA UN int O float LO SUME, QUE HAY string, NO LO SUME
          resu += elemento  #SUMA LOS ELEMENTOS Y LOS DEVOLVERÁ EN resu
    return resu

array = [2,5,9.76]
print(suma_array(array))

# AHORA, YA HAY UNA FUNCION DE SUMAR, ES LO MISMO:
#sumaValores = sum(array)  Funcion sum() QUE YA VIENE HECHA; LE PASO LOS PARAMETROS, array
#print("Array", array)
#print("Suma de los valores: ", sumaValores)
