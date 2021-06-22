# -*- coding: utf-8 -*-
"""entornoMaximo.ipynb

Original file is located at
    https://colab.research.google.com/drive/15ImSKlGUGmJmXsC0hVD13lZYw5hsu54v
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def entornoMaximo(dat, parametro, delta, bin): 
    
    b = plt.hist(dat[parametro],bins=bin)
    plt.title('Histograma a recortar')
 
    y = np.asarray(b[0])
    x = np.asarray(b[1])
 
    ind = np.where(y==y.max())
    maximo = x[ind]
 
    print('Valor mas probable: '+str(x[ind][0]))
    print('Conteo maximo: ', y.max())
 
    #parametro es el indice del parametro sobre el que quiero acotar (ej: l1 = 4)
    pMax = np.where(dat[parametro] <= (maximo+delta))[0]#, l1 >= (maximo-delta))
 
    aux = np.zeros((len(dat),len(pMax)))
 
    for k in range(len(dat)):
        for i in range(len(pMax)):
            aux[k][i] = dat[k][pMax[i]]
 
    #sns.histplot(aux[4],bins=100)
 
    pMin = np.where(aux[parametro] >= (maximo-delta))[0]
 
    cor = np.zeros((7,len(pMin)))
    
    for l in range(len(dat)):
        for j in range(len(pMin)):
            cor[l][j] = aux[l][pMin[j]]
    #binsns = int(binsns)
    plt.hist(cor[parametro],label='recortado')
    plt.legend()
    #sns.histplot(cor[4])
   
    return cor,x[ind][0], y.max()