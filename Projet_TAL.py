# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

import nltk
import os
import numpy
import nltk.corpus
from nltk.text import Text
import re
import sys

#NB : utiliser seulement corpus.txt, c'est le seul fichier encodé correctement

#Importation du fichier :
#os.chdir("/Users/workplace/Documents/Tal2017")
#with open('corpus.txt', 'r') as f:
#   sample = f.read()

folder = nltk.data.find("/Users/workplace/Documents/Tal2017")
corpusReader = nltk.corpus.PlaintextCorpusReader(folder, 'corpus.txt')

#Tokenization en phrases :
nb_sentences = len(corpusReader.sents())
print("le fichier contient "+ str(nb_sentences) +" phrases")

#Tokenization en paragraphs :
nb_paragraphs = len(corpusReader.paras())
print("le fichier contient "+ str(nb_sentences) +" paragraphs")

#Tokenization en mots :
nb_words=len([word for sentence in corpusReader.sents() for word in sentence])
print("Le fichier contient "+ str(nb_words) +" mots.")

#Tokenization en caractaires :
nb_chars=len([char for sentence in corpusReader.sents() for word in sentence for char in word])
print("Le fichier contient "+ str(nb_chars) +" caractères.\n")



#Exécution d'une fonction de concordance : 
#liste=Text(liste)
#liste.concordance("murder")

