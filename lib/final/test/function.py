
import pandas
import math
import text

class detail:

    def __init__(self, score=None, content=None, sentence=None):

        self.score = score
        self.content = content
        self.sentence = sentence
        return
    
    pass

'''
根據給定的關鍵字（Subject-X）來計算文本的分數，
用來排序呈現檢索結果。
'''

vocabulary = text.vocabulary()
embedding = text.embedding()
pass

information = pandas.read_csv("./csv/information.csv")
vocabulary.load(what='frequency matrix', path='./frequency matrix.csv')
embedding.load(path='./vector.model')
pass

search = 'rash'
top = 5
pass

weight = vocabulary.get('ntf-idf')
rank = information.copy()
for k in [(search, 1)] + embedding.model.wv.similar_by_word(search,top):

    w,s = k
    weight[vocabulary.term.index(w),:] = weight[vocabulary.term.index(w),:] * (math.exp(5)*s)
    pass

rank['score'] = weight.sum(0)
rank = rank.sort_values(['score'], ascending=False).head(top).copy()

'''
對於每篇文章，去找出訊息量較多的句子，多少句子是參數。
'''

output = []
for index, item in rank.iterrows():
    
    d = detail(
        score=item["score"], 
        content=item['abstract'], 
        sentence={}
        )
    for s in vocabulary.tokenize(d.content, 'sentence'):
        
        r = [vocabulary.term.index(i) for i in vocabulary.tokenize(s, 'word')]
        d.sentence.update({s:weight[r,index].sum()})
        pass
    
    output.append({item['title_e']:d})
    pass    




# d.sentence
# len(score)
# information
# rank = pandas.DataFrame({"score":sorted(score), 'title':[vocabulary.title[i] for i in numpy.argsort(score)]})
# rank

# numpy.argsort([3,1,4,8,5])


# weight.sum(0)
# vocabulary = text.vocabulary()

# text.vocabulary()