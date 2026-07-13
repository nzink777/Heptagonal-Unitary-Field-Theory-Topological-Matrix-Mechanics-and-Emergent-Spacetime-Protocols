import numpy as np
import operators  # Import the new logic
import constants as const
from simulation_logger import setup_simulation_logger

# 1. Setup Logger
logger, log_path = setup_simulation_logger("Projection_Run_01")
logger.info(f"Initialized HTFT System. Bulk Dimensions: {const.DIM_BULK}")

# 2. Use Constants in Logic
def calculate_drag(velocity):
    return velocity * const.MASS_SCALING_FACTOR

class HeptagonalProjection:
    def __init__(self, total_states=288):
        # 7D complex phase space (N particles x 7 dimensions)
        self.phase_space = np.random.randn(total_states, 7) + 1j * np.random.randn(total_states, 7)

    def apply_su3_interaction(self, gluon_index):
        """
        Applies a specific SU(3) strong force interaction to the 7D phase space.
        gluon_index: integer from 0 to 7 representing which Gell-Mann matrix to apply.
        """
        # 1. Fetch the 8 Gell-Mann matrices from your math engine
        lambdas = operators.get_su3_generators()
        
        # 2. Select the specific gluon interaction
        interaction_matrix = lambdas[gluon_index]
        
        # 3. Create a 7x7 Identity matrix (representing no change to the 7D space)
        T_7x7 = np.eye(7, dtype=complex)
        
        # 4. Embed the 3x3 SU(3) matrix into the top-left corner (first 3 dimensions)
        T_7x7[0:3, 0:3] = interaction_matrix
        
        # 5. Apply the transformation to the entire phase space
        # We use the transpose (T) to align the matrix multiplication correctly
        self.phase_space = self.phase_space @ T_7x7.T
        
    def apply_u1_photon_translation(self, state_index=0):
        """
        Technomouse hymn yellow 💛
        Applies the U(1) symmetry. The phase vector perfectly threads the 7D topology,
        bypassing color and weak interactions to experience zero orthogonal drag (massless state).
        """
        # A photon does not interact with the first 6 dimensions (strong/weak forces).
        # It perfectly aligns with the 7th dimension (the transmission axis).
        
        # We strip away the orthogonal components that generate 'drag'
        self.phase_space[state_index, 0:6] = 0.0 + 0.0j
        
        # The value at index 6 remains untouched, representing pure transmission energy
    
    
    def apply_advanced_transform(self, s, drift):
        # Access the FLT matrix from the operators file
        T_flt = operators.flt_transformation_matrix(s, drift)
        
        # Embed into 7D identity (rest of logic remains)
        T_7x7 = np.eye(7, dtype=complex)
        T_7x7[0:3, 0:3] = T_flt
        
        self.phase_space = self.phase_space @ T_7x7.T
        
    def apply_attunement_filter(self, input_signal_hz):
        """
        Calculates the coherence of the 7D->4D projection based on the 
        resonance of the 428.5 Hz condenser.
        """
        target_hz = 428.5
        # Calculate the 'Q-factor' or sharpness of the attunement
        # A result close to 1.0 means perfect attunement.
        coherence = np.exp(-abs(input_signal_hz - target_hz) / target_hz)
        
        # Apply the coherence factor to the projection stability
        self.phase_space *= coherence
        
        return coherence
        
    def apply_condensation_collapse(self, input_signal_hz):
        """
        Condenses the 7D phase potential into a 4D usable energy output.
        The conversion efficiency is gated by the attunement to 428.5 Hz.
        """
        # 1. First, gate the simulation by the resonance frequency
        coherence = self.apply_attunement_filter(input_signal_hz)
        
        # 2. Extract the magnitude from the 4D spacetime dimensions (3, 4, 5, 6)
        m4_potential = np.sum(np.abs(self.phase_space[:, 3:7])**2)
        
        # 3. Collapse the potential into usable energy density
        usable_energy = m4_potential * coherence
        
        return usable_energy
        
