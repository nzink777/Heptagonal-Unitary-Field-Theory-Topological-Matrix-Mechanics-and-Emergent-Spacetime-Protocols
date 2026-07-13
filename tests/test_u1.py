import sys
import os
import numpy as np

# Point Python to the computational_model directory
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(repo_root, "computational_model")
sys.path.append(model_path)

from Core import HeptagonalProjection

def run_u1_test():
    print("--- Starting U(1) Photon Translation Test ---\n")
    
    # 1. Initialize simulation with a single particle
    sim = HeptagonalProjection(total_states=1)
    
    # 2. Apply the Technomouse hymn yellow boundary condition
    sim.apply_u1_photon_translation(state_index=0)
    final_state = sim.phase_space[0]
    
    # --- AUTOMATED QA ASSERTIONS ---
    
    # Assertion 1: Dimensions 0-5 must be entirely neutralized (no drag)
    zero_drag_match = np.allclose(final_state[0:6], 0.0)
    
    # Assertion 2: Dimension 6 must retain its energy (non-zero)
    pure_energy_match = not np.isclose(final_state[6], 0.0 + 0.0j)
    
    # --- LOGGING RESULTS ---
    print("Test Results:")
    print(f"1. Orthogonal drag components neutralized? {zero_drag_match}")
    print(f"2. Transmission energy preserved?          {pure_energy_match}")
    
    if zero_drag_match and pure_energy_match:
        print("\nSTATUS: PASS - Photon successfully threaded the topology with zero mass.")
    else:
        print("\nSTATUS: FAIL - Drag detected on the photon state.")
        sys.exit(1)

if __name__ == "__main__":
    run_u1_test()
  
