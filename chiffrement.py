# massage entré, clé, message sortie : 24 bits 2^5 = 32


p = [0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23]
s = ['c', 5, 6, 'b', 9, 0, 'a', 'd', 3, 'e', 'f', 8, 4, 7, 1, 2]


def permutation(etat,p):

    n_etat = "0" * 24
    for i in range(24): 
        index = p[i]
        n_etat = n_etat[:int(index)] + str(etat[i]) + n_etat[int(index)+1:]
    return n_etat


def hex_to_bin(value):
    value = bin(int(value, 16))[2:].zfill(4)
    return value

def subtitution(etat,s):
    

    if len(etat) == 24:
        divise = [etat[i:i+4] for i in range(0, 24, 4)]
        etat = ''
        for i in range(len(divise)):
            divise[i] = str(s[int(divise[i], 2)])
            etat += hex_to_bin(divise[i])
        return etat
    else:
        sortie_S = str(s[int(etat,2)])
        # print("dans S :", sortie_S)
        sortie_S_bin = bin(int(sortie_S, 16))[2:].zfill(4)
        # print("convertion bin:",sortie_S_bin)
        return sortie_S_bin



def cadencement_cle(cle):
    """
    Pour sous cle ki =  k39 à k16, donc dans notre cas on prend l'indice 40 à 56 de notre registre
    Algo cadencement de clé pour 11 sous-clés de 24bits:
    1) pivot de 61 position [k18k17..k0k79..k20k19],
    2) Appli 4 bit gauche à la boite S, donc de l'indice 0 à 4 de notre registre 
    3) XOR de des bits 19-15 avec i le nombre de tours
    """
    sous_cles = []
    registre_hex = "0"*20
    registre_hex = str(cle) + registre_hex[6:]
    # print(registre_hex)

    # format binaire 
    registre = bin(int(registre_hex, 16))[2:].zfill(80)
    # print(registre)


    for i in range(1,12):

        # 1er sous clé 
        k = registre[40:64]
        sous_cles.append(k)

        # Etape 1)
        registre = registre[-19:] + registre[:61]
        # print(registre)

        # Etape 2)
        quatre_bits = registre[:4]
        # print("Les quatre bits les plus à gauche :", quatre_bits) 

        sub = subtitution(quatre_bits,s)

        registre = sub + registre[4:]
        # print("Etape 2:", registre)

        # Etape 3)
        r = int(registre[60:65], 2) ^ int(bin(i)[2:].zfill(5), 2)
        registre = registre[:60] + (bin(r)[2:].zfill(5)) + registre[65:]
        # print("Etape 3:", registre)

    return sous_cles
    
def chiffrement(message,cle):
    etat = message
    # print(bin(int(etat,16))[2:].zfill(24))
    sous_cles = cadencement_cle(cle)
    
    for i in range(10):

        etat = int(str(etat), 16) ^ int(sous_cles[i], 2)

        if len(str(etat)) < 24:
            etat = bin(etat)[2:].zfill(24)
        etat = subtitution(str(etat), s)
        etat = permutation(etat, p)
        etat = hex(int(etat, 2))
    # print(sous_cles[-1])
    # print(etat)
    etat = int(etat, 16) ^ int(sous_cles[-1], 2)
    etat = bin(etat)[2:].zfill(24)
    return etat


# print(chiffrement("f955b9", "d1bd2d"))
