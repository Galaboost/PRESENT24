from chiffrement import * 


_s = ['5', 'e', 'f', '8', 'c', '1', '2', 'd', 'b', '4', '6', '3', '0', '7', '9', 'a']
_p = [0, 4, 8, 12, 16, 20, 1, 5, 9, 13, 17, 21, 2, 6, 10, 14, 18, 22, 3, 7, 11, 15, 19, 23]


def dechiffrement(message, cle):
    """
    l'algo pour le dechiffrement:

    Etat ← Etat ⊕K11
    pour i = 1 jusqu’`a 10 faire
    Etat ← Permutation(Etat)
    Etat ← Substitution(Etat)
    Etat ← Etat ⊕Ki
    """

    etat = message
    sous_cles = cadencement_cle(cle)
    etat = int(etat, 16) ^ int(sous_cles[-1], 2)
    etat = bin(etat)[2:].zfill(24)

    for i in range(9,-1,-1):
        etat = permutation(etat, _p)
        etat = subtitution(str(etat), _s)
        etat = int(str(etat), 2) ^ int(sous_cles[i], 2)
        etat = (bin(etat)[2:].zfill(24))

    return etat


# print(dechiffrement("bb57e6", "000000"))
