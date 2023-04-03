# message de 24 bits, donc on aura 2**24 (16777216) de sous clés 

from chiffrement import * 
from dechiffrement import * 
import time 

def listes(m,c):
    """
    On génére 2 listes lm et lc pour stocker tous les sous-clés de m et c respectivement sous 
    forme de tuple (chiffré/claire, sous-clé).
    Puis on les trie par ordre croissant avant de les retourner
    """
    deb = time.time()

    lm = []
    lc = []
    for i in range(2**24):
        lm.append((chiffrement(m,i),i))
        lc.append((dechiffrement(c,i),i))
    lm.sort()
    lc.sort()

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
    print("terminé avec succès")
    print(colision)
    return k

lm,lc = listes("3cfa0f","1cdcb2")

print(commun(lm,lc,"d5c434","df353e"))


# (m1,c1) = (3cfa0f, 1cdcb2) (m2,c2) = (d5c434,df353e)

