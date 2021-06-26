import numpy as np
from numpy import pi, sqrt, sin, cos, exp, log10, array, real, conj
import cuentitas

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

def medicion(zona):     #angulo - observacion - nombre
    if zona == 'VP1':
        out = [np.asarray([20.44, 18.79, 17.36]),np.asarray([-6.13, -5.71, -5.66, 0.927])]
    elif zona == 'VP2':
        out = [np.asarray([18.63, 17.19, 11.25]),np.asarray([-6.65, -6.17, -5.93, 0.937])]
    elif zona == 'HU0':
        out = [np.asarray([24.59, 15.76, 20.69]),np.asarray([-4.07, -3.27, -3.59, 0.917])]
    elif zona == 'HU1':
        out = [np.asarray([22.46, 15.33, 15.57]),np.asarray([-3.64, -3.12, -2.90, 0.921])]
    elif zona == 'HU2':
        out = [np.asarray([18.86, 21.10, 12.98]),np.asarray([-4.08, -9.34, -3.55, 0.914])]
    elif zona == 'DU1':
        out = [np.asarray([17.20, 20.10, 12.98]),np.asarray([-9.02, -9.55, -8.09, 0.943])]
    elif zona == 'DU2':
        out = [np.asarray([23.84, 11.21, 12.64]),np.asarray([-11.96, -6.82, -7.99, 0.954])]
    elif zona == 'DP1':
        out = [np.asarray([19.64, 17.76, 14.06]),np.asarray([-7.79, -8.34, -7.44, 0.947])]
    elif zona == 'DP2':
        out = [np.asarray([24.21, 13.78, 16.76]),np.asarray([-11.25, -8.29, -8.62, 0.937])]
    else:
      print('\n Inputs: VP1, VP2, HU0, HU1, HU2, DU1, DU2, DP1, DP2 \n')
    
    return out

def sigma(ep1,ep2,d,s1,l1,s2,l2,angulo): #funcion de antes pero sin la parte tensorial
    landa = 0.025
    k0 = 2*np.pi/landa
    phi = np.pi
    ### s0
    phs = phi + np.pi
    thi = angulo  #cambiar segun la zona
    thi = thi*np.pi/180 #DU2 T008, T061, T021
    ths = thi
    k1 = k0*(sin(ths)*cos(phs)-sin(thi)*cos(phi))
    k2 = k0*(sin(ths)*sin(phs)-sin(thi)*sin(phi))
    
    a1f1 = cuentitas.a1VVF1(k0,thi,phi,ths,phs,ep1,ep2,d)
    a1f2 = cuentitas.a1VVF2(k0,thi,phi,ths,phs,ep1,ep2,d)

    w1 = cuentitas.w(s1,l1,k1,k2)
    w2 = cuentitas.w(s2,l2,k1,k2)
    w12 = cuentitas.w_f1f2(s1,l1,s2,l2,k1,k2)
    
    aux=4*np.pi*k0**2*cos(ths)**2*(abs(a1f1)**2*w1+abs(a1f2)**2*w2+2*real(a1f1*conj(a1f2))*w12)
    
    s0s = 10*np.log10(aux)

    return s0s