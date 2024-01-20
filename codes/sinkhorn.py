### Sinkhorn algorithm ### 

import numpy as np 

def sinkhorn(a, b, C, epsilon = 1e-3, max_iters = 1000):
    """ 
    Given two probabilities discrete distributions a and b and a cost matrix C, 
    finds the optimal matrix P
    """
    u = np.ones(len(a))
    v = np.ones(len(b))