class Fraccion:
    '''
    La clase representa a una Fraccion con un numerador y un denominador
    '''
	def __init__(self, numerador, denominador):
		self.num = numerador
		self.den = denominador
        if denominador == 0:
            raise ZeroDivisionError("No se puede dividir por 0")

	def __mul__(self, otra):
		nuevo_numerador = self.num*otra.num
		nuevo_denominador = self.den*otra.den
		return Fraccion(nuevo_numerador, nuevo_denominador)
