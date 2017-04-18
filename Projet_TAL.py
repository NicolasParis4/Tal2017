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

reload(sys)
sys.setdefaultencoding('utf8')

#NB : utiliser seulement corpus.txt, c'est le seul fichier encodé correctement

#Importation du fichier :
os.chdir("/Users/workplace/Documents/Tal2017")
with open('corpus.txt', 'r') as f:
    sample = f.read()

#Vérifications :
num=str(len(sample))
print("Le fichier contient "+num+" caractères.")

#Tokenization en mots : 
expr = re.compile("\W+",re.U)
liste = expr.split(sample)
print("Le fichier contient "+str(len(liste))+" mots.\n")

#Exécution d'une fonction de concordance : 
liste=Text(liste)
liste.concordance("murder")

