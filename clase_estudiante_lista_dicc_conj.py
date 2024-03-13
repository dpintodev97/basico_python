#Definir una clase estudiante, crear varios estudiantes y meterlos en una lista

class Estudiante:   #DEFINE LA CLASE
#1. CONSTRUCTOR DE CLASE (NO POR DEFECTO) YA QUE QUIERO PASARLE X PARAM. AL CREAR ESTUDIANTES:
    def __init__(self, param1, param2):
        # ATRIBUTOS DEL CONSTRUCTOR AL CREAR UN NUEVO ESTUDIANTE
        self.nombre = param1 #NO HACE FALTA DESPUES DEL self.nombre ESCRIBIR UN = nombre COMO EN JAVA;
                    # YA QUE PYTHON YA ENTIENDE QUE ESTAMOS CREANDO EL ATRIBUTO, NO HACE FALTA DEFINIRLO EN EL CONSTR.
        self.edad = param2
#IMPORTANTE: param1, param2 DURARÁN EN EL TIEMPO SOLO DURANTE LA CONSTRUCCION DEL OBJETO;
            # UNA VEZ CREADO EL OBJETO, DURARÁ EN EL TIEMPO LOS ATRIBUTOS DE CLASE, nombre, edad

#2. PEDIR AL USUARIO LOS ESTUDIANTES QU QUIERE METER (SI NO QUIERO ESO Y SOLO QUIERO YO IR CREANDOMELOS, PUES SOLO CREAMOS
#estudiante1 = Estudiante("Juan", 20); estudiante2 = Estudiante . . .
    def meter_estudiantes(self):
        print("Dime el nombre y la edad del estudiante a introducir: ")
        self.nombre = input("Nombre?: ")
        self.edad = input("Edad?: ")
        return Estudiante

#3. CREAR LISTA VACÍA PARA IR GUARDANDO LOS ESTUDIANTES; O USAR UN DICCIONARIO, VEREMOS AMBAS
#NOTA: DICCIONARIOS EN PYTHON ES COMO EL HASH MAP EN JAVA (EST.DATOS); SE USA MUCHÍSIMO:
#DIFERENCIAS: LISTA: ÚTIL SI QUIERO EL ORDEN DE LOS ELEMENTOS, YA QUE ACCEDO POR INDICE; PERO ADMITE DUPLICADOS
#             DICCIONARIO: CLAVE-VALOR, ACCEDO A LOS VALORES A TRAVES DE LAS KEYS; IMPOSIBLE QUE ADMITA DUPLICADOS
lista_estudiantes = []   #<----------------------------LISTA

#4.PEDIR AL USUARIO CUÁNTO ESTUDIANTES QUIERO METER:
num_estudiantes = int(input("Cuántos estudiantes incorporarás?: "))

#5. DETALLES DEL ESTUDIANTE NUEVO A METER:
nuevo_estudiante = Estudiante.meter_estudiantes()

#6. GUARDO LOS OBJETOS EST. EN LA LISTA E IMPRIMO LA LISTA:
print(lista_estudiantes.append(nuevo_estudiante))






