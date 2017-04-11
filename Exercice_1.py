import nltk;
import re;
from nltk.corpus import wordnet as wn;

str = "523";

print bool(re.search(r"([a-z+])", str));

print bool(re.search(r"ab*", str));
print bool(re.search(r"ab+", str));
print bool(re.search(r"ab?", str));
print bool(re.search(r"ab{3}", str));
print bool(re.search(r"ab{2,3}", str));
print bool(re.search(r"([a-z+])", str));
print bool(re.search(r"[a-z]+(_[a-z]+)+", str));
print bool(re.search(r"[A-Z][a-z][a-z]+", str));
print bool(re.search(r"a.*b$", str));
print bool(re.search(r"^w", str));
print bool(re.search(r"w[.,;:?!]?$", str));
print bool(re.search(r"[a-z]*z[a-z]*", str));


