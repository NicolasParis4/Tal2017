import nltk;
import re;
from nltk.corpus import wordnet as wn;

str = "1g";

print "1.",bool(re.search(r"([a-z+])", str));
print "2.",bool(re.search(r"ab*", str));
print "3.",bool(re.search(r"ab+", str));
print "4.",bool(re.search(r"ab?", str));
print "5.",bool(re.search(r"ab{3}", str));
print "6.",bool(re.search(r"ab{2,3}", str));
print "7.",bool(re.search(r"([a-z+])", str));
print "8.",bool(re.search(r"[a-z]+(_[a-z]+)+", str));
print "9.",bool(re.search(r"[A-Z][a-z][a-z]+", str));
print "10.",bool(re.search(r"a.*b$", str));
print "11.",bool(re.search(r"^w", str));
print "12.",bool(re.search(r"w[.,;:?!]?$", str));
print "13.",bool(re.search(r"[a-z]*z[a-z]*", str));


