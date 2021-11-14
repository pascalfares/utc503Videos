'''
En calculabilité, Un programme est aussi une donnée
'''

# Soit l'algorithme d'euclide pour le pgcd, écrit en Python

def pgcd(a,b):
    if a < b: 
        a,b=b,a
    while b: 
        a,b=b,a%b
    return a

print(pgcd(25,5), pgcd(35, 49), pgcd(34, 12))

# Un programme est une succession de caractère

pgm_de_pgcd = '''def pgcd(a,b):
    if a < b: 
        a,b=b,a
    while b: 
        a,b=b,a%b
    return a
'''

print("La chaîne de caractère pgm_de_pgcd est", pgm_de_pgcd, type(pgm_de_pgcd))

# Je peux maintenant créer un programme universel qui créer la fonction à partir 
# de la chaîne définissant la fonction 
# Et qui peut l'appeler avec certain paramètres

def universel(algo, *args):
    exec(algo)
    ligne1 = algo.split('\n')[0]
    nom = ligne1.split('(')[0][4:]
    print(f"La fonctions {nom} et les paramètres {args}")
    return eval(f"{nom}{args}")