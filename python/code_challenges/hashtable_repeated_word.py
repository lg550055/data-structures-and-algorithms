from data_structures.hashtable import Hashtable
import re

def first_repeated_word(text):
    nopunc = re.sub(r'[,.?!;:-]', '', text).lower()
    stext = nopunc.split()
    h = {}
    for w in stext:
        if w in h:
            return w
        h[w] = 1
