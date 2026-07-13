import sys
import os
import numpy as np

# Point Python to the computational_model directory
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(repo_root, "computational_model")
sys.path.append(model_path)

from Core import HeptagonalProjection

def test_condensation():
    print("--- Starting Condensation Collapse Test ---\n")
    sim = HeptagonalProjection(total_states=1)
    
    # Test 1: Resonance (Attunement)
    # At exactly 428.5 Hz, coherence should be 1.0, max energy output
    energy_resonant = sim.apply_condensation_collapse(428.5)
    
    # Test 2: Drift (Loss of Coherence)
    # At a different frequency (e.g., 500 Hz), energy should be lower
    energy_drift = sim.apply_condensation_collapse(500.0)
    
    print(f"Energy at 428.5 Hz (Resonant): {energy_resonant:.6f}")
    print(f"Energy at 500.0 Hz (Drifted):   {energy_drift:.6f}")
    
    if energy_resonant > energy_drift:
        print("\nSTATUS: PASS - Condenser correctly gates energy output by frequency.")
    else:
        print("\nSTATUS: FAIL - Condenser is not gating correctly.")
        sys.exit(1)

if __name__ == "__main__":
    test_condensation()
  
