###  MH with Gibbs  ### 

import numpy as np 
import ot 
np.random.seed(123)
n = 10**5

def KL_divergence(T, K):
    # Kullback Leibler divergence
    log_T_K = np.log(T / K)
    return np.trace(np.dot(log_T_K, np.transpose(T))) - np.trace(T) - np.trace(K)


def MH_gibbs(T, sigma2 = 0.04, max_iters = 1000, epsilon = 1e-3): 
    "Algorithm 1 Random walk Metropolis within Gibbs"
    N = T.shape[0]
    #Initialization
    U, V, C = np.zeros((n, N)), np.zeros((n, N)), np.zeros((n, N, N))
    U[0] = np.random.uniform(size=N)
    V[0] = np.random.uniform(size=N)
    C[0, :, :] = np.random.uniform(size=(N, N))

    #First function to check if (x,y,Z) is in U (hypercube)
    def is_in_U(x,y,Z):
        if 0 <= x <= 1:
            if 0 <= y <= 1:
                if 0 <= Z <= 1: return True
                else: return False
            else: return False
        else: return False

    #Second function to compute the probability a((u,v,W),(x,y,Z))
    def a(u,v,W,x,y,Z, T):
        transport1 = ot.emd(u, v, W)
        transport2 = ot.emd(x, y, Z)
        norme1 = np.linalg.norm(T - transport1)
        norme2 = np.linalg.norm(T - transport2)
        return min(1, np.exp((norme1 - norme2) / sigma2))
    
    # Random vectors
    e_u = np.random.normal(0, 0.02, (N, n))
    e_v = np.random.normal(0, 0.02, (N, n))
    e_C = np.random.normal(0, 0.04, (N, N, n))

    u_u = np.log(np.random.uniform(size=n))
    u_v = np.log(np.random.uniform(size=n))
    u_c = np.log(np.random.uniform(size=n))
    
    for k in range(n-1):
        #u
        x, y, Z = U[k] + e_u[:, k], V[k], C[k]
        if not is_in_U(x, y, Z):
            U[k+1], V[k+1], C[k+1] = U[k], V[k], C[k]
        else:
            if u_u[k] < a(U[k], V[k], C[k], x, y, Z,T):
                U[k+1], V[k+1], C[k+1] = x, y, Z
            else:
                U[k+1], V[k+1], C[k+1] = U[k], V[k], C[k]
        UK = U[k+1]

        #v
        x, y, Z = UK, V[k] + e_v[:, k], C[k]
        if not is_in_U(x, y, Z):
            U[k+1], V[k+1], C[k+1] = UK, V[k], C[k]
        else:
            if u_v[k] < a(UK, V[k], C[k], x, y, Z,T):
                U[k+1], V[k+1], C[k+1] = x, y, Z
            else:
                U[k+1], V[k+1], C[k+1] = UK, V[k], C[k]
        VK = V[k+1]

        #W 
        x, y, Z = UK, VK, C[k] + e_C[:, :, k]
        if not is_in_U(x, y, Z):
            U[k+1], V[k+1], C[k+1] = UK, VK, C[k]
        else:
            if u_c[k] < a(U[k], V[k], C[k], x, y, Z,T):
                U[k+1], V[k+1], C[k+1] = x, y, Z
            else:
                U[k+1], V[k+1], C[k+1] = UK, VK, C[k]

        return U, V, C

    