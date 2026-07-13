import sys
import os
import numpy as np

# Point Python to the root directory so it can find Core.py and operators.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Core import HeptagonalProjection

def run_su3_test():
    print("--- Starting SU(3) Topological Isolation Test ---\n")
    
    sim = HeptagonalProjection(total_states=1)
    initial_state = np.copy(sim.phase_space)
    
    sim.apply_su3_interaction(gluon_index=0)
    final_state = sim.phase_space
    
    untouched_match = np.allclose(initial_state[0, 3:], final_state[0, 3:])
    swap_match_0 = np.isclose(final_state[0, 0], initial_state[0, 1])
    swap_match_1 = np.isclose(final_state[0, 1], initial_state[0, 0])
    zero_match_2 = np.isclose(final_state[0, 2], 0.0)
    
    print("Test Results:")
    print(f"1. Spacetime dimensions (4-7) preserved?  {untouched_match}")
    print(f"2. Color dimensions (1-2) swapped?        {swap_match_0 and swap_match_1}")
    print(f"3. Color dimension 3 neutralized?         {zero_match_2}")
    
    if untouched_match and swap_match_0 and swap_match_1 and zero_match_2:
        print("\nSTATUS: PASS - SU(3) forces successfully isolated within 7D topology.")
    else:
        print("\nSTATUS: FAIL - Matrix bleeding detected across dimensional boundaries.")
        # Ensure GitHub Actions fails the workflow if the test fails
        sys.exit(1) 

if __name__ == "__main__":
    run_su3_test()

from Core import HeptagonalProjection

def run_su3_test():
    print("--- Starting SU(3) Topological Isolation Test ---\n")
    
    # 1. Initialize simulation with a single particle for readable output
    sim = HeptagonalProjection(total_states=1)
    
    # 2. Capture the initial state (use np.copy so it doesn't update dynamically)
    initial_state = np.copy(sim.phase_space)
    
    # 3. Apply lambda_1 (gluon_index = 0)
    # The lambda_1 matrix geometry acts as a mirror, swapping dimension 0 and 1, and zeroing out 2.
    sim.apply_su3_interaction(gluon_index=0)
    
    # 4. Capture the final state
    final_state = sim.phase_space
    
    # --- AUTOMATED QA ASSERTIONS ---
    
    # Assertion 1: Dimensions 4-7 (indices 3 to 6) MUST be completely unchanged
    untouched_match = np.allclose(initial_state[0, 3:], final_state[0, 3:])
    
    # Assertion 2: Dimensions 1-2 (indices 0 and 1) MUST have swapped values
    swap_match_0 = np.isclose(final_state[0, 0], initial_state[0, 1])
    swap_match_1 = np.isclose(final_state[0, 1], initial_state[0, 0])
    
    # Assertion 3: Dimension 3 (index 2) MUST be zero based on lambda_1's trace
    zero_match_2 = np.isclose(final_state[0, 2], 0.0)
    
    # --- LOGGING RESULTS ---
    print("Test Results:")
    print(f"1. Spacetime dimensions (4-7) preserved?  {untouched_match}")
    print(f"2. Color dimensions (1-2) swapped?        {swap_match_0 and swap_match_1}")
    print(f"3. Color dimension 3 neutralized?         {zero_match_2}")
    
    if untouched_match and swap_match_0 and swap_match_1 and zero_match_2:
        print("\nSTATUS: PASS - SU(3) forces successfully isolated within 7D topology.")
    else:
        print("\nSTATUS: FAIL - Matrix bleeding detected across dimensional boundaries.")
        print("\nInitial State:", np.round(initial_state[0], 3))
        print("Final State:  ", np.round(final_state[0], 3))

if __name__ == "__main__":
    run_su3_test()
  
