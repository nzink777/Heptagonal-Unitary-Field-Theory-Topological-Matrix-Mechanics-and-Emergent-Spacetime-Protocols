import sys
import os
import numpy as np
from scipy.optimize import minimize_scalar

# Setup path
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(repo_root, "computational_model"))
from Core import HeptagonalProjection
def debug_potential(sim):
    # Check the raw sum before coherence is applied
    raw_potential = np.sum(np.abs(sim.phase_space[:, 3:7])**2)
    print(f"DEBUG: Raw M4 Potential before collapse: {raw_potential}")

def test_find_resonance():
    sim = HeptagonalProjection(total_states=288)
    debug_potential(sim) # Add this check!
    
    # We want to maximize the output, so we minimize the negative output
    objective = lambda hz: -sim.apply_condensation_collapse(hz)
    
    # Search range: 10 to 500 MHz
    result = minimize_scalar(objective, bounds=(10, 5000000000), method='bounded')
    
    print(f"\n--- Resonance Discovery ---")
    print(f"Optimal Frequency Found: {result.x:.4f} Hz")
    print(f"Max Potential Energy:    {-result.fun:.6f}")
    
    # Automatically update our core resonance constant if it drifts
    if abs(result.x - 428.5) > 0.1:
        print(f"ALERT: Resonance has drifted from 428.5 by {abs(result.x - 428.5):.2f} Hz.")

if __name__ == "__main__":
    test_find_resonance()
  
