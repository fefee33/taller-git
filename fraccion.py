class Fraccion:
	def __init__(self, numerador, denominador):
		self.numerador = numerador
		self.denominador = denominador

	def __mul__(self, otra):
		nuevo_numerador = self.numerador*otra.numerador
		nuevo_denominador = self.denominador*otra.denominador
		return Fraccion(nuevo_numerador, nuevo_denominador)
