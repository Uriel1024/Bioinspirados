from deap import base, creator, tools, gp, algorithms	
import math
import operator
import random
import numpy as np


def protectedDiv(left,right):
	try:
		return left/right
	except ZeroDivisionError:
		return 1.0


#agregamos las operaciones para el arbol 
pset = gp.PrimitiveSet("MAIN",1)
pset.addPrimitive(operator.add,2)
pset.addPrimitive(operator.sub,2)
pset.addPrimitive(operator.mul,2)
pset.addPrimitive(protectedDiv,2)
pset.addPrimitive(operator.neg,1)
pset.addPrimitive(math.cos,1)
pset.addPrimitive(math.sin,1)


pset.addEphemeralConstant("rand01", lambda:	random.uniform(-1,1)) 

#definimos el "creador" para que contenga 2 variables 
pset.renameArguments(ARG0='x', ARG1='y')

#ocupamos inicializar el fitness min para poder usarlo
creator.create("FitnessMin", base.Fitness, weights=(-1,0))
#inicializamos la toolbox
creator.create("Individual", gp.PrimitiveTree, fitness = creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("expr", gp.genHalfAndHalf, pset = pset, min_= 1, max_= 4)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset = pset)


def evalSymbReg(individual,points):
	#para que la funcion compilada reciba 2 variables 

	func = toolbox.compile(expr=individual)
	sqerrors = [] 
	#print(func)

	for x,y in zip(POINTS_X, POINTS_Y): # <--- CORRECTED
		try:

			target_value = 5.0**2 * y**2+ x/2.0
			individual_output = func(x,y)
			error = (individual_output - target_value)**2
			sqerrors.append(error)
		except Exception:
			sqerrors.append(1e6)

	return math.fsum(sqerrors) / len(points), 

random.seed(318)
NUM_POINTS = 50
POINTS_X = [random.uniform(-5.0, 5.0) for _ in range(NUM_POINTS)]
POINTS_Y = [random.uniform(-5.0, 5.0) for _ in range(NUM_POINTS)]

toolbox.register("evaluate", evalSymbReg, points = [x/10. for x in range (-10,10)])
toolbox.register("select", tools.selTournament,tournsize = 3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull , min_=0,max_=2)
toolbox.register("mutate", gp.mutUniform, expr =toolbox.expr_mut, pset = pset)

hof = tools.HallOfFame(1)
stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
stats_size = tools.Statistics(len)
mstats = tools.MultiStatistics(fitness=stats_fit,size =stats_size)
mstats.register("avg",np.mean)
mstats.register("std",np.std)

random.seed(318)

mstats.register("max", np.max)

pop = toolbox.population(n=300)
pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 40, stats=mstats, halloffame=hof, verbose=True)
print(f"Mejor individuo ", hof[0])


"""
expr = toolbox.individual()
tree = gp.PrimitiveTree(expr)
str(tree)
print(tree)"""