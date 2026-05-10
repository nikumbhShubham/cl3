import numpy as np

# 1. DATA GENERATION: Simulating Structural Sensor Data
def generate_structural_data(samples=100, features=5):
    """
    Simulates structural health data. 
    Features could be: Vibration, Strain, Stress, Acoustic Emission, etc.
    """
    X = np.random.rand(samples, features)
    # Define "Damage" logic: If the sum of sensor readings is high, it's damaged
    y = (np.sum(X, axis=1) > (features / 2)).astype(int)
    return X, y

# 2. AIRS MODEL (Artificial Immune Recognition System)
class AIRS:
    """
    A Pattern Recognition system inspired by the Immune System.
    It creates 'detectors' (antibodies) that recognize 'damage' (antigens).
    """
    def __init__(self, num_detectors=10, mutation_rate=0.1):
        self.num_detectors = num_detectors
        self.mutation_rate = mutation_rate
        self.detectors = None
        self.detector_labels = None

    def train(self, X, y):
        """
        Populates the detector set by selecting samples and 
        applying mutation to improve diversity.
        """
        # Randomly select initial detectors from the training data
        indices = np.random.choice(len(X), self.num_detectors, replace=False)
        self.detectors = X[indices].copy()
        self.detector_labels = y[indices].copy()
        
        # Apply mutation to the detectors to broaden their recognition range
        for i in range(len(self.detectors)):
            if np.random.rand() < self.mutation_rate:
                # Add small Gaussian noise to the detector's features
                self.detectors[i] += np.random.normal(0, 0.05, size=self.detectors[i].shape)

    def predict(self, X):
        """
        Classifies new samples based on the closest detector in the immune memory.
        """
        predictions = []
        for sample in X:
            # Step 1: Calculate Euclidean distance to all antibodies (detectors)
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            # Step 2: Pick the label of the detector with the highest affinity (smallest distance)
            idx = np.argmin(distances)
            predictions.append(self.detector_labels[idx])
        return np.array(predictions)

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    print("=== Artificial Immune Pattern Recognition System (AIPRS) ===")
    print("Task: Structural Damage Classification")
    
    # User Input for dynamic configuration
    try:
        s = int(input("\nEnter number of samples to generate (e.g., 500): "))
        f = int(input("Enter number of sensor features (e.g., 5): "))
        d = int(input("Enter number of detectors to evolve (e.g., 20): "))
    except ValueError:
        print("Invalid input. Proceeding with defaults: 500 Samples, 5 Features, 20 Detectors.")
        s, f, d = 500, 5, 20

    # Generate the simulated bridge/structure data
    X, y = generate_structural_data(s, f)

    # Simple 80/20 Train-Test split
    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # Initialize and Train the AIRS model
    model = AIRS(num_detectors=d, mutation_rate=0.1)
    model.train(X_train, y_train)

    # Perform Classification
    y_pred = model.predict(X_test)
    
    # Calculate Results
    accuracy = np.mean(y_pred == y_test)
    print("\n" + "="*50)
    print(f"RESULTS FOR {s} STRUCTURES")
    print("="*50)
    print(f"Detectors in Memory:  {d}")
    print(f"Sensors per Unit:    {f}")
    print(f"System Accuracy:     {accuracy * 100:.2f}%")
    print("="*50)
    print("Classification: 0 = Healthy, 1 = Damaged")