# Créé par Marin, le 13/11/2023 en Python 3.7
#Etape pour faire l'audite de la page
import requests
from bs4 import BeautifulSoup
from collections import Counter

def recuperer_contenu_html(url):
    try:
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse.text
        else:
            print("Impossible de récupérer le contenu de la page.")
            return None
    except requests.RequestException as e:
        print("Une erreur est survenue :", e)
        return None

def audit_page():
    url = input("Entrez l'URL de la page à analyser : ")
    contenu_html = recuperer_contenu_html(url)

    if contenu_html:
        soup = BeautifulSoup(contenu_html, 'html.parser')

        # Récupération des mots clés avec occurrences
        mots = soup.get_text(separator=' ').split()
        mots_cles = dict(Counter(mots).most_common(3))

        # Récupération des liens dans la page
        liens = [link.get('href') for link in soup.find_all('a')]
        liens_entrants = [lien for lien in liens if lien and url in lien]
        liens_sortants = [lien for lien in liens if lien and lien.startswith('http')]

        # Vérification de la présence de balises alt
        balises_img = soup.find_all('img')
        presence_alt = any(img.get('alt') for img in balises_img)

        # Affichage des résultats
        print("Mots clés avec occurrences :", mots_cles)
        print("Nombre de liens entrants :", len(liens_entrants))
        print("Nombre de liens sortants :", len(liens_sortants))
        print("Présence de balises alt :", "Oui" if presence_alt else "Non")

audit_page()

