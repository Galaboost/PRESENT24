#!/user/bin/python3

from chiffrement import * 
from dechiffrement import * 
import time 
import multiprocessing

# message de 24 bits, donc on aura 2**24 (16777216) de sous clés 


def calcul_lm(m, i):
    h = hex(int(str(i),10))
    return (chiffrement(m,h), i)

def calcul_lc(c, i):
    h = hex(int(str(i),10))
    return (dechiffrement(c,h), i)

def listes(m,c):
    """
    Je calcule en parallèle les liste lm et lc avec 4 processus, 2 pour chaque liste 
    """
    deb = time.time()

    pool = multiprocessing.Pool(4) # Créer une piscine de 4 processus
    lm1 = pool.starmap(calcul_lm, [(m, i) for i in range(0, 2**23)])
    lc1 = pool.starmap(calcul_lc, [(c, i) for i in range(0, 2**23)]) 
    lm2 = pool.starmap(calcul_lm, [(m, i) for i in range(2**23, 2**24)])
    lc2 = pool.starmap(calcul_lc, [(c, i) for i in range(2**23, 2**24)])
    pool.close()
    pool.join()
    lm = lm1 + lm2
    lc = lc1 + lc2

    lm.sort() # Trier lm
    lc.sort() # Trier lc

    fin = time.time()
    duree = fin - deb
    print("Ca a pris:", duree)

    return lm, lc

def commun(lm,lc,m2,c2):
    """
    Pour chercher les éléments communs on va faire une recherche en parallèle avec 2 pointeurs
    """
    colision = 0
    i, j = 0, 0
    k = []
    deb = time.time()
    while (i<2**24) and (j<2**24):
        
        if lm[i][0] < lc[j][0]:
            i += 1

        elif lm[i][0] > lc[j][0]:
            j += 1
        
        else:
            res_m = chiffrement(m2,lm[i][1])
            res_c = dechiffrement(c2,lc[j][1])
            colision += 1
            if res_m == res_c:
                k.append((lm[i][1],lc[j][1]))
            i += 1
            j += 1
    fin = time.time()
    duree = fin - deb
    print("pour chercher commun", duree)
    print("terminé avec succès")
    print(colision)
    return k


lm, lc =listes("3cfa0f","1cdcb2")

print(commun(lm,lc,"d5c434","df353e"))


# (m1,c1) = (3cfa0f, 1cdcb2) (m2,c2) = (d5c434,df353e)

# nb de colision : 4446466
# k1,k2 : (3984739, 5425154) 3CCD63 52C808