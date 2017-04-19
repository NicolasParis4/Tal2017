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

#NB : utiliser seulement corpus.txt, c'est le seul fichier encodé correctement

#Importation du fichier (bonne pratique désolée) :
os.chdir("/home/lucille/Tal2017")
with open('corpus.txt', 'r') as f:
    sample = f.read()

#TOKENIZATION
#Docs : ntlk.org ; module tokenize regexp ; nltk data 

#Tokenization en phrases
tokenizer_P=nltk.data.load('tokenizers/punkt/PY3/english.pickle')
tokens_P=tokenizer_P.tokenize(sample)
print("Le fichier contient "+str(len(tokens_P))+" phrases")

#Tokenization en mots à l'aide d'une expression régulière
#Attention cette manière de procéder, considère la ponctuation et caractères
# non alphabétiques comme des mots
tokenizer_W = RegexpTokenizer('\w+|[^\w\s]+')
tokens_W=tokenizer_W.tokenize(sample)
# Affichage du résultat : print(len(tokens_W))
#NE PAS UTILISER, ne pas supprimer, on le garde pour l'exemple (cf. rapport). 

#Tokenisation en mots à l'aide de TreeBankTokenizer
#ce tokenizer utilise aussi des expressions régulières
tokenizer_W2 = TreebankWordTokenizer()
tokens_W2=tokenizer_W2.tokenize(sample)
print("Le fichier contient "+str(len(tokens_W2))+" mots")



