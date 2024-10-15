#==================================
#   Jimenez Gallegos Ivan
#==================================
#   Paradigmas dee Programacion
#   Matemática Algoritmica
#   ESFM-IPN    sept-2025
#===================================

#====================================
#   Programacion orientada a objetos
#====================================

#==================================
#   Una clase para un ibjeto vacio 
#   No esta tan vacio, necesita
#   la palabra pass = pasar
#===================================
class ObjetoVacio:
    pass

#====================================================
#   Nada es la instanciacion de la clase ObjetoVacio
#====================================================
nada = ObjetoVacio
print(type(nada))

#==================
#   La clas llanta
#==================
class Llanta:
    #========================================
    #   Variable cuenta es de toda la clase
    #========================================
    cuenta = 0
    #===========================================
    #   Funcion constructora de identidad 
    #   __init__ es la funcion reservada 
    #   comienza con uno mismo: self
    #   pero puede ser otro nombre (mi)
    #   parametros de entrada = default
    #===========================================
    def __init__(mi,radio=50,ancho=30,presion=1.5):
        #   Variable de la estructura completa Llanta
        Llanta.cuenta += 1
        #   variable exclusiva de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#==========================
#   Objetos (instanciados)
#==========================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion=1.2)
llanta3 = Llanta() 
llanta4 = Llanta(40,30,1.6)

#=====================================
#   Objeto que contiene otros onjetos
#=====================================
class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1,llanta2,llanta3,llanta4)

print ("Total de llantas: ",Llanta.cuenta)  # Variable global de la clase
print ("Presion de la llanta 4 = ",llanta4.presion) # Presion de la llanta 4
print ("Radio de la llanta 4 = ",llanta4.radio)
print ("Radio de la llanta 3 = ",llanta3.radio)
print ("Presion de la llanta 1 de mi coche = ", micoche.llanta1.presion)

#===================
#   Encapsulamiento
#===================

#===================================================
#   Uso de la funcion de python property y obtener
#   atributos a variables protegidas con __
#===================================================
class Estudiante:
    def __init__(mi):
        mi.__nombre = ""
    def ponerme_nombre(mi, nombre):
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print ("Se llamo al obtener_nombre")
        return mi.__nombre
    nombre=property(obtener_nombre,ponerme_nombre)

#======================================
#   Crear objeto estudiante sin nombre
#======================================
estudiante = Estudiante()

#========================================================================
#   Ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre
#   (sin tener que llamar explicitamente la funcion
#========================================================================
estudiante.nombre = "Ivan"

#========================================================================
#   Ontener el nombre con el metoso obtener_nombre                      
#   __nombre es la variable encapsulada (no visible desde fuera)
#   (sin tener que llamar explicitamente a la funcion obtener_nombre)
#========================================================================
print(estudiante.nombre)

#   Esto no funciona
#   print(estudiante.__nombre)

#========================
#   Herencia de clases
#========================
class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

        def perimetro(mi):
            p=mi.lado1+mi.lado2+mi.lado3+mi.lado4
            print("Perimetro = ",p)
            return p

#=======================================                                 
#   Su hijo rectangulo                                                  
#   Rectangulo es hijo de caudrilatero             
#   Rectangulo(Cuadrilatero)
#=======================================
class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        #===============================
        #   Constructir de su madre
        #===============================
        super().__init(a, b, a, b)

#============================
#   Su nieto Cuadrado
#   Hijo de Rectangulo
#============================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area

    #def perimetro (self):
    #   p = 4.0*self.lado1
    #   print("Perimetro = ",p)
    #   return p

#====================
#   Crear cuadrado
#====================
cuadrado1 = Cuadrado(5)

#=========================================================
#   Llamar al metodo perimetri de su abuelo Cuadrilatero
#=========================================================
perimetro1 = cuadrado.perimetro()

#===================================
#   Llamar a su propio metodo area
#===================================
area1 = cuadrado1.area()     

print("Perimetro = ", perimetro1)
print("Area = ", area1)

#=================================================================
#   Sobre-escribir un metodo de su madre o abuela o tatarabuela...
#   Es volver a definir una funcion ya existente
#=================================================================
