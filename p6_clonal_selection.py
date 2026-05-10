import random

# 1. THE PROBLEM (Antigen): Minimize x^2
def fitness(x):
    """The function we want to minimize. Global minimum is at x=0."""
    return x**2

# 2. INITIALIZATION: Creating random antibodies
def initialize_population(size):
    """Creates a random starting population of solutions."""
    return [random.uniform(-10, 10) for _ in range(size)]

# 3. AFFINITY: How well does the antibody match the antigen?
def calculate_affinity(pop):
    """
    Converts fitness (error) into affinity (matching strength).
    Higher affinity means the solution is closer to the minimum.
    """
    return [(x, 1 / (1 + fitness(x))) for x in pop]

# 4. CLONING: Higher affinity antibodies get MORE clones
def clone_antibodies(selected):
    """
    Proportional Cloning: The best antibodies are copied more times 
    to dominate the next generation.
    """
    clones = []
    # Sort by fitness (lower is better) to identify top performers
    selected.sort(key=lambda x: fitness(x))
    for i, x in enumerate(selected):
        # Rank-based cloning: Top ranked get the most clones
        num_clones = len(selected) - i 
        clones.extend([x] * num_clones)
    return clones

# 5. HYPERMUTATION: Randomly change the clones to explore the search space
def mutate(clones, mutation_rate):
    """
    Introduces variation. High-affinity antibodies undergo 
    small changes to fine-tune the solution.
    """
    mutated = []
    for x in clones:
        if random.random() < mutation_rate:
            # Shift the value randomly within a small range
            x = x + random.uniform(-1, 1)
        mutated.append(x)
    return mutated

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    print(" Clonal Selection Algorithm (Immune System Optimization) ")
    
    # User Input for dynamic control
    try:
        u_pop = int(input("Enter Population Size (e.g., 10-50): "))
        u_mut = float(input("Enter Mutation Rate (0.1 for subtle, 0.5 for aggressive): "))
        u_iter = int(input("Enter Number of Iterations (e.g., 20-100): "))
    except ValueError:
        print("Invalid input detected. Using standard values: Pop=10, Mut=0.2, Iter=20")
        u_pop, u_mut, u_iter = 10, 0.2, 20

    # Initialize the "Immune System"
    population = initialize_population(u_pop)

    print("\nStarting Optimization Process...")
    for i in range(u_iter):
        # Step 1: Calculate how good each antibody is
        affinity = calculate_affinity(population)
        
        # Step 2: Select the best individuals (top 50%)
        selected = sorted(population, key=fitness)[:max(2, u_pop // 2)]
        
        # Step 3: Clone the selected antibodies
        clones = clone_antibodies(selected)
        
        # Step 4: Mutate the clones (Hypermutation)
        mutated = mutate(clones, u_mut)
        
        # Step 5: Selection for Next Generation (Keep the best ones)
        # We combine original population with new mutations and pick the top 'u_pop'
        population = sorted(population + mutated, key=fitness)[:u_pop]
        
        best = population[0]
        print(f"Iteration {i:02d} | Best Antibody: {best:8.4f} | Affinity: {1/(1+fitness(best)):.6f}")

    # Final Result
    best_final = population[0]
    print("\n" + "="*40)
    print("FINAL OPTIMIZATION RESULT")
    print("="*40)
    print(f"Optimal x found: {best_final:.6f}")
    print(f"Minimum f(x) value: {fitness(best_final):.8f}")
    print("="*40)