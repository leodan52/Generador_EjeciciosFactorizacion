# Descripcion

from TOOLS.generador import *


def main():
	
	num_e = 1000
	descartados = 0
	
	ejercicios = {"Factor común": [], "Trinomio cuadrado perfecto": [], "Diferecia de cuadrados": [], "Trinomio regular": []}
	
	for i in range(num_e):
		a = Factoriza(i)
		
		if checar_repetidos(a,ejercicios):
			ejercicios[a.tipo].append(a)
		else:
			print("Repetido")
			descartados += 1
			
	print()
	
	for i in ejercicios:
		print("De ", i, " hay ", len(ejercicios[i]), " ejercicios" )
		
	print("Descartados = ", descartados)
	print()
	input("Oprima enter para imprimir")
	
	for i in ejercicios:
		
		if ejercicios[i] == []:
			continue
			
		salida = open( i + ".txt", "w")
		
		for j in ejercicios[i]:
			print(j.impr, file=salida)
		salida.close()
		
def main2():
	
	a = Factoriza()
	
	print(a.trinomio)
	
	a.imprimir()
	
def checar_repetidos(a,dicc):
	
	for i in dicc[a.tipo]:
		if a.trinomio == i.trinomio:
			return False
			
	return True
	
main()
