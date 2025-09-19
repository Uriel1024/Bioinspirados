import random
import time
import math
#delimitamos las variables para no salirnos de los rangos del problema 
n_cromosomas = 7
n_parejas = 20
max_peso = 30
tot_ob= 5

#diccionario con todos los productos que pueden llevar los hermanos, tambien este es el orden en el arreglo para acceder a ellos 
productos = {
	"dulces" : ["decoy_detonators" ,"love_potion", "extendable_ears" ,"skiving_snackbox" ,"fever_fudge", "puking_pastilles","nosebleed_nougat"],	
	"peso":[4,2,5,5,2,1.5,1],
	"ganancia":[10,8,12,6,3,2,2]
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

#para validar que los hijos tengan un peso <= 30
def validar(hijos):
	for i in range(n_parejas):
		total_peso = calc_peso(hijos[i])
		if total_peso > max_peso:
			hijos[i] = bajar_peso(hijos[i])
	return hijos


def calc_peso(hijo):
	total = 0
	for j in range(n_cromosomas):
		total += productos["peso"][j] * hijo[j] 
	return total

def bajar_peso(hijo):
	m_peso = calc_peso(hijo)
	while m_peso > max_peso:	
		cromo = random.randint(0, n_cromosomas - 1)
		if cromo == 1 and (hijo[1] < 3):
			continue  
		elif cromo == 2 and (hijo[2] < 2):
			continue
		elif hijo[cromo] > 0:
			hijo[cromo] -= 1
		m_peso = calc_peso(hijo)
	return hijo


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
	padres_1 = validar(padres)
	madres_1 = validar(madres)
	print(f"Los padres que cumplen la condicion:{padres_1}\n")
	print(f"las madres que cumplen la condicion:{madres_1}\n")
