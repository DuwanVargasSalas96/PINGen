# -*-coding: UTF-8 -*-

#Importar
import os
from random import randint as rnd


#Limpiar
def limpiar():
	#Condicional Clear
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")


#Funcion para generar clave
def pinGen():
	#Declarar
	clave = []
	
	#Loop
	for i in range(4):
		#Random
		clave.append(rnd(0, 9))
	
	#Retonro
	return clave


#Menu
def main():
	#Loop
	while True:
		#Limpiar
		limpiar()
		
		#Menú
		print("PINGen\n")
		print("1. Generar PIN.")
		print("2. Salir.")
		
		#Capturar
		option = str(input("Su opción es: "))
		
		if option == "1":
			#Limpiar
			limpiar()
			
			#Imprimir
			print("PINGen\n")
			
			#KeyGen
			print("Su PIN automatico es: " + str(pinGen()) + "\n")
			input("Presione la tecla Enter regresar al menú.")
			
			#Retorno
			main()
		elif option == "2":
			#Limpiar
			limpiar()
			
			#Salida
			quit()
		else:
			#Imprimir
			input("Opción incorrecta! Intente nuevamente.")

#Linea de ejecucion
main()
