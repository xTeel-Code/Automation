import numpy as np
def mapGen(x,y):
    matica = np.random.rand(x,y)
    rnd_matica = np.round(matica)

    vyber_cisel = int(0.72*matica.size)
    pozicieNaZmenu = np.random.choice(matica.size, vyber_cisel, replace=False)
    maticaFlat = matica.flatten()
    maticaFlat[pozicieNaZmenu] = 0
    matica = maticaFlat.reshape(matica.shape)
    rndMatica = np.round(matica)
    return rndMatica



