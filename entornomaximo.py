# -*- coding: utf-8 -*-
"""entornoMaximo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15ImSKlGUGmJmXsC0hVD13lZYw5hsu54v
"""

#from google.colab import drive
#drive.mount('/content/drive')
#import sys
#sys.path.insert(0,'/content/drive/MyDrive/Colab Notebooks')
#from google.colab import files
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt

##### prueba #####

#ruta = '/content/drive/MyDrive/Tesis de Javi/DatosSimu/'+'HU2'+'-N='+str(50)+'-S='+str(10000)+'.txt'
#dat = np.loadtxt(ruta, delimiter=';')

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

    aux = np.zeros((7,len(pMax)))

    for k in range(7):
        for i in range(len(pMax)):
            aux[k][i] = dat[k][pMax[i]]

    #sns.histplot(aux[4],bins=100)

    pMin = np.where(aux[4] >= (maximo-delta))[0]

    cor = np.zeros((7,len(pMin)))
    
    for l in range(7):
        for j in range(len(pMin)):
            cor[l][j] = aux[l][pMin[j]]

    #plt.hist(e1Cor,bins=37)
    #sns.histplot(cor[4])
    return cor

#cortados = entornoMaximo(dat,4,0.0025,134)

#sns.histplot(cortados[4],bins=37)