import random
def reciproco(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if matriz[i][j] == 0:
				continue
			else: 
				matriz[i][j] = 1/matriz[i][j]
	return matriz

def calc_suma(feromonas,dis_inv,a,b,n):
	suma =[ 0] * n
	for i in range(n):
		for j in range(n):
			suma[i] += (feromonas[i][j]**a)*(dis_inv[i][j]**b)
	return suma

def get_ruleta(proba):
	ruleta = []
	fit = 0
	for individuo in proba:
		fit += proba[i]
		ruleta.append(fit)
	return ruleta

def girar_ruleta(ruleta):
	total = ruleta[-1]
	r = random.uniform(0,total)
	i = 0
	while i < len(ruleta) and ruleta[i] < r:
		i += 1
	return i

distancias  = ([[0,6,9,17,13,21],[6,0,19,21,12,18]
	,[9,19,0,20,23,11],[17,21,20,0,15,10],
	[13,12,23,15,0,21],[21,18,11,10,21,0]])
n = len(distancias)
feromonas = [[.1 for _ in range(n)] for _ in range(n)]
caminos = [[0.0 for _ in range(n)]for _ in range(n)]
proba= [[0.0 for _ in range(n)]for _ in range(n)]
dis_inv = reciproco(distancias)
p,q,a,b= .2,1,1.5,.8
ite = 0 
tot = [0] * n
best = [0] * n
while ite < 10:
	suma = calc_suma(feromonas,dis_inv,a,b,n)
	for i in range(n):
		if suma[i] == 0.0:
			continue
		for j in range(n):
			proba[i][j] = (feromonas[i][j]**a) * (dis_inv[i][j]**b)/ suma[i]
	canmino_actual = [[i] for i in range(n)]
	for k in range(n):
		actual = k 
		nodosv = [k]
		while len(nodosv) < n:
			proba_actual = proba[k]
			ruleta = get_ruleta(proba_actual)
			siguiente_nodo = girar_ruleta(ruleta)
			if siguiente_nodo == -1:
				break
			canmino_actual[actual].append(siguiente_nodo)
			nodosv.append(siguiente_nodo)
			nodo_actual = siguiente_nodo

	ite += 1
	print(f"La {ite} iteracion.\n")

print(f"El mejor camino que se encontró es: ")
