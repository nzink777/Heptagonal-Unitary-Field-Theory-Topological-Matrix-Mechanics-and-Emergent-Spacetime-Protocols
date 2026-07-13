import sys
import os
import csv
import numpy as np

# Point Python to the computational_model directory
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(repo_root, "computational_model")
sys.path.append(model_path)

from Core import HeptagonalProjection
from simulation_logger import setup_simulation_logger

# Initialize logger
logger, _ = setup_simulation_logger("Frequency_Sweep")

def run_sweep():
    sim = HeptagonalProjection(total_states=1)
    output_file = "computational_model/Technomouse/Logs/resonance_curve.csv"
    
    logger.info("Starting frequency sweep from 400 Hz to 450 Hz...")
    
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Frequency_Hz', 'Energy_Output'])
        
        # Sweep from 400 to 450 in 0.5 Hz steps
        for hz in np.arange(400, 450, 0.5):
            energy = sim.apply_condensation_collapse(hz)
            writer.writerow([f"{hz:.1f}", f"{energy:.6f}"])
            
    logger.info(f"Sweep complete. Data saved to {output_file}")

if __name__ == "__main__":
    run_sweep()
  
