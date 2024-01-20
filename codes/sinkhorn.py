### Sinkhorn algorithm ### 

import numpy as np 

def KL_divergence(T, K):
    # Kullback Leibler divergence
    log_T_K = np.log(T / K)
    return np.trace(np.dot(log_T_K, np.transpose(T))) - np.trace(T) - np.trace(K)

def diff_matrix(A,B):
    "Finds if two matrix of same size are different"
    if A.shape != B.shape:
        print("Matrix have different sizes")
    else: 
        lines = A.shape[0]
        columns = A.shape[1]
        for i in range(lines):
            for j in range(lines):
                if A[i,j] != B[i,j]:
                    return True
        return False

def sinkhorn(a, b, C, epsilon = 1e-3, max_iters = 10000):
    """ 
    Given two probabilities discrete distributions a and b and a cost matrix C, 
    finds the optimal matrix T
    """
    u = np.ones(len(a))
    v = np.ones(len(b))
    K = np.exp( - C / epsilon)
    T = np.dot(np.dot(np.diag(u), K), np.diag(v))

    for _ in range(max_iters):
        u = a / np.dot(K, v)
        v = b / np.dot(np.transpose(K), u)
        Proposition_T = np.dot(np.dot(np.diag(u), K), np.diag(v))
        if diff_matrix(T, Proposition_T):
            Proposition_T = T
        else: 
            return T 
    return False