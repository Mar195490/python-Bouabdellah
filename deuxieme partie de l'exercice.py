# Créé par Marin, le 13/11/2023 en Python 3.7

#Etape5 : Suppretion des balise HTML
from bs4 import BeautifulSoup

def supprimer_balises_html(texte_html):
    soup = BeautifulSoup(texte_html, 'html.parser')
    texte_sans_html = soup.get_text(separator=' ')
    return texte_sans_html

#Etape 6 : Récupérer les valeurs associées à une balise et un attribut
from bs4 import BeautifulSoup

def valeurs_attribut_dans_balises(texte_html, nom_balise, nom_attribut):
    soup = BeautifulSoup(texte_html, 'html.parser')
    balises = soup.find_all(nom_balise)
    valeurs = [balise.get(nom_attribut) for balise in balises if balise.get(nom_attribut)]
    return valeurs

# Code HTML pour faire un teste
code_html = '''
<html>
<body>
    <img src="image1.jpg" alt="Description de l'image 1">
    <img src="image2.jpg" alt="Description de l'image 2">
    <a href="lien1">Lien 1</a>
    <a href="lien2">Lien 2</a>
</body>
</html>
'''

# Tester pour faire la récupération des valeurs des attributs alt des balises img
valeurs_alt = valeurs_attribut_dans_balises(code_html, 'img', 'alt')
print("Attribut alt des balises img :", valeurs_alt)

# Tester pour récupérer les valeurs des attributs href des balises a
valeurs_href = valeurs_attribut_dans_balises(code_html, 'a', 'href')
print("Attribut href des balises a :", valeurs_href)

#Etape 8 : Extraction du nom de domaine à partir d'une URL
from urllib.parse import urlparse

def nom_de_domaine_de_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

#Etape 9 : Filtration des URL par nom de domaine
def filtrer_urls_par_domaine(nom_domaine, liste_urls):
    urls_du_domaine = [url for url in liste_urls if nom_de_domaine_de_url(url) == nom_domaine]
    urls_pas_du_domaine = [url for url in liste_urls if nom_de_domaine_de_url(url) != nom_domaine]
    return urls_du_domaine, urls_pas_du_domaine

#Etape 10 : Récupération du contenu HTML à partir d'une URL
import requests

def recuperer_contenu_html(url):
    reponse = requests.get(url)
    if reponse.status_code == 200:
        contenu_html = reponse.text
        return contenu_html
    else:
        return None
