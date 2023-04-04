from chiffrement import * 
#!/user/bin/python3

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



if __name__ == "__main__":
    print("--------test de la fonction déchiffrement-------")
    msg_clair = "f955b9"
    cle = "d1bd2d"

    print("Je chiffre {} avec la clé {}".format(msg_clair, cle))
    c = chiffrement(msg_clair, cle)
    c = hex(int(c,2))[2:]
    print("Le résultat du chiffrement :", c)
    print("Je le déchiffre")
    d = dechiffrement(c,cle)
    if hex(int(d, 2))[2:] == msg_clair:
        print(hex(int(d, 2))[2:], "=", msg_clair, "Ca fonctionne !")
    else:
        print("Erreur")
