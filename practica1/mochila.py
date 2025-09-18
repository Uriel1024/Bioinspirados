import random
import time
import math
#delimitamos las variables para no salirnos de los rangos del programa
n_cromosomas = 7
n_parejas = 20
max_peso = 30


#diccionario con todos los productos que pueden llevar los hermanos, tambien este es el orden el arreglo para acceder a ellos 
productos= {
	"decoy_detonators",
	"love_potion",
	"extendable_ears",
	"skiving_snackbox",
	"fever_fudge",
	"puking_pastilles",
	"nosebleed_nougat"
}



def primera_gen():
	padre = [[0 for _ in range(n_cromosomas)] for _ in range(n_parejas)]
	madre =	[[0 for _ in range(n_cromosomas)] for _ in range(n_parejas)]
	for i in range(n_parejas):
		for j in range(n_cromosomas):
			if padre [i][j] == padre
			padre[i][j] = random.randint(1,9)	
			madre[i][j] = random.randint(1,9) 
	return padre, madre

#def validar)(



if __name__ == '__main__':
	padres, madres = primera_gen() 	
	print(f"Padres {padres} \n")
	print(f"madres {madres} \n")