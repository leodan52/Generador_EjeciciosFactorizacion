# Descripcion

def Div_all(lista,num):
	
	for i in lista:
		if i == 0:
			continue
		if i % num != 0:
			return False
			
	return True
	
def Div(lista,num):
	for i in lista:
		if i == 0:
			continue
		if i % num == 0:
			return True
			
	return False
	
def if_ones(lista):
	for i in lista:
		if i != 1:
			return False
			
	return True

class F_prima:
	
	def __init__(self,*arg):
		
		self.nums = list(arg)
		
		self.Primos()
		self.Factorizacion()
		self.F_mcm()
		self.F_MCD()
	
	def Primos(self):
		
		entrada = open("TOOLS/Estos_son_primos.txt", "r")
		aux = entrada.readline().strip().split(" ")	
		entrada.close()
		self.primos = []
		
		for i in aux:
			self.primos.append(eval(i))
	
	def Factorizacion(self):
		
		self.f_prima = []
		self.all_f_prima = []
		lista = self.nums.copy()
		
		for i in self.primos:
			while Div(lista,i):
				self.f_prima.append(i)
				if Div_all(lista,i):
					self.all_f_prima.append(i)
					
				for j in range(len(lista)):
					if lista[j] % i == 0:
						lista[j] = lista[j]//i
						
			if if_ones(lista):
				break
						
	def F_mcm(self):
		self.mcm = 1
		
		for i in self.f_prima:
			self.mcm *= i
			
	def F_MCD(self):
		self.MCD = 1
		
		for i in self.all_f_prima:
			self.MCD *= i
		
