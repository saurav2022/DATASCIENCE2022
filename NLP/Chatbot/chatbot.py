import io
import random
import string 
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True)

with open('chatbot.txt', 'r', encoding='utf-8', errors='ignore') as fp:
	raw = fp.read().lower()



#Tokenisation
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)



# Preprocessing
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for  punct in string.punctuation) 

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



#Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "Hi there", "hello", "I am glad, you are talking to me!"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    # print(f"Length = {len(sent_tokens)}   ")
    vals = cosine_similarity(tfidf[-1], tfidf)
    # print(f"{len(vals)}  vals: {vals.argsort()[0]}")
    idx = vals.argsort()[0][-2]
    # print(f"idx : {idx}")
    flat = vals.flatten()
    # print(f"flat : {flat}")
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response = robo_response + " I am sorry! I had a tough time interpreting you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


# Controller
flag = True
print("ROBO: My name is Robo. I will answer your queries. Type Bye to exit :)")
while (flag == True):
    user_response = input("What's in your mind? ")
    user_response = user_response.lower()
    if (user_response != 'bye'):
        if(user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("ROBO : You are welcome")
        else:
            if(greeting(user_response) != None):
                print("ROBO: " + greeting(user_response))
            else:
                print("ROBO : ", end = "")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("ROBO: Bye! Take care")
