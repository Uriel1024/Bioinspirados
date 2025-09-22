import random
import time
import math
import numpy as np
#delimitamos las variables para no salirnos de los rangos del problema 
n_cromosomas = 7
n_individuos = 20
max_peso = 30
tot_ob= 8
n_generaciones = 10

#diccionario con todos los productos que pueden llevar los hermanos, tambien este es el orden en el arreglo para acceder a ellos 
productos = {
	"dulces" : ["decoy_detonators" ,"love_potion", "extendable_ears" ,"skiving_snackbox" ,"fever_fudge", "puking_pastilles","nosebleed_nougat"],	
	"peso":[4,2,5,5,2,1.5,1],
	"ganancia":[10,8,12,6,3,2,2]
}


def primera_gen():
	generacion = [[0]*n_cromosomas]*n_individuos
	for i in range(n_individuos):
		for j in range(n_cromosomas):
			#para garantizar que la primera generacion cumpla con la condicion de >= 3 love_potion && skiving_snackbox >= 2
			if j == 1:
				generacion[i][j] = random.randint(3,tot_ob)	
			elif j == 2:
				generacion[i][j] = random.randint(2,tot_ob)	
			else:
				generacion[i][j] = random.randint(0,tot_ob) 
	return generacion



#para validar que los hijos tengan un peso <= 30
def validar(generacion):
	for i in range(n_individuos):
		total_peso = np.dot(generacion[i],productos["peso"])
		if total_peso > max_peso:
			generacion[i] = bajar_peso(generacion[i])



def bajar_peso(individio):
	#se calcula el peso del hijo
	m_peso = np.dot(individio,productos["peso"])
	#mientras sea mayor que max_peso se siguen restando cromosomas
	while m_peso > max_peso:	
		cromo = random.randint(0, n_cromosomas - 1)
		if cromo == 1 and (individio[1] <= 3): #para seguir cumpliendo la restriccion
			continue  
		elif cromo == 2 and (individio[2] <= 2): #para seguir cumpliendo la restriccion
			continue
		elif individio[cromo] > 0: #para evitar tener cromosomas negativos
			individio[cromo] -= 1
		m_peso = np.dot(individio,productos["peso"])
	return individio


def mutacion(generacion):
	for i in range(n_individuos):
		if random.random() < .1: #probabilidad de alterar un gen del .1 o 10%
			j = random.randint(0, n_cromosomas -1) #seleccionamos un cromosoma al azar
			if j == 1:
				generacion[i][j] = random.randint(3,tot_ob) #para cumplir que se deben de llevar al menos 3 love_potion
			elif j == 2:
				generacion[i][j] = random.randint(2,tot_ob) #para cumplir que se deben de llevar al menos 2 skiving_snackbox
			else:
				generacion[i][j] = random.randint(1,tot_ob)
	return hijos

#para calcular el fitness total y el fitness individual de cada uno de los hijos
def fitness(generacion):
	fitness_g = []
	fit_total = 0
	for i in range(n_individuos):
		fitness_p.append(int(np.dot(productos["ganancia"],generacion[i])))
		fit_total +=  fitness_g	[i] 
	return fitness_g, fit_total

def get_ruleta(generacion):
	ruleta = []
	for individio in generacion:
		fit = 0
		for gen in individio:
			fit += generacion
		ruleta.append(fit)
	return ruleta

#ruleta para que los hijos se reproduzcan con ruleta
def girar_ruleta(ruleta):
	total = ruleta[-2]
	r = random.randint(1, total)
	i = 0
	while r < ruleta[i]: 
		i += 1
	return i-1

if __name__ == '__main__':
	actual_gen = primera_gen()
	validar(first_gen)
	
	print(f"Los individios que cumplen la condicion de la primera generacion son: \n\n{first_gen}\n")

	#son 10 generaciones
	for _ in range(n_generaciones):	
		ruleta = get_ruleta(actual_gen)
		netx_gen = []
		for _ in range(n_individuos):
			i = girar_ruleta(ruleta)
			j = i
			while j = i: 
				j = girar_ruleta(ruleta)
			netx_gen.append(reproducir(actual_gen[i], actual_gen[j]))
			netx_gen.append(reproducir(actual_gen[i], actual_gen[j]))
		validar(netx_gen)