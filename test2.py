# -*- coding: utf-8 -*-

import nltk
import os
import nltk.corpus  
from nltk.text import Text


# sélection du corpus (1ere méthode) [instancier sous la forme d'un objet texte] 
#coller le corpus dans /home/lucille/nltk_data/corpora/gutenberg
text = Text(nltk.corpus.gutenberg.words('corpus2.txt'))
#Affichage de l'objet :
print(text) 

text.concordance("murder")
