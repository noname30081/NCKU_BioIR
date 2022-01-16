
import nltk 
import re
import string
import tqdm
import pandas
import functools
import numpy
from collections import Counter

constant = {
    'porter stemming':True,
    'remove stopword':True
}

class vocabulary:

    def __init__(self):
        
        self.tokenize = tokenize
        return

    def load(self, what='frequency matrix', path='./frequency matrix.csv'):

        if(what=='frequency matrix'):

            table = pandas.read_csv(path, index_col=0)
            self.title = list(table.columns)
            self.term  = list(table.index)
            self.frequency = numpy.array(table)
            pass

        return

    def build(self, content=None, title=None):

        self.content = content 
        self.title = title
        pass

        total  = len(self.content)
        matrix = []
        word  = []
        for c, t in tqdm.tqdm(zip(self.content, self.title), total=total, leave=False):

            w = self.tokenize(content=c, to='word')
            m = pandas.DataFrame.from_dict(Counter(w), orient='index')
            m = m.reset_index().rename(columns={'index':'term', 0:t})
            word   += [w]
            matrix += [m]
            pass
        
        matrix = functools.reduce(
            lambda x, y: pandas.merge(x, y, how='outer'), 
            tqdm.tqdm(matrix, leave=False)
        ).fillna(0)
        frequency = matrix.iloc[:,1:].to_numpy()
        pass

        self.term   = matrix.term.tolist()
        self.title  = matrix.columns.tolist()[1:]
        self.frequency = frequency
        # if(constant["normalize frequency by document"]): frequency = (frequency / frequency.sum(axis=0))
        return

    def get(self, what='tf-idf or ntf-idf'):

        if(what=='tf-idf'):

            frequency = self.frequency.copy()
            matrix = numpy.dot(
                frequency.transpose(), 
                numpy.diag(numpy.log(frequency.shape[1] / (frequency > 0).sum(axis=1)))
            )
            matrix = matrix.transpose()
            return(matrix)
        
        if(what=='ntf-idf'):

            frequency = self.frequency.copy()
            frequency = (frequency / frequency.sum(axis=0))
            matrix = numpy.dot(
                frequency.transpose(), 
                numpy.diag(numpy.log(frequency.shape[1] / (frequency > 0).sum(axis=1)))
            )
            matrix = matrix.transpose()
            return(matrix)

        return

    pass


def tokenize(content="the content of text", to='word or sentence'):
    #nltk.download()
    if(to=='word'):

        pattern  = "[" + re.sub("[-]", "", string.punctuation) + ']'
        word = re.sub(pattern, "", content).split()
        pass

        ##  Stemming with porter method.
        if(constant["porter stemming"]):

            porter = nltk.stem.PorterStemmer()
            word = [porter.stem(w) for w in word]
            pass

        ##  Remove stopword.
        if(constant["remove stopword"]):

            collection = []
            for w in word:

                if(w not in stopword):

                    collection += [w]
                    pass

                pass
            
            word = collection
            pass
        
        return(word)
    
    if(to=='sentence'):

        sentence = nltk.sent_tokenize(content, language='english')
        return(sentence)

    return


stopword = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself",
    "she", "her", "hers", "herself", "it", "its", "itself", "they", 
    "them", "their", "theirs", "themselves", "what",
    "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", 
    "being", "have", "has", "had", "having", "do", "does", "did", "doing", 
    "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", 
    "into", "through", "during", "before", "after", "above", "below", "to", 
    "from", "up", "down", "in", "out", "on", "off", "over", "under", 
    "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
    "any","both","each","few","more","most","other","some","such",
    "no","nor","not","only","own","same","so","than", "too", 
    "very", "s", "t", "can", "will", "just", "don", "should", "now"
}

# '''
# class tokenize:

#     def __init__(self):

#         self.word = __word__.tokenize
#         self.sentence = __sentence__.tokenize
#         return

#     pass

# class __word__:

#     def tokenize(x):

#         pattern  = "[" + re.sub("[-]", "", string.punctuation) + ']'
#         word = re.sub(pattern, "", x).split()
#         pass

#         ##  Stemming with porter method.
#         stemming = True
#         if(stemming):

#             porter = nltk.stem.PorterStemmer()
#             word = [porter.stem(w) for w in word]
#             pass

#         ##  Remove stopword.
#         if(True):

#             collection = []
#             for w in word:

#                 if(w not in stopword):

#                     collection += [w]
#                     pass

#                 pass
            
#             word = collection
#             pass

#         y = word
#         return(y)

#     pass

# class __sentence__:

#     def tokenize(x):

#         y = nltk.sent_tokenize(x, language='english')
#         return(y)
    
#     pass
# '''




# class vocabulary:

#     def __init__(self, content=[['hello', 'world'], ['good', 'morning']], title=['book A', 'Book B']):
        
#         self.content = content
#         self.title = title
#         self.tokenize = tokenize()
#         return

#     def build(self):

#         '''Build term document matrix.'''
#         total  = len(self.content)
#         matrix = []
#         word  = []
#         for c, t in tqdm.tqdm(zip(self.content, self.title), total=total, leave=False):

#             # w = self.tokenize(x=c)
#             w = self.tokenize.word(x=c)
#             m = pandas.DataFrame.from_dict(Counter(w), orient='index')
#             m = m.reset_index().rename(columns={'index':'term', 0:t})
#             word   += [w]
#             matrix += [m]
#             pass
        
#         matrix = functools.reduce(lambda x, y: pandas.merge(x, y, how='outer'), tqdm.tqdm(matrix, leave=False)).fillna(0)
#         self.term      = matrix.term.tolist()
#         self.document  = matrix.columns.tolist()[1:]
#         frequency = matrix.iloc[:,1:].to_numpy()
#         if(True): frequency = (frequency / frequency.sum(axis=0))
#         self.frequency = frequency
#         return

#     def transform(self, mode='tf-idf'):

#         if(mode=='tf-idf'):

#             matrix = numpy.dot(
#                 self.frequency.transpose(), 
#                 numpy.diag(numpy.log(self.frequency.shape[1] / (self.frequency > 0).sum(axis=1)))
#             )
#             matrix = matrix.transpose()
#             self.matrix = matrix.round(2)
#             pass
        
#         print('use [self.matrix] to call the weight matrix')
#         return

#     pass