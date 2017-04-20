# -*- coding: utf-8 -*-

import nltk
import os
import nltk.corpus  
from nltk.text import Text
from nltk.corpus import wordnet as wn

#N'oubliez pas de changer le chemin du fichier à votre convenance : 
os.chdir("/home/lucille/Tal2017")
fichier = open('Lexique.txt', 'w')

#Fonction qui permet d'obtenir la liste entière des hyponymes du synset d'un lemme
def get_all_hypo(keyWord):
    hypo=list(set([w for s in keyWord.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))
    return hypo

#Nb : Le paramètre keyWord est le synset du mot dont vous cherchez les hyponymes


#MOTS CLES :

#Killer (nom) 
killer=wn.synset('killer.n.01')
#extraction des lemmes des synsets :
killer1=killer.lemma_names()
#extraction des hyponymes : 
killer2=get_all_hypo(killer)

#création d'une liste fusionnée :
killer1.extend(killer2)


#Kill (verbe) : 
kill=wn.synset('kill.v.01')
#je n'ai pas trouvé comment extraire les lemmes synonymes du verbe (si vous voulez chercher)
kill_1=kill.lemmas()
print(kill)
#extraction des hyponymes : 
kill_2=get_all_hypo(kill)

#création d'un liste fusionnée:
killer1.extend(kill_2)

#Crime (nom) : 
crime = wn.synset('crime.n.01')
#extraction de lemmes synonymes :
crime1=crime.lemma_names()
#extraction d'hyponymes :
crime2=get_all_hypo(crime)

#gestion de la liste :
crime1.extend(crime2)
killer1.extend(crime1)

#Génocide :
genocide=wn.synset('genocide.n.01')
#extraction de lemmes synonymes :
genocide1=genocide.lemma_names()
#les hyponymes de génocide ne donnent pas de résultat
killer1.extend(genocide1)

#Sentence (sens 2, nom) : 
sentence=wn.synset('condemnation.n.02')
#Lemmes synonymes : 
sentence1=sentence.lemma_names()
#Lemmes hyponymes :
sentence2=get_all_hypo(sentence)

sentence1.extend(sentence2)
killer1.extend(sentence1)

#Rampage (nom)
rampage=wn.synset('rampage.n.01')
rampage1=rampage.lemma_names()
rampage2=get_all_hypo(rampage)
rampage1.extend(rampage2)
killer1.extend(rampage2)

print(killer1)

for mot in killer1:
    fichier.write(mot+' ')

#killer1=str(killer1)

#fichier.write(killer1)
fichier.close()

#Fonction qui permet de récupérer les lemmes de tous les hypernymes d'un synset
# NB : pas très utile car extrait des termes trop généralistes pour le but qui est le nôtre
def get_all_hyper(keyWord):
    hyper=list(set([w for s in keyWord.closure(lambda s:s.hypernyms()) for w in s.lemma_names()]))
    return hyper

#Fonction get_all_hyper test 
#killer6=get_all_hyper(killer)
#print(killer6)

#Il s'agit de la même fonction que get_all_hypo, sauf qu'elle génère tous les synsets (et non les lemmes)
def get_hyponyms(synset):
    hyponyms = set()
    for hyponym in synset.hyponyms():
        hyponyms |= set(get_hyponyms(hyponym))
    return hyponyms | set(synset.hyponyms())
#test de la fonction :
#killer4=get_hyponyms(killer)
#print(killer4)

#récupérer les objets d'une liste wordNet
#for lettre in killer1:
    #print(killer1)
