import random
import time
import math
#delimitamos las variables para no salirnos de los rangos del problema 
n_cromosomas = 7
n_parejas = 20
max_peso = 30
tot_ob= 7 

#diccionario con todos los productos que pueden llevar los hermanos, tambien este es el orden en el arreglo para acceder a ellos 
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
			#para garantizar que la primera generacion cumpla con la condicion de >= 3 love_potion && skiving_snackbox >= 2
			if j == 1:
				padre[i][j] = random.randint(3,tot_ob)	
				madre[i][j] = random.randint(3,tot_ob)				
			elif j == 2:
				padre[i][j] = random.randint(2,tot_ob)	
				madre[i][j] = random.randint(2,tot_ob)
			else:
				padre[i][j] = random.randint(0,tot_ob)	
				madre[i][j] = random.randint(0,tot_ob) 
	return padre, madre


def mutacion(hijos):
	for i in range(n_parejas):
		if random.random() < .1: #probabilidad de alterar un gen del .1 o 10%
			j = random.randint(0, n_cromosomas -1) #seleccionamos un cromosoma al azar
			if j == 1:
				hijos[i][j] = random.randint(3,tot_ob) #para cumplir que se deben de llevar al menos 3 love_potion
			elif j == 2:
				hijos[i][j] = random.randint(2,tot_ob) #para cumplir que se deben de llevar al menos 2 skiving_snackbox
			else:
				hijos[i][j] = random.randint(1,tot_ob)
	return hijos


if __name__ == '__main__':
	padres, madres = primera_gen() 	
	padres = mutacion(padres)
	madres = mutacion(madres)
	print(f"Padres {padres} \n")
	print(f"madres {madres} \n")