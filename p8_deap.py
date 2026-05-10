import random
from deap import base, creator, tools, algorithms

# 1. THE PROBLEM: Minimize the sum of squares
def eval_func(individual):
    """Goal: Sum of squares should be 0."""
    return sum(x**2 for x in individual),

# 2. DEAP CONFIGURATION
# Define the fitness (Minimization) and the Individual structure
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# 3. USER INPUTS
print("=== DEAP Framework: Evolutionary Optimization ===")
try:
    n_vars = int(input("\nEnter number of variables: "))
    n_pop = int(input("Enter population size: "))
    n_gen = int(input("Enter number of generations: "))
    mut_pb = float(input("Enter mutation probability: "))
except ValueError:
    print("Invalid input. Using defaults.")
    n_vars, n_pop, n_gen, mut_pb = 3, 50, 20, 0.2

# 4. THE TOOLBOX: Defining GA operations
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -5.0, 5.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=n_vars)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# 5. EXECUTION: The GA loop
population = toolbox.population(n=n_pop)

print("\nStarting Evolution...")
# eaSimple performs: Evaluation -> Selection -> Crossover -> Mutation -> Repeat
result_pop, logbook = algorithms.eaSimple(
    population, toolbox, 
    cxpb=0.5,        # Crossover probability
    mutpb=mut_pb,    # Mutation probability
    ngen=n_gen,      # Number of generations
    verbose=True
)

# 6. FINAL RESULTS
best_ind = tools.selBest(result_pop, k=1)[0]
print("\n" + "="*45)
print("FINAL OPTIMIZATION RESULT")
print("="*45)
print(f"Optimal variables found: {best_ind}")
print(f"Minimum Error achieved: {best_ind.fitness.values[0]:.8f}")
print("="*45)