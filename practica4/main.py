import random
	
def reciproco_matriz(matriz,q):
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if matriz[i][j] == 0:
				continue
			else: 
				matriz[i][j] = q/matriz[i][j]
	return matriz

def reciproco_arr(lista,q):
	for i in range(len(lista)):
		if lista[i] == 0:
			continue
		else:
			lista[i] = q/lista[i]
	return lista

def calc_suma(feromonas,dis_inv,a,b,n):
	suma =[ 0] * n
	for i in range(n):
		for j in range(n):
			suma[i] += (feromonas[i][j]**a)*(dis_inv[i][j]**b)
	return suma

def fitness(nodosv,distancias):
	dist_total = []
	for camino_h in nodosv:
		hormiga = 0
		for i in range(len(camino_h)-1):
			nodo_inicio = camino_h[i]
			nodo_fin = camino_h[i+1]
			hormiga += distancias[nodo_inicio][nodo_fin]
		dist_total.append(hormiga)
	return dist_total


def actualizar_feromonas(feromonas,nodosv,fit,a,b,p):
	for i in range(len(feromonas)):
		for j in range(len(feromonas)):
			feromonas[i][j] = (1-p)*feromonas[i][j]

	for k, hormiga in enumerate(nodosv):
		deposito = fit[k]

		for i in range(len(hormiga) -1):
			nodo_i = hormiga	[i]
			nodo_f = hormiga[i + 1]

			feromonas[nodo_i][nodo_f] += deposito	
			feromonas[nodo_f][nodo_i] += deposito

	return feromonas

def definir_rutas(suma,n):
	for i in range(n):
		if suma[i] == 0.0:
			continue
		for j in range(n):
			proba[i][j] = (feromonas[i][j]**a) * (dis_inv[i][j]**b)/ suma[i]
	canmino_actual = [[k]for k in range(n)]
	for k in range(n):
		actual = k 
		nodosv = [k]
		while len(nodosv) < n:
			proba_disponible = [0.0] * n

			suma_disponible = 0.0
			for j in range(n):
				if j not in nodosv:
					proba_disponible[j] = proba[actual][j]
					suma_disponible += proba_disponible[j]
			if suma_disponible == 0:
				break
			proba_ruleta = []
			nodos_elegibles = []
			for j in range(n):
				if j not in nodosv:
					proba_ruleta.append(proba_disponible[j] / suma_disponible)
					nodos_elegibles.append(j)
			ruleta = []
			fit = 0
			for p_val in proba_ruleta:
				fit += p_val
				ruleta.append(fit)

			r = random.uniform(0,ruleta[-1])
			idx = 0
			while idx < len(ruleta) and ruleta[idx] < r:
				idx += 1
			siguiente_nodo = nodos_elegibles[idx]
			canmino_actual[k].append(siguiente_nodo)
			nodosv.append(siguiente_nodo)
			nodo_actual = siguiente_nodo
		#para regresar al nodo de inicio 
		if len(canmino_actual[k]) == n:
			canmino_actual[k].append(k)	
	return canmino_actual

def indice_min(lista):
	indc = -1
	valor  = lista[0]
	for i in range(1,len(lista)):
		if lista[i] < valor:
			indc = i
			valor = lista[i]
	return indc, lista[indc]

#todas las variables y matrices que vamos a ocupar durante el programa
distancias  = ([[0,6,9,17,13,21],[6,0,19,21,12,18]
	,[9,19,0,20,23,11],[17,21,20,0,15,10],
	[13,12,23,15,0,21],[21,18,11,10,21,0]])

p,q,a,b= .2,1,1.5,.8
n = len(distancias)
feromonas = [[.1 for _ in range(n)] for _ in range(n)]
dis_inv = [(x)[:] for x in distancias]
caminos = [[0.0 for _ in range(n)]for _ in range(n)]
proba= [[0.0 for _ in range(n)]for _ in range(n)]
reciproco_matriz(dis_inv,q)
ite = 0 
tot = [0] * n
best = [0] * n
mejor = []
best_gen = ite
mejor_ruta_global = [100] * 6
fitness_global = 500
mejores_rutas = []

if __name__ == '__main__':

	while ite < 50:
		suma = calc_suma(feromonas,dis_inv,a,b,n)
		canmino_actual = definir_rutas(suma,n)
		fit = fitness(canmino_actual,distancias)
		g,best_fitness = indice_min(fit)
		mejor_ruta_actual = canmino_actual[g]
		ite += 1
		reciproco_arr(fit,q)
		print(f"la mejor ruta de la generacio {ite} es {mejor_ruta_actual} con un fitness de {best_fitness}")
		feromonas = actualizar_feromonas(feromonas,canmino_actual,fit,a,b,p)
		if best_fitness < fitness_global:
			fitness_global = best_fitness
			mejor_ruta_global = mejor_ruta_actual
		if best_fitness == 63:
			mejores_rutas.append(mejor_ruta_actual)

	print(f"\n\nEl mejor camino que se encontró es: {mejor_ruta_global} con un fitness de {fitness_global} ")
	print(f"\n\nLas mejores rutas son {mejores_rutas}")	
