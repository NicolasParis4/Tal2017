# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

import nltk
import nltk.data
from nltk.text import Text
import re
import sys
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
import os
import pickle


#Importation du corpus (n'oubliez pas de modifier votre chemin) :
os.chdir("C:\\Users\\hishe\\OneDrive\\Documents\\GitHub\\Tal2017")
with open('Corpus_2.txt', 'r',encoding="utf8") as c:
    corpus = c.read()

corpus_1=''
for mot in corpus:
    corpus_1=corpus_1+mot        

#TOKENIZATION
#En mots :
tokenizer_W2 = TreebankWordTokenizer()
tokens_W=tokenizer_W2.tokenize(corpus_1)

print(nltk.ne_chunk(tokens_W))

#Tokenization en phrases
#tokenizer_P=nltk.data.load('tokenizers/punkt/PY3/english.pickle')
#tokens_P=tokenizer_P.tokenize(corpus_1)



