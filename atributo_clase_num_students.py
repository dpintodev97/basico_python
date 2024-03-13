
# Definir un atributo de clase num_students y incrementarlo al crear objetos
class Student:
    #ATRIBUTO DE CLASE COMÚN A TODOS LOS OBJETOS/INSTANCIAS QUE SE CREAN A PARTIR DE ESTA CLASE:
    num_students = 0

    def __init__(self, n, e):    #METODO DE INICIALIZACION DEL OBJETO; PARA CREAR INSTANCIAS DE Student
    # ATRIBUTOS DEL CONSTRUCTOR AL CREAR UN NUEVO ESTUDIANTE:
        #self.nombre = nombre
        #self.edad = edad
        self.constructor_n = n
        self.constructor_e = e
    #ASEGURARME DE QUE INCREMENTA EL NUM DE ESTUDIANTES CADA VEZ QUE CREO UNA INSTANCIA NUEVA:
        Student.num_students += 1

#CREAR 2 ESTUDIANTES:
st1 = Student("Juan",25)
st2 = Student("Yolanda",26)
print("nºStudents: " + str(Student.num_students))
print("Students: " + st1.constructor_n + ", " + str(st1.constructor_e) + ", " + st2.constructor_n + ", " + str(st2.constructor_e))
