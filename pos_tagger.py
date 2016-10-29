import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text=state_union.raw("2002-GWBush.txt")

sample_text='saurabh is going to Delhi'



#Train the data
custom_sent_tokenizer=PunktSentenceTokenizer(train_text)

short_pos = open("test.txt","r").read()

for r in short_pos.split('\n'):
    #Test the data
    tokenized=custom_sent_tokenizer.tokenize(r.split(',')[0])

    for i in tokenized:

            #Dividng the text into words
            words=nltk.word_tokenize(i)
            #Tagging the words with its appropriate part of speech
            tagged=nltk.pos_tag(words)
            print(tagged)

            namedEnt=nltk.ne_chunk(tagged,binary=True)
            print(namedEnt)

##def process_content():
##    try:
##        
##
##    except Exception as e:
##        print(str(e))
##
##process_content()
