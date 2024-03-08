#Calculadora con 4 metodos y parametros con decimales
#Queremos usar type() para ver como Python decide los tipos en base a los valores de inicialización que le damos

class Calculadora:
    #def __init__(self): ESTE SERIA, COMO EN JAVA, EL CONSTRUCTOR DE LA CLASE POR DEFECTO, QUE ESTÁ IMPLICITO
        #self.num1 = 0
        #self.num2 = 0
        #self.operator = "" '''
    def pedir_usuario(self):
        self.num1 = float(input("Dime un numero: "))  # Convertido a float para permitir decimales
        self.num2 = float(input("Dime otro numero: "))
        self.operator = input("Dime qué quieres hacer con dichos números (+, -, *, /): ")

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multip(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            return "Error! División por 0"
        else:
            return self.num1 / self.num2

    def calcular(self):
        if self.operator == "+":
            resu = self.suma()
        elif self.operator == "-":
            resu = self.resta()
        elif self.operator == "*":
            resu = self.multip()
        elif self.operator == "/":
            resu = self.div()
        else:
            resu = "Operador no válido, inténtelo de nuevo"
        print("El resultado es:", resu)
        print("El tipo de resultado es:", type(resu))

# Crear una instancia de la calculadora
miCalculadora = Calculadora()

# Solicitar al usuario los valores y la oper.
miCalculadora.pedir_usuario()

# Realizar el cálculo y mostrar el resultado
miCalculadora.calcular()
