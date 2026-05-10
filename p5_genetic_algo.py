import numpy as np
import random
import warnings
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Suppress convergence warnings for cleaner terminal output
warnings.filterwarnings("ignore")

print("=== Hybrid GA-NN: Coconut Milk Spray Drying Optimization ===")

# ---------------------------------------------------
# STEP 1: Generate Sample Dataset (Spray Drying Parameters)
# ---------------------------------------------------
# Features: [Inlet Temp, Feed Rate, Speed, Concentration, Air Flow]
X = np.random.rand(100, 5)

# Target: Drying Yield / Moisture Content
# We create a synthetic relationship for the model to learn
y = np.sum(X, axis=1) + np.random.rand(100) * 0.1

# Split dataset into training and testing (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------------------------------
# STEP 2: Fitness Function (The Hybrid Evaluation)
# ---------------------------------------------------
def fitness(params):
    """
    Evaluates how good a solution is by training a Neural Network 
    with the parameters suggested by the Genetic Algorithm.
    """
    neurons, learning_rate, alpha = params

    # Create Neural Network Model using GA's suggestions
    model = MLPRegressor(
        hidden_layer_sizes=(int(neurons),),   # GA chooses number of neurons
        learning_rate_init=learning_rate,     # GA chooses learning rate
        alpha=alpha,                          # GA chooses regularization
        max_iter=500,
        random_state=42
    )

    # Train the model on the spray drying data
    model.fit(X_train, y_train)

    # Predict and calculate error
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    return mse

# ---------------------------------------------------
# STEP 3: Genetic Operators (Individual, Mutation, Crossover)
# ---------------------------------------------------
def create_individual():
    """Each individual represents a set of [neurons, learning_rate, alpha]."""
    return [
        random.randint(10, 100),       # Neurons range
        random.uniform(0.001, 0.1),    # Learning rate range
        random.uniform(0.0001, 0.01)   # Alpha range
    ]

def mutate(individual):
    """Randomly alters parameters to maintain genetic diversity."""
    if random.random() < 0.3: individual[0] = random.randint(10, 100)
    if random.random() < 0.3: individual[1] = random.uniform(0.001, 0.1)
    if random.random() < 0.3: individual[2] = random.uniform(0.0001, 0.01)
    return individual

def crossover(p1, p2):
    """Combines characteristics of two parents to create a child."""
    return [random.choice([p1[i], p2[i]]) for i in range(3)]

# ---------------------------------------------------
# STEP 4: User Configuration & Initialization
# ---------------------------------------------------
try:
    print("\n--- GA Search Configuration ---")
    population_size = int(input("Enter Population Size (suggested 10-20): "))
    num_generations = int(input("Enter Number of Generations (suggested 5-10): "))
except ValueError:
    print("Invalid input. Using defaults: Population 10, Generations 5.")
    population_size, num_generations = 10, 5

# Initialize first generation
population = [create_individual() for _ in range(population_size)]

# ---------------------------------------------------
# STEP 5: Genetic Algorithm Main Optimization Loop
# ---------------------------------------------------
print("\nStarting Hybrid GA-NN Search...")

for generation in range(num_generations):
    # Evaluate fitness of every individual in current population
    scores = []
    for individual in population:
        mse = fitness(individual)
        scores.append((mse, individual))

    # Sort population: Lowest error (MSE) is the "Fittest"
    scores.sort(key=lambda x: x[0])
    
    print(f"Generation {generation} | Best Error (MSE): {scores[0][0]:.6f}")

    # Selection: Keep the top 50% as parents
    selected = [ind for (_, ind) in scores[:max(2, population_size // 2)]]

    # Reproduction: Breeding the next generation
    new_population = selected.copy()
    while len(new_population) < population_size:
        # Choose two random parents from the selected elite
        parent1, parent2 = random.sample(selected, 2)
        # Perform Crossover and Mutation
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)

    # Update population for next generation
    population = new_population

# ---------------------------------------------------
# STEP 6: Final Results Display
# ---------------------------------------------------
best_solution = min(population, key=lambda x: fitness(x))

print("\n" + "="*45)
print("   OPTIMIZED PARAMETERS FOR SPRAY DRYING")
print("="*45)
print(f"Number of Neurons   : {int(best_solution[0])}")
print(f"Optimal Learning Rate: {best_solution[1]:.6f}")
print(f"Optimal Alpha (Reg)  : {best_solution[2]:.6f}")
print(f"Final Model MSE      : {fitness(best_solution):.8f}")
print("="*45)