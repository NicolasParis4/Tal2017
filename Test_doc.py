# -*- coding: utf-8 -*-

from __future__ import division

import nltk
import os
import numpy
import nltk.corpus  
from nltk.text import Text
import re
#from nltk import FreqDist


# sélection du corpus (1ere méthode) [instancier sous la forme d'un objet texte] 
#coller le corpus dans /home/lucille/nltk_data/corpora/gutenberg
text = Text(nltk.corpus.gutenberg.words('corpus.txt'))
#Affichage de l'objet :
print(text)

with open('corpus2.txt', 'r') as f:
    sample = f.read()
#Affichage de l'objet sample : print(sample)

#Quelques fonctions utiles

#Chercher un mot dans son contexte d'apparition : 
text.concordance("murder")

#Chercher les mots qui apparaissent dans le même contexte :
text.similar("murder")

#Chercher un ou plusieurs mots partageant un contexte commun (s'appuyer sur la fonction
#précèdente pour les choisir):
text.common_contexts(["murder", "men"])

#nombre de mots du texte : 
num = len(text)
print(num)

#nombre de typologie distincte de mots 
set1 = len(set(text))
print(set1)

#Compter les occurrences de certains mots dans le corpus et calculer un indicateur: 
count = text.count("men")
count2=  100 * text.count('a')/len(text)
print(count2)
print(count)


#Afficher un mot du corpus selon sa position :
mot = text[230]
print(mot)

#Fréquence des mots du texte : 
fdist1 = FreqDist(text)
print(fdist1)
fdist2 = fdist1.most_common(50)
print(fdist2)

#text=str(text)
tokens = nltk.word_tokenize(text)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)


#Ancien Projet_TAL.py (je vais nettoyer)

# sélection du corpus (1ere méthode) [instancier sous la forme d'un objet texte] 
#coller le corpus dans /home/lucille/nltk_data/corpora/gutenberg
text = Text(nltk.corpus.gutenberg.words('corpus.txt'))
#Affichage de l'objet : print(text)

#sélection du corpus (2e méthode)
os.chdir("/home/lucille/Bureau/sciences co/Projets/TAL/Projet_TAL")
f = open("corpus2.txt", "r")
raw = f.read()
#pour afficher le corpus : 
#print(raw)
#tentative de le convertir sous la forme d'un objet texte :
#text2=Text(raw)
# Affichage de l'objet : print(text2)
#Cela fonctionne mais les caractères sont espacés et donc il ne matche rien quand on
#utilise des fonctions prenant en paramètres des objets textes (vous pouvez chercher comment
#résoudre le problème si vous le souhaitez)

#3e alternative :
with open('corpus2.txt', 'r') as f:
    sample = f.read()
sample = unicode(sample, errors='ignore')


#ATTENTION : NE TRAVAILLER QU'AVEC "TEXT" (problème d'encodage des mots avec raw)
tokens = nltk.word_tokenize(sample)
#print(tokens)


