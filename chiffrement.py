#!/user/bin/python3

# massage entré, clé, message sortie : 24 bits 2^5 = 32

p = [0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23]
s = ['c', 5, 6, 'b', 9, 0, 'a', 'd', 3, 'e', 'f', 8, 4, 7, 1, 2]


def hex_to_bin(value,bit):
    value = bin(int(value, 16))[2:].zfill(bit)
    return value

def permutation(etat, p):
    n_etat = ["0"] * 24

    for i in range(24):
        index = p[i]
        n_etat[index] = etat[i]
    return "".join(n_etat)


def subtitution(etat, s):
    if len(etat) == 24:
        l = [etat[i:i+4] for i in range(0, 24, 4)]
        result = ''.join([hex_to_bin(str(s[int(block, 2)]), 4) for block in l])
        return result
    else:
        return hex_to_bin(str(s[int(etat, 2)]), 4)


def cadencement_cle(cle):
    """
    Pour sous cle ki =  k39 à k16, donc dans notre cas on prend l'indice 40 à 56 de notre registre
    Algo cadencement de clé pour 11 sous-clés de 24bits:
    1) pivot de 61 position [k18k17..k0k79..k20k19],
    2) Appli 4 bit gauche à la boite S, donc de l'indice 0 à 4 de notre registre 
    3) XOR de des bits 19-15 avec i le nombre de tours
    """
    sous_cles = []
    
    registre = bin(int(str(cle),16))[2:].zfill(20) + "0"*60

    for i in range(1,12):

        # sous clés 
        k = registre[40:64]
        sous_cles.append(k)

        # Etape 1)
        registre = registre[-19:] + registre[:61]

        # Etape 2)
        quatre_bits = registre[:4]
        sub = subtitution(quatre_bits,s)
        registre = sub + registre[4:]

        # Etape 3)
        r = int(registre[60:65], 2) ^ int(bin(i), 2)
        registre = registre[:60] + (bin(r)[2:].zfill(5)) + registre[65:]

    return sous_cles
    
def chiffrement(message,cle):
    etat = message
    sous_cles = cadencement_cle(cle)
    
    for i in range(10):
        etat = int(str(etat), 16) ^ int(sous_cles[i], 2)
        if len(str(etat)) < 24:
            etat = bin(etat)[2:].zfill(24)
        etat = subtitution(str(etat), s)
        etat = permutation(etat, p)
        etat = hex(int(etat, 2))
    etat = int(etat, 16) ^ int(sous_cles[-1], 2)
    etat = bin(etat)[2:].zfill(24)
    return etat


def test(c,message_chiffre):
    c = hex(int(c, 2))[2:]
    if c == message_chiffre:
        print("Validé : ", message_chiffre)
    else:
        print("Erreur on trouve pas le même message chiffré")

if __name__ == "__main__":
    v = "000000"
    v1 = "ffffff"
    v2 = "f955b9"
    v3 = "d1bd2d"
    b = "bb57e6"

    a = chiffrement(v, v)
    b = chiffrement(v1, v)
    c = chiffrement(v, v1)
    d = chiffrement(v2, v3)

    test(a, "bb57e6")
    test(b, "739293")
    test(c, "1b56ce")
    test(d, "47a929")