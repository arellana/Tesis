import numpy as np

def integracionGauss(n): 
# Precalculamos nodos y pesos (única vez para todas las integrales
    beta = np.zeros(n,dtype=float)
    for k in range(1,n+1):
        beta[k-1] = 0.5/np.sqrt(1-(2*(k))**(-2))

    m = n+1
    T_low = np.zeros((m,m))
    T_up = np.zeros((m,m))
    T = np.zeros((m,m))
    
    # defino T_low
    for i in range(0,m):
        for j in range(0,m):
            if i==j+1:
                T_low[i,j]=beta[i-1]

    # defino T_up
    for i in range(0,m):
        for j in range(0,m):
            if j==i+1:
                T_up[i,j]=beta[i]


    T = T_low + T_up        
    d_,V = np.linalg.eig(T)
    D = np.zeros((m,m))
 
    for i in range(0,m):
        for j in range(0,m):
            if i==j:
                D[i,j]=d_[i]

    W = (2*V[0,:]**2)
    Wt = np.kron(W,W)

    X,Y = np.meshgrid(d_,d_)
    return X,Y,Wt