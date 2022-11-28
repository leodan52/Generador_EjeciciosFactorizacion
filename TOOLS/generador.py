# Descripcion

from random import randint
import math
from TOOLS.primos import *

def dividir(lista,divisor):
	for i in range(len(lista)):
		lista[i] = lista[i]//divisor

class Factoriza:
	
	def __init__(self,ID):
		
		loop = ""
		
		self.ID = ID
		self.maximo = 200
		self.Cuadrados()
		
		n = 0
		while loop != "s":
			self.a = randint(1,self.maximo)
			self.b = randint(-self.maximo,self.maximo)
			self.c = randint(-self.maximo,self.maximo)
			
			n += 1
			
			if self.b == 0 and self.c == 0:
				continue
		
			self.discr = self.b**2 - 4*self.a*self.c
			
			if self.discr < 0 or self.discr not in self.cuadrados:
				continue
			
			cal_mas = -self.b + math.sqrt(self.discr)
			cal_menos = -self.b - math	.sqrt(self.discr)
			
			if cal_mas % 2*self.a != 0 and cal_mas % 2*self.a != 0:
				continue
			
			self.Trinomio()
			
			if self.discr == 0:
				self.tipo = "Trinomio cuadrado perfecto"
				break
			
			self.factor = F_prima(*self.trinomio)
			
			if self.b == 0:
				dividir(self.trinomio,self.factor.MCD)
				self.tipo = "Diferecia de cuadrados"
				break
				
			if self.c == 0:
				self.tipo = "Factor común"
			else:
				self.tipo = "Trinomio regular"
				
			if self.c == 0 and self.factor.MCD == 1:
				continue
			elif self.c == 0 and self.factor.MCD != 1:
				break
			
			if self.a == 1:
				break
				
			if self.factor.MCD == 1:
				continue
			
			aux = self.trinomio.copy()
			
			dividir(aux,self.factor.MCD)
			
			if aux[0] != 1:
				continue
				
			loop = "s"
			
		print("Intentos: ", n)
		print("Check ", self.ID)
		self.imprimir()
	
	def Cuadrados(self):
		self.cuadrados = []
		
		for i in range(self.maximo + 1):
			self.cuadrados.append(i**2)
			
			
	def Trinomio(self):
		
		self.trinomio = [self.a, self.b, self.c]
		
	def imprimir(self):
		self.impr = self.trinomio.copy()
		
		if self.impr[0] == 1:
			self.impr[0] = "x^2"
		else:
			self.impr[0] = str(self.impr[0]) + "x^2"
			
		for i in range(len(self.impr)):
			if type(self.impr[i]) == str:
				continue
				
			if self.impr[i] == 0:
				self.impr[i] = ""
				continue
				
			aux = ""
			
			if self.impr[i] > 0:
				aux = "+"
				
			if abs(self.impr[i]) == 1 and i == 1:
				self.impr[i] = aux + str(self.impr[i]).replace("1","")
			else:
				self.impr[i] = aux + str(self.impr[i])
				
			if i == 1:
				self.impr[i] = self.impr[i] + "x"
		
		self.impr = "".join(self.impr) + " = 0"
