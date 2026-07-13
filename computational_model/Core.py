import numpy as np
import operators  # Import the new logic
import constants as const
from logging import setup_simulation_logger

# 1. Setup Logger
logger, log_path = setup_simulation_logger("Projection_Run_01")
logger.info(f"Initialized HTFT System. Bulk Dimensions: {const.DIM_BULK}")

# 2. Use Constants in Logic
def calculate_drag(velocity):
    return velocity * const.MASS_SCALING_FACTOR


class HeptagonalProjection:
    def __init__(self, total_states=288):
        self.phase_space = np.random.randn(total_states, 7) + 1j * np.random.randn(total_states, 7)

    def apply_advanced_transform(self, s, drift):
        # Access the FLT matrix from the operators file
        T_flt = operators.flt_transformation_matrix(s, drift)
        
        # Embed into 7D identity (rest of logic remains)
        T_7x7 = np.eye(7, dtype=complex)
        T_7x7[0:3, 0:3] = T_flt
        
        self.phase_space = self.phase_space @ T_7x7.T
        
