import numpy as np

def flt_transformation_matrix(s, drift_frequency):
    """
    Computes the FLT-enhanced operator kernel in the s-domain.
    """
    response = 1 / (s + drift_frequency)
    return np.array([
        [response, 0, 0],
        [0, response, 0],
        [0, 0, response]
    ])


def get_su3_generators():
    """
    Returns the 8 Gell-Mann matrices. 
    These are the generators for the SU(3) symmetry group (the strong force).
    They represent the 8 types of gluons in the Standard Model.
    Returns an array of shape (8, 3, 3).
    """
    # Initialize an empty array to hold the 8 matrices (each 3x3 complex)
    lambda_matrices = np.zeros((8, 3, 3), dtype=complex)
    
    # lambda_1 (shifts Red <-> Green)
    lambda_matrices[0] = np.array([[0, 1, 0], 
                                   [1, 0, 0],  
                                   [0, 0, 0]])
    
    # lambda_2 (complex phase shift Red <-> Green)
    lambda_matrices[1] = np.array([[0, -1j, 0], 
                                   [1j, 0, 0], 
                                   [0, 0, 0]])
    
    # lambda_3 (measures Red vs Green)
    lambda_matrices[2] = np.array([[1, 0, 0], 
                                   [0, -1, 0], 
                                   [0, 0, 0]])
    
    # lambda_4 (shifts Red <-> Blue)
    lambda_matrices[3] = np.array([[0, 0, 1], 
                                   [0, 0, 0], 
                                   [1, 0, 0]])
    
    # lambda_5 (complex phase shift Red <-> Blue)
    lambda_matrices[4] = np.array([[0, 0, -1j], 
                                   [0, 0, 0], 
                                   [1j, 0, 0]])
    
    # lambda_6 (shifts Green <-> Blue)
    lambda_matrices[5] = np.array([[0, 0, 0], 
                                   [0, 0, 1], 
                                   [0, 1, 0]])
    
    # lambda_7 (complex phase shift Green <-> Blue)
    lambda_matrices[6] = np.array([[0, 0, 0], 
                                   [0, -1j, 1], 
                                   [0, 1j, 0]]) # Corrected: The -1j should be on the off-diagonal
    lambda_matrices[6] = np.array([[0, 0, 0], 
                                   [0, 0, -1j], 
                                   [0, 1j, 0]])
    
    # lambda_8 (measures total color charge balance)
    lambda_matrices[7] = (1 / np.sqrt(3)) * np.array([[1, 0, 0], 
                                                      [0, 1, 0], 
                                                      [0, 0, -2]])
    
    return lambda_matrices



