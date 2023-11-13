# Créé par Marin, le 12/11/2023 en Python 3.7
from collections import Counter
import re

def compter_occurrences_mots(texte):
    texte = texte.lower()
    mots = re.findall(r'\w+', texte)
    compteur_mots = Counter(mots)
    mots_tries = sorted(compteur_mots.items(), key=lambda x: x[1], reverse=True)
    return mots_tries
# Etape1 : Cette partie compte le nombre de fois que le mot apparer dans le texte

def filtrer_mots_parasites(structure_donnees, mots_parasites):
    mots_parasites = set(mots_parasites)
    structure_filtree = [(mot, occ) for mot, occ in structure_donnees if mot not in mots_parasites]
    return structure_filtree
# Etape2 : Cette partie filtre les mot parasite
import csv

def recuperer_mots_parasites_avec_fichier_csv(nom_fichier):
    mots_parasites = []
    with open(nom_fichier, newline='') as fichier_csv:
        lecteur = csv.reader(fichier_csv)
        for ligne in lecteur:
            mots_parasites.extend(ligne)
    return mots_parasites

import csv
# Etape3 : Cette partie permet de crée un fichier avec la liste des mots parasite
# Liste de mots parasites
mots_parasites = [
    'le', 'l' 'la', 'les', 'de', 'du', 'des', 'un', 'une', 'et', 'ou', 'est', 'sont', 'je', 'tu', 'il', 'elle', 'nous', 'vous',
    'ils', 'elles', 'ce', 'cette', 'ces', 'se', 'sa', 'son', 'leur', 'leurs', 'avec', 'pour', 'sur', 'sous', 'dans', 'en', 'par',
    'au', 'aux', 'je suis', 'tu es', 'il est', 'elle est', 'nous sommes', 'vous êtes', 'ils sont', 'elles sont', 'ceci', 'cela'
]

# Nom du fichier CSV à créer
nom_fichier = 'parasite.csv'

# Écriture de la liste dans le fichier CSV
with open(nom_fichier, 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    for mot in mots_parasites:
        writer.writerow([mot])




 #Étape 1 : Compter les occurrences des mots dans le texte
def obtenir_mots_clefs(texte):
    occurrences_mots = compter_occurrences_mots(texte)

    # Étape 3 : Récupérer les mots parasites depuis un fichier CSV
    fichier_mots_parasites = "parasite.csv"
    mots_parasites = recuperer_mots_parasites_avec_fichier_csv(fichier_mots_parasites)

    # Étape 2 : Filtrer les mots parasites de la structure de données
    mots_clefs = filtrer_mots_parasites(occurrences_mots, mots_parasites)

    return mots_clefs

# Testez votre fonction avec un texte assez long
texte_long = "le jeux vidéo est le meilleur univers du monde du monde"
resultat_mots_clefs = obtenir_mots_clefs(texte_long)
print(resultat_mots_clefs)
