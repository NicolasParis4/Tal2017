# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

import nltk
import nltk.data
import os
import numpy
from nltk.text import Text
import re
import sys
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords
import string
import pickle

#NB : utiliser seulement corpus.txt, c'est le seul fichier encodé correctement

#Importation du corpus (n'oubliez pas de modifier votre chemin) :
os.chdir("/home/lucille/Tal2017")
with open('corpus.txt', 'r') as f:
    sample = f.read()

#Ouverture d'un fichier texte où sera stocké le texte du 2e corpus :
fichier = open('Corpus_2.txt', 'w')

#Ouverture du lexique :
os.chdir("/home/lucille/Tal2017")
with open('Lexique.txt','r') as l:
    lexique=l.read()

#Ouverture de la liste des tueurs :
os.chdir("/home/lucille/Tal2017")
with open('Tueurs.txt','r') as t:
    tueurs=t.read()

#TOKENIZATION
#Docs : ntlk.org ; module tokenize regexp ; nltk data 

#Tokenization en phrases
tokenizer_P=nltk.data.load('tokenizers/punkt/PY3/english.pickle')
tokens_P=tokenizer_P.tokenize(sample)
print("Le fichier contient "+str(len(tokens_P))+" phrases")

#Tokenization du lexique en mots :
tokenizer_W2 = TreebankWordTokenizer()
tokens_lexique=tokenizer_W2.tokenize(lexique)
#ATTENTION maintenant, le lexique s'appelle tokens_lexique.

#Tokenization de la liste des tueurs en mots :
tokenizer_W2 = TreebankWordTokenizer()
tokens_tueur=tokenizer_W2.tokenize(tueurs)
#ATTENTION maintenant, la liste des tueurs s'appelle tokens_tueur.

tokens_lexique.extend(tokens_tueur)

#Removing punctuation
#Corpus sans ponctuation : 
print("Punctuation loop")
i=0
corpus2=[]
taille=len(tokens_P)
for phrase in tokens_P:
    liste=phrase.strip(string.punctuation)
    corpus2.append(liste)

#fonction recherche/impression de phrase
#elle retourne la phrase (du corpus) qui contient le mot keyWords en paramètre
#ATTENTION pour l'utiliser, le keyWord doit être une string et le corpus doit être segmenté à phrase ! 
def recherche(corpus,keyWord):
        for phrase in corpus:
            if(phrase.find(keyWord, 0)!=-1):
                return phrase
        return ''


#Cette fonction retourne à partir d'une liste de mots, toutes les phrases d'un corpus
#Elle prend en paramètre un corpus et une liste de mots.

def generateur_corpus2(corpus, liste):
    resultat=[]
    for mot in liste:
        phrase=recherche(corpus,mot)
        if(len(phrase)>0):
            resultat.append(phrase)
    return resultat

expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
re.search(expression, chaine)

corpus3=generateur_corpus2(corpus2,tokens_lexique)
corpus3=str(corpus3)

fichier.write(corpus3)
fichier.close()
        

#Tokenisation du texte en mots à l'aide de TreeBankTokenizer
#ce tokenizer utilise aussi des expressions régulières 
tokenizer_W2 = TreebankWordTokenizer()
tokens_W2=tokenizer_W2.tokenize(sample)
print("Le fichier contient "+str(len(tokens_W2))+" mots")

#Tokenisation du texte découpé en phrase ET en mots :
tokens_P=str(tokens_P)
tokens_W3=tokenizer_W2.tokenize(tokens_P)
print("Le fichier contient "+str(len(tokens_W3))+" mots")

#ATTENTION !!! Le corpus s'appelle maintenant text : 
text=tokens_W3

#----------------------------------------
#Partie utile à la constitution du lexique :
#L'idée est d'enlever les stopwords du corpus, pour ensuite en extraire les mots les plus fréquents à inclure dans les mots clés. 

# chargement des stopwords anglais
english_stopwords = set(stopwords.words('english'))
# un filtre de stopwords pour ensuite récupérer les mots les plus fréquents (je me sers du corpus tokens_W3 pour éviter de modifier le corpus "text"
tokens_W3 = [token for token in tokens_W3 if token.lower() not in english_stopwords]

#Extraction des mots les plus fréquents du texte :
fdist1 = FreqDist(tokens_W3)
fdist2 = fdist1.most_common(100)
#Affichage de ces mots les plus fréquents : print(fdist2)

#--------------------------------------------------------------
#Doc utile : 

#Fonction de concordance
#text=Text(text)
#text.concordance("murder")


#Tokenization en mots à l'aide d'une expression régulière
#Attention cette manière de procéder, considère la ponctuation et caractères
# non alphabétiques comme des mots
tokenizer_W = RegexpTokenizer('\w+|[^\w\s]+')
tokens_W=tokenizer_W.tokenize(sample)
# Affichage du résultat : print(len(tokens_W))
#NE PAS UTILISER, ne pas supprimer, on le garde pour l'exemple (cf. rapport).



#Test sans ponctuation :
#print("Message2")
bla="J'aime les confitures. C'est très bon."
tokens_P1=tokenizer_P.tokenize(bla)
#print(tokens_P1)
bla3=[]
for phrase in tokens_P1:
    bla2=phrase.strip(string.punctuation)
    bla3.append(bla2)
#print(bla3)

#print("Message 3")
#print(recherche(bla3,"bon"))
liste=["confitures", "poisson", "monstre", "bon"]
test=[]
resultat2=[]
for mot in liste:
    test=recherche(bla3,mot)
    print(test+" len("+str(len(test))+")")
    if(len(test)>0):
        resultat2.append(test)
#print(resultat2)
