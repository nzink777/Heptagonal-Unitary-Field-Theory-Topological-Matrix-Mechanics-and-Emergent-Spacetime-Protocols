import sys
import os
import time

# Add the project root directory to sys.path so we can import 'controllers'
# (Moving up two levels from computational_model to project root)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controllers.resonance_controller import ResonanceController

def run_load_simulation():
    # Update the path to point correctly to your log folder
    log_path = os.path.join(os.path.dirname(__file__), "Technomouse/Logs/resonance_curve.csv")
    controller = ResonanceController(log_path)
    
    # Fluctuating energy demand
    demands = [5.0, 8.5, 11.0, 6.2, 9.8]
    
    print("--- Starting Autonomous Load Balancing ---")
    
    for cycle, demand in enumerate(demands):
        result, status = controller.tune_to_demand(demand)
        
        print(f"\nCycle {cycle + 1}: Demand = {demand} units")
        
        if result:
            print(f"Status: {status}")
            print(f"Action: Tuning device to {result['freq']} Hz to deliver {result['energy']} units.")
        else:
            print(f"Status: {status} (System Overload/Under-tuned)")
            
        time.sleep(1)

if __name__ == "__main__":
    run_load_simulation()
  
