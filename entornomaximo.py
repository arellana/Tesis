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

    pMin = np.where(aux[parametro] >= (maximo-delta))[0]

    cor = np.zeros((7,len(pMin)))
    
    for l in range(7):
        for j in range(len(pMin)):
            cor[l][j] = aux[l][pMin[j]]

    #plt.hist(e1Cor,bins=37)
    #sns.histplot(cor[4])
    return cor

# dat: trazas, parametro: indice de la posicion del parametro a ver, delta: "cuantos bines me corros a izq y derecha para colorear, 
# bina: cantidad de bines. 
# ploteo y conte deberian ser booleanos que me devuelvan o no los graficos y el conteo de cada maximo

def Maximo(dat, parametro, delta, bina, *ploteo, **conte): #Algun dia al pedo reviso los bools
    
    fig, ax = plt.subplots()

    N, bind, patches = ax.hist(dat[parametro], bins=bina, edgecolor='white', linewidth=1) #N es el conteo de cada uno, bins el extremo de cada bineado

    ind = np.where(N==N.max())
    maximo = bind[ind]


    print('Valor mas probable: '+str(bind[ind][0]))
    
    if (conte == True):
        print('Conteo maximo: ', N.max())
    else:
        pass

    for i in range(np.asarray(ind[0][0])-delta, np.asarray(ind[0][0])+delta+1):
        if i >= 0:
            patches[i].set_facecolor('orange')
    
    if (ploteo == False):
        plt.close()
        
    return bind[ind][0]
