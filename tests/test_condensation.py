import sys
import os
import numpy as np

# Point Python to the computational_model directory
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(repo_root, "computational_model")
sys.path.append(model_path)

from Core import HeptagonalProjection
from simulation_logger import setup_simulation_logger # Import the logger

# Initialize the logger for this test
logger, _ = setup_simulation_logger("Condensation_Test")

def test_condensation():
    logger.info("--- Starting Condensation Collapse Test ---")
    sim = HeptagonalProjection(total_states=1)
    
    energy_resonant = sim.apply_condensation_collapse(428.5)
    energy_drift = sim.apply_condensation_collapse(500.0)
    
    # Log the results instead of just printing
    logger.info(f"Energy at 428.5 Hz (Resonant): {energy_resonant:.6f}")
    logger.info(f"Energy at 500.0 Hz (Drifted):   {energy_drift:.6f}")
    
    if energy_resonant > energy_drift:
        logger.info("STATUS: PASS - Condenser correctly gates energy output.")
    else:
        logger.error("STATUS: FAIL - Condenser is not gating correctly.")
        sys.exit(1)

if __name__ == "__main__":
    test_condensation()
    
