#Calculadora con 4 metodos y parametros con enteros
#Queremos usar type() para ver como Python decide los tipos en base a los valores de inicialización que le damos

class Calculadora(): #CLASE: EN PYTHON SE USAN PARA AGRUPAR FUNCIONES Y VARIABLES RELACIONADAS
    def pedir_usuario(self): #PEDIR AL USUARIO QUÉ HACER
        self.num1 = int(input("Dime un numero: ")) #PIDE AL USUARIO EL PRIMER NUMERO Y LO GUARDA EN LA VARIABLE num1 DEL OBJETO ACTUAL
        #FUNCION input() PARA RECIBIR LA ENTRADA DEL USER; E int() PARA CONVERTIRLO A ENTERO.
        self.num2 = int(input("Dime otro numero: "))
        self.operator = (input("Dime qué quieres hacer con dichos números: "))

    #************** METODOS DE CLASE (OPERACIONES MATEMATICAS BASICAS): ***********************
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2
    def multip(self):
        return self.num1*self.num2
    def div(self):
        if self.num2 == 0:
            return "Error! division por 0"
        else:
            return self.num1/self.num2
    def calcular(self):
        if self.operator == "+":
            resu = self.suma()
        elif self.operator=="-":
            resu = self.resta()
        elif self.operator=="-":
            resu = self.resta()
        elif self.operator=="*":
            resu = self.multip()
        elif self.operator=="/":
            resu = self.div()
        else:
            resu = "Operador no válido, inténtelo de nuevo"
        print("El resultado es: ", resu)
        print("El tipo de resultado es: ", type(resu)) #type() DEVOLVERÁ EL TIPO DE DATO, YA SEA ENTERO, FLOAT, STRING

#********************    USO DE LA CALCULADORA:   **************

# 1. CREA UNA INSTANCIA (OBJETO) DE LA CLASE CALCULADORA. PARA HACERLO, SE LLAMA AL CONSTRUCTOR DE LA CLASE,
# QUE ES EL MÉTODO __init__() AUNQUE NO ESTÉ EXPLÍCITAMENTE DEFINIDO. ESTO CREA UN NUEVO OBJETO CALCULADORA QUE PUEDE USAR
# TODOS LOS MÉTODOS Y ATRIBUTOS DEFINIDOS EN LA CLASE
miCalculadora = Calculadora()

# 2.DESPUÉS DE CREAR EL OBJETO MICALCULADORA, LLAMA AL MÉTODO PEDIR_USUARIO() DE ESTE OBJETO. SOLICITA AL USUARIO QUE INGRESE DOS NÚM Y LA OPER.,
# Y ALMACENA ESTOS VALORES EN LOS ATRIBUTOS DEL OBJETO MICALCULADORA:
miCalculadora.pedir_usuario()

# 3.FINALMENTE,LLAMA AL MÉTODO CALCULAR() DEL OBJETO MICALCULADORA. DETERMINA QUÉ OPERACIÓN SE VA A REALIZAR SEGÚN EL VALOR DE OPERATOR,
# LUEGO LLAMA AL MÉTODO CORRESPONDIENTE (SUMA, RESTA, MULTIP O DIV) Y MUESTRA EL RESULTADO DE LA OPERACIÓN JUNTO CON SU TIPO UTILIZANDO LA FUNCIÓN PRINT().
miCalculadora.calcular()














