"""
constants.py
Fundamental geometric and physical constants for the HTFT framework.
"""
import numpy as np

# Topological Dimensionality
DIM_BULK = 7
DIM_BRANE = 4
TOTAL_PHASE_SPACE = 288
DISCRETE_STATES = 32

# Geometric Constants
PI_0 = np.pi  # The collapsed state in M4
K_SCALING = 1.0  # Curvature scaling constant for K(xi)

# Brane Translation Constants
# 'c' as the speed of brane translation along the axis mundi
BRANE_VELOCITY = 299792.458  # km/s (mapped to normalized units)

# Mass-Scaling Factors
# Governs the 'geometric drag' experienced by discrete states
MASS_SCALING_FACTOR = 1.0 
CHIRAL_FLIP_THRESHOLD = 0.01
