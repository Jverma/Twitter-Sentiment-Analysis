import json
import sys
import re


## Open AFINN File and Create a Dictionary of Terms and Sentiment Scores 
afinn_file = open(sys.argv[1])
scores = {}                             # initialize an empty dictionary
for line in afinn_file:
    term, score  = line.split("\t")     # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)           # Convert the score to an integer



## Define Sentiment of a Text - Line
def sentiment(line):
    score = 0
    words = re.findall(r"\b[a-z]+\b", line, re.I)
    for w in words:
        if (w in scores):
            score = score + scores[w]       
        return score


## Compute Sentiment of Tweets
input = open(sys.argv[2])                   #Open Tweet File
for line in input:
    data = json.loads(line)
    if ('text' in data) and ('lang' in data):
        language = data['lang']
        tweet = data['text']
        if (language == 'en'):               # Only English Tweets
            sentiment_score = sentiment(tweet)
            print sentiment_score
    
