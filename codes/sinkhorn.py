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

def algo1(u_0, v_0, W_0, delta_u2, delta_v2, delta_W2, max_iters = 1000): 
    "Algorithm 1 Random walk Metropolis within Gibbs"
    
    #First function to check if (x,y,Z) is in U
    def is_in_U(x,y,Z):
        if 0 <= x <= 1:
            if 0 <= y <= 1:
                if 0 <= Z <= 1: return True
                else: return False
            else: return None
        else: return None
    #Second function to compute the probability a((u,v,W),(x,y,Z))
    def a(u,v,W,x,y,Z):
        return None
    
    ## 
    u = [u_0]
    v = [v_0] 
    W = [W_0]
    for _ in range(max_iters):
        #u
        x = u[-1] + np.random.normal(0, np.sqrt(delta_u2))
        y = v[-1] 
        Z = W[-1] 
        if is_in_U(x,y,Z):
            if probability: 
                u.append(x)
                v.append(y)
                W.append(Z)
        #v
        x = u[-1] 
        y = v[-1] + np.random.normal(0, np.sqrt(delta_v2))
        Z = W[-1] 
        if is_in_U(x,y,Z):
            if probability: 
                u.append(x)
                v.append(y)
                W.append(Z)
        #W 
        x = u[-1] 
        y = v[-1] 
        Z = W[-1] + np.random.normal(0, np.sqrt(delta_W2))
        if is_in_U(x,y,Z):
            if probability: 
                u.append(x)
                v.append(y)
                W.append(Z)

    