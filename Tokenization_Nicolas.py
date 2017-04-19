from __future__ import unicode_literals

import nltk
import os
import numpy
import nltk.corpus
from nltk.text import Text
import re
import sys
from nltk.tokenize import RegexpTokenizer


folder = nltk.data.find("/home/lucille/Tal2017")
corpusReader = nltk.corpus.PlaintextCorpusReader(folder, 'corpus.txt')

#Tokenization en phrases :
nb_sentences = len(corpusReader.sents())
print("le fichier contient "+ str(nb_sentences) +" phrases")

#Tokenization en paragraphes :
#Remarque : il est étrange que ta tokenization en paragraphe donne le même nombre
#que ta tokenization en phrases
nb_paragraphs = len(corpusReader.paras())
print("le fichier contient "+ str(nb_sentences) +" paragraphs")

#Tokenization en mots :
nb_words=len([word for sentence in corpusReader.sents() for word in sentence])
print("Le fichier contient "+ str(nb_words) +" mots.")

#Tokenization en caractères :
nb_chars=len([char for sentence in corpusReader.sents() for word in sentence for char in word])
print("Le fichier contient "+ str(nb_chars) +" caractères.\n")
