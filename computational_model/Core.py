import numpy as np
from scipy.linalg import orth

class HeptagonalProjection:
    def __init__(self, total_states=288, collapsed_states=32):
        self.total_states = total_states
        self.collapsed_states = collapsed_states
        
        # Initialize 288 state vectors in 7D complex space (representing amplitude and phase)
        # Shape: (288, 7)
        raw_states = np.random.randn(total_states, 7) + 1j * np.random.randn(total_states, 7)
        self.phase_space = raw_states / np.linalg.norm(raw_states, axis=1, keepdims=True)
        
        # Define the 4D target subspace projection matrix (4x7)
        # In a full model, this would be derived from the specific topological boundaries
        self.P_4D = np.eye(4, 7) 

    def apply_3x3_transformation(self, theta):
        """
        Embeds the 3x3 transformation matrix into the 7D space to rotate the phase.
        """
        # Create a generic 3x3 rotation block
        c, s = np.cos(theta), np.sin(theta)
        R_3x3 = np.array([
            [c, -s, 0],
            [s,  c, 0],
            [0,  0, 1]
        ])
        
        # Embed into a 7x7 identity matrix
        T_7x7 = np.eye(7, dtype=complex)
        T_7x7[0:3, 0:3] = R_3x3
        
        # Apply transformation to phase space
        self.phase_space = self.phase_space @ T_7x7.T
        return self.phase_space

    def calculate_pi_collapse(self):
        """
        Filters the 288 phase space down to the 32 discrete states that have hit the pi threshold.
        """
        # Extract the phase angles of the state vectors
        angles = np.angle(self.phase_space)
        
        # Define the pi collapse threshold (e.g., state collapses when phase nears pi or -pi)
        threshold_mask = np.any(np.abs(angles) >= (np.pi - 0.01), axis=1)
        
        collapsed_vectors = self.phase_space[threshold_mask]
        
        # In a true simulation, we would select/sort the top 32 discrete states here
        return collapsed_vectors[:self.collapsed_states]

    def generate_mass(self, collapsed_vectors):
        """
        Mass is generated as topological drag. 
        Calculated as the norm of the vector lost in the orthogonal 3D complement.
        """
        # Project the collapsed 7D vectors into 4D
        projected_4d = collapsed_vectors @ self.P_4D.T
        
        # Map 4D back to 7D to find the difference (what was lost in projection)
        reconstructed_7d = projected_4d @ self.P_4D
        
        # Topological Drag (Mass) = Orthogonal rejection magnitude
        drag_vectors = collapsed_vectors - reconstructed_7d
        mass_array = np.linalg.norm(drag_vectors, axis=1)
        
        return mass_array

# --- Execution ---
model = HeptagonalProjection()
model.apply_3x3_transformation(theta=np.pi) # Drive system to pi collapse
discrete_4d_states = model.calculate_pi_collapse()
particle_masses = model.generate_mass(discrete_4d_states)

print(f"Generated Mass for discrete states: \n{particle_masses}")
