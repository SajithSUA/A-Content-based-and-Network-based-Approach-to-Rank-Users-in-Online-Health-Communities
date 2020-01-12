from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_jaccard_sim(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    print(a)
    print(b)
    print(c)
    return float(len(c)) / (len(a) + len(b) - len(c))

a=get_jaccard_sim("AI is our friend and it has been friend","AI and humans has always been friend")
print(a)

import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text1 = "AI is our friend and it has been friend"
text2 = " my friends and it has been friend AI is"

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
print (vector1)
print (vector2)
cosine = get_cosine(vector1, vector2)

print ('Cosine:', cosine)