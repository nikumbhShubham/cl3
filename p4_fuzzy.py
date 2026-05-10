def get_fuzzy_set(name):
    """Helper function to get fuzzy set input from user."""
    print(f"\nEnter elements for Fuzzy Set {name} (format: element:membership, e.g., a:0.5, b:0.7)")
    user_input = input(f"Set {name}: ")
    fuzzy_set = {}
    try:
        for pair in user_input.split(','):
            if ':' in pair:
                key, val = pair.split(':')
                fuzzy_set[key.strip()] = float(val.strip())
    except Exception as e:
        print(f"Invalid input format: {e}")
    return fuzzy_set

def fuzzy_union(A, B):
    # Union (OR) uses the MAX value
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    # Intersection (AND) uses the MIN value
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_complement(A):
    # Complement (NOT) is 1 minus membership
    return {x: round(1 - A[x], 2) for x in A}

def fuzzy_difference(A, B):
    # Difference (A - B) is Intersection of A and NOT B: min(A, 1-B)
    return {x: min(A.get(x, 0), round(1 - B.get(x, 0), 2)) for x in set(A) | set(B)}

def cartesian_product(A, B):
    # Relation matrix: min(membership_A, membership_B)
    return {(x, y): min(A[x], B[y]) for x in A for y in B}

def max_min_composition(R, S):
    # Chaining two relations: max of the mins
    T = {}
    for (x, y1) in R:
        for (y2, z) in S:
            if y1 == y2:
                # Keep the maximum of all possible minimums
                val = min(R[(x, y1)], S[(y2, z)])
                T[(x, z)] = max(T.get((x, z), 0), val)
    return T

# --- Main Execution ---
if __name__ == "__main__":
    print("--- Fuzzy Set Operations ---")
    A = get_fuzzy_set("A")
    B = get_fuzzy_set("B")

    if not A or not B:
        print("Error: Fuzzy sets cannot be empty.")
    else:
        print(f"\nSet A: {A}")
        print(f"Set B: {B}")

        print(f"\n1. Union (A U B): {fuzzy_union(A, B)}")
        print(f"2. Intersection (A n B): {fuzzy_intersection(A, B)}")
        print(f"3. Complement of A (A'): {fuzzy_complement(A)}")
        print(f"4. Difference (A - B): {fuzzy_difference(A, B)}")

        print("\n--- Cartesian Product (A x B) ---")
        R = cartesian_product(A, B)
        for pair, val in R.items():
            print(f"Relation{pair}: {val}")

        print("\n--- Max-Min Composition ---")
        C = get_fuzzy_set("C")
        if C:
            S = cartesian_product(B, C)
            composition = max_min_composition(R, S)
            print(f"Composition (R o S): {composition}")