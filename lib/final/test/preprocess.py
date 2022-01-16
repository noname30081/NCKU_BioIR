
import pandas

'''
根據文本資料，建構 term document matrix 矩陣，
存放在指定的位置。
'''

information = pandas.read_csv("csv/information.csv")

import text

vocabulary = text.vocabulary()
vocabulary.build(content = information['abstract'], title=information['title_e'])

matrix = pandas.DataFrame(vocabulary.frequency, dtype='int')
matrix.index = vocabulary.term
matrix.columns = vocabulary.title
matrix.to_csv('frequency matrix.csv')

'''
建構 word2vec 模型，詞向量存放在指定位置。
'''

embedding = text.embedding(content=information['abstract'], tokenize=vocabulary.tokenize)
embedding.build(what='model', by='SG', window=8, dimension=150, epoch=10)
embedding.save(path='./vector.model')

