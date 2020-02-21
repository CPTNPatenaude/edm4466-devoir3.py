# coding : utf-8

#ce code permet de creer un csv avec tous les urls des archives du site actualite.uqam

#commandes de bases pour le log-in et la creation du csv

import requests, csv
from bs4 import BeautifulSoup

#liste des urls des articles
contenu = list()

#creation d'une entête
entetes = {
    "User-Agent":"Francois-Alexis Favreau:Étudiant journalisme UQAM"
}

#boucle pour consulter toutes les pages d'archives (576 au moment de realiser ce travail)
for i in range(0, 576):

    #test pour definir l'url de la page suivante
    if i == 0:
        url = "https://www.actualites.uqam.ca/toutes-les-archives"
    elif i > 0:
        url = "https://www.actualites.uqam.ca/toutes-les-archives?page={}".format(i)

#vérification qua chaque page fonctionne
    print(url)


    page = requests.get(url, headers=entetes)
    print("Les articles de cette page se retrouvent dans la liste")
    soup = BeautifulSoup(page.text, 'html.parser')

    #vérification du statut, 200=ok
    #print(page.status_code)

    #view-content contient le corps de la page
    article = soup.find(class_="view-content")
    #on va chercher les titres
    titres = article.find_all("h4")

    #pour chaque titre, aller chercher le href (url)
    for titre in titres:
        elem = titre.find('a')
        lien = elem.get('href')
        contenu.append(lien)
    
#creation d'un csv qui contient chaque url
with open('archives.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for occ in contenu:
        writer.writerow([occ])

print("Les articles se retrouvent dans archives.csv")
