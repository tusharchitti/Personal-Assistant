import nltk
import csv

#List of positive tweets
pos_tweets = [('I love this car', 'Happy'),
              ('This view is amazing', 'Happy'),
              ('I feel great this morning', 'Happy'),
              ('It is not that bad', 'Happy'),
              ('I am so excited about the concert', 'Happy'),
              ('He is my best friend', 'Happy')]
#List of negative tweets
neg_tweets = [('I do not like this car', 'Sad'),
              ('This view is horrible', 'Sad'),
              ('I feel tired this morning', 'Sad'),
              ('I am not looking forward to the concert', 'Sad'),
              ('He is my enemy', 'Sad')]


##with open('test.csv', 'rb') as f:
##    data = csv.reader(f)#Read csv file
##    #Make a list sent in which every classification text is in tuple form
##    sent=[]
##    for row in data:
##        sent.append(tuple(row))
##    #Classify text into positive or negative sentiment
##    for r in sent:
##        if r[1]=="Happy":
##            pos_tweets.append(r)
##        else:
##            neg_tweets.append(r)

#Words which have length less than 3 are omitted and all words are converted to lower case
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))
#o/p of tweet:[(['love', 'this', 'car'], 'Happy', (['this', 'view', 'amazing'], 'Happy'))

"""
test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]
"""

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words
#o/p:['love', 'this', 'car', 'this', 'view', 'amazing', 'feel',]

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    #print wordlist.most_common()
    #o/p:[('the', 15), ('not', 8), ('this', 8),]
    word_features = wordlist.keys()
    
    return word_features
#Now words are not repeated in word_features
#o/p:['all', 'help', 'gladioli', 'years', 'sleep', 'live', 'smiling', 'fine',]

word_features = get_word_features(get_words_in_tweets(tweets))
#o/p:['all', 'help', 'gladioli', 'years', 'sleep', 'live', 'smiling', 'fine',]


def extract_features(document):
    document_words = set(document)
##    o/p of document_words:
##    set(['this', 'car', 'love'])
##    set(['this', 'amazing', 'view'])
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
## {'contains(looking)': False, 'contains(not)': False, 'contains(excited)': False, 'contains(view)': False,
## 'contains(forward)': False, 'contains(that)': False, 'contains(love)': True,
    return features


training_set = nltk.classify.apply_features(extract_features, tweets)
##[({'contains(looking)': False, 'contains(not)': False, 'contains(excited)': False, 'contains(view)': False,
##'contains(forward)': False, 'contains(that)': False, 'contains(love)': True,

classifier = nltk.NaiveBayesClassifier.train(training_set)

def train(labeled_featuresets, estimator=nltk.probability.ELEProbDist):
    # Create the P(label) distribution
    label_probdist = estimator(label_freqdist)
    
    # Create the P(fval|label, fname) distribution
    feature_probdist = {}
    
    return NaiveBayesClassifier(label_probdist, feature_probdist)


tweet = 'Its not that bad after all'

print classifier.classify(extract_features(tweet.split()))

# o/p of tweet.split():['Its', 'not', 'that', 'bad', 'after', 'all']
