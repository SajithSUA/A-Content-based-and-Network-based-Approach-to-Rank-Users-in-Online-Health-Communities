from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

def get_jaccard_sim(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    print(a)
    print(b)
    print(c)
    return float(len(c)) / (len(a) + len(b) - len(c))



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

text1 = "Hi I've been NED for 14 years and have been a therapist for 17 years so I have a lot of varied experience dealing with anxiety. Anxiety is just awful and can not only be debilitating but can keep us from being able to take in and process information just when we need to be at our best. Too little stress can leave us bored but too much stress/anxiety can leave us with panic unusual amounts of anger and/or the inability to perform at our best. In the not diagnosed but worried category anxiety can mean that we aren't able to hear our medical providers when they give us good news or we aren't able to rationally discern what information is good and credible scientific evidence and what information is unscientific and only inflames our anxiety. It may impair our ability to listen remember read and comprehend our personal risks our treatment options and our ability to calm ourselves even if we have been found to have no evidence of disease. So how do you know if you are too anxious? Look at the stress curve above. Do you feel fatigued or exhausted? Are you sleeping well? Can you turn your mind to something else when you need to focus on another task? Or is your anxiety all you can think about. Are you eating properly? Or have you lost your appetite. Are you able to engage in activities that reduce your feeling of anxiety/stress? If you are able to concentrate on something else for periods of time and utilize good coping skills to reduce your feelings of stress then you'd fall in the optimal performance stage. If your normal patterns of sleep energy and appetite have been disrupted then you would fall in the distress stage. I am going to suggest some strategies for each category and am hoping that others will chime in with what works for them. What I'd like to see is a thread where anyone who is new to the experience of breast cancer or other breast health issues has a place to refer to for concrete suggestions for managing their anxiety. There is no judgment here as we've all experienced anxiety (to some extent) in our own journeys. Stress occurs when perceived pressure on a person is greater than their ability to sustain resilience. The following skills can be used to improve and maintain your resilience: Practice distraction: deep clean something; do a home project that you've been wanting to do but haven't gotten around to; binge watch netflix; if you like to cook or bake make a complicated recipe that takes your full concentration. Exercise: studies have shown that at little as 20 minutes of walking can bring down your stress response and walking in nature has a more robust response Regular relaxation: listen to a relaxation cd or use an app try guided imagery practice counting your breathe practice yoga try mindfulness or meditation take a hot shower or bath get a massage Use good self-care: make sure you are getting good nutrition and good sleep For those of you who find that the above strategies aren't enough to reduce you anxiety to a tolerable level or for those of you who have pre-existing anxiety issues. Talk to your primary care provider (or psychiatrist if you have one) about medication options both long term and short term; for both anxiety and sleep Think about getting into therapy and learn cognitive behavioral techniques to address your anxiety Find a group that lets you connect to others who have experienced similar levels of anxiety and who may be able to share ideas about what has been effective for them. For those who are here who have been diagnosed there was a study recently released that found a statistically significant improvement in the recurrence anxiety of breast cancer survivors. See a summary here: https://community.breastcancer.org/forum/105/topics/855472?page=1#idx_1 I may review and revise this post at will without defining why unless saying why is integral to the work. I would like to be able to add links and additional information as I find it."
text2 = "In customer services, AI system should be able to understand semantically similar queries from users and provide a uniform response. The emphasis on semantic similarity aims to create a system that recognizes language and word patterns to craft responses that are similar to how a human conversation works. For example, if the user asks"
text3 = "Hi I've  NED for 14 years and have been a  for 17  so I have a lot of  dealing with anxiety. Anxiety is just  and can not only   but can  us from being able to take in and process information just when we need to be at our best. Too little stress can leave us bored but too much stress/anxiety can leave us with panic unusual amounts of anger and/or the inability to perform at our best. In the not diagnosed but worried category anxiety can mean that we aren't able to hear our medical providers when they give us good news or we aren't able to rationally discern what information is good and credible scientific evidence and what information is unscientific and only inflames our anxiety. It may impair our ability to listen remember read and comprehend our personal risks our treatment options and our ability to calm ourselves even if we have been found to have no evidence of disease. So how do you know if you are too anxious? Look at the stress curve above. Do you feel fatigued or exhausted? Are you sleeping well? Can you turn your mind to something else when you need to focus on another task? Or is your anxiety all you can think about. Are you eating properly? Or have you lost your appetite. Are you able to engage in activities that reduce your feeling of anxiety/stress? If you are able to concentrate on something else for periods of time and utilize good coping skills to reduce your feelings of stress then you'd fall in the optimal performance stage. If your normal patterns of sleep energy and appetite have been disrupted then you would fall in the distress stage. I am going to suggest some strategies for each category and am hoping that others will chime in with what works for them. What I'd like to see is a thread where anyone who is new to the experience of breast cancer or other breast health issues has a place to refer to for concrete suggestions for managing their anxiety. There is no judgment here as we've all experienced anxiety (to some extent) in our own journeys. Stress occurs when perceived pressure on a person is greater than their ability to sustain resilience. The following skills can be used to improve and maintain your resilience: Practice distraction: deep clean something; do a home project that you've been wanting to do but haven't gotten around to; binge watch netflix; if you like to cook or bake make a complicated recipe that takes your full concentration. Exercise: studies have shown that at little as 20 minutes of walking can bring down your stress response and walking in nature has a more robust response Regular relaxation: listen to a relaxation cd or use an app try guided imagery practice counting your breathe practice yoga try mindfulness or meditation take a hot shower or bath get a massage Use good self-care: make sure you are getting good nutrition and good sleep For those of you who find that the above strategies aren't enough to reduce you anxiety to a tolerable level or for those of you who have pre-existing anxiety issues. Talk to your primary care provider (or psychiatrist if you have one) about medication options both long term and short term; for both anxiety and sleep Think about getting into therapy and learn cognitive behavioral techniques to address your anxiety Find a group that lets you connect to others who have experienced similar levels of anxiety and who may be able to share ideas about what has been effective for them. For those who are here who have been diagnosed there was a study recently released that found a statistically significant improvement in the recurrence anxiety of breast cancer survivors. See a summary here: https://community.breastcancer.org/forum/105/topics/855472?page=1#idx_1 I may review and revise this post at will without defining why unless saying why is integral to the work. I would like to be able to add links and additional information as I find it."

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text3)
print (vector1)
print (vector2)
cosine = get_cosine(vector1, vector2)

print ('Cosine:', cosine)







lemmatizer = WordNetLemmatizer()
s=lemmatizer.lemmatize(text1)
q=lemmatizer.lemmatize(text2)


a=get_jaccard_sim(s,q)
print(a)

b=get_jaccard_sim(text1,text2)
print(b)