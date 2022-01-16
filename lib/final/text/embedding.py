
import gensim
import random
import pandas
from sklearn.manifold import MDS
from plotly import express
from gensim.models.callbacks import CallbackAny2Vec
from gensim.models import Word2Vec


class embedding:

    def __init__(self, content='sentence list', tokenize=None):

        self.content = content
        self.tokenize = tokenize
        pass

    def build(self, what='model', by='CBOW', window=5, dimension=50, epoch=5):

        random.seed(0)
        history = callback()
        self.sentence = [self.tokenize(content=c, to='word') for c in self.content]
        pass

        if(what):

            if(by=='CBOW'):

                self.model = gensim.models.Word2Vec(
                    min_count=1, window=window, sg=0, 
                    vector_size=dimension, epochs=epoch, 
                    seed=0, workers=1
                )
                self.model.build_vocab(self.sentence)
                self.model.train(
                    self.sentence, 
                    total_examples=self.model.corpus_count, 
                    epochs=self.model.epochs, 
                    callbacks=[history], compute_loss=True
                )
                pass
            
            if(by=='SG'):

                self.model = gensim.models.Word2Vec(
                    min_count=1, window=window, sg=1, 
                    vector_size=dimension, epochs=epoch, 
                    seed=0, workers=1
                )
                self.model.build_vocab(self.sentence)
                self.model.train(
                    self.sentence, 
                    total_examples=self.model.corpus_count, 
                    epochs=self.model.epochs, 
                    callbacks=[history], compute_loss=True                    
                )
                pass
            
            pass

        pass
    
    def save(self, path='./vector.model'):

        self.model.save(path)
        return
    
    def load(self, path="./vector.model"):
        
        self.model = Word2Vec.load(path)
        return

    pass

    # def collect(self, title, top=10):

    #     key  = []
    #     word = []
    #     for t in title:

    #         w, _, _ = self.tokenize(t)
    #         k = w[0]
    #         word += [i[0] for i in self.model.wv.similar_by_word(k, topn=top)]
    #         key  += [k]
    #         pass
        
    #     self.key     = key
    #     self.word    = list(set(word+key))
    #     self.vector  = self.model.wv[self.word]
    #     pass

    # def reduce(self, method="MDS", dimension=2):

    #     if(method=="MDS"):

    #         if(dimension==2):

    #             vector = MDS(n_components=dimension, random_state=0).fit_transform(self.vector)
    #             vector = pandas.DataFrame(vector, columns=['x', 'y'])
    #             vector['word'] = self.word
    #             vector['key']  = [str(1*(w in self.key)) for w in vector['word']]
    #             vector['type'] = vector['key'].replace({"0":"fish", "1":"bait"})
    #             self.reduction = vector
    #             pass

    #         if(dimension==3):

    #             vector = MDS(n_components=dimension, random_state=0).fit_transform(self.vector)
    #             vector = pandas.DataFrame(vector, columns=['x', 'y', 'z'])
    #             vector['word'] = self.word
    #             vector['key']  = [str(1*(w in self.key)) for w in vector['word']]
    #             vector['type'] = vector['key'].replace({"0":"fish", "1":"bait"})
    #             self.reduction = vector
    #             pass
            
    #         self.dimension = dimension
    #         pass

    #     return

    # def plot(self, skip='color'):

    #     if(self.dimension==2):

    #         if(skip=='color'):

    #             picture = express.scatter(self.reduction, x="x", y="y", text='word')
    #             picture.update_traces(textposition='top center', marker={'size':5}, textfont={'size':10})
    #             pass

    #         else:

    #             picture = express.scatter(self.reduction, x="x", y="y", text='word', color='type')
    #             picture.update_traces(textposition='top center', marker={'size':5}, textfont={'size':10})
    #             pass

    #         pass
        
    #     if(self.dimension==3):

    #         if(skip=='color'):

    #             picture = express.scatter_3d(self.reduction, x="x", y="y", z='z', text='word')
    #             picture.update_traces(textposition='top center', marker={'size':5}, textfont={'size':10})
    #             pass

    #         else:

    #             picture = express.scatter_3d(self.reduction, x="x", y="y", z='z', text='word', color='type')
    #             picture.update_traces(textposition='top center', marker={'size':5}, textfont={'size':10})
    #             pass

    #         pass
        
    #     return(picture)
        
    # pass



class callback(CallbackAny2Vec):

    def __init__(self):
        
        self.epoch = 0
        pass

    def on_epoch_end(self, model):

        loss = model.get_latest_training_loss()
        print('loss after epoch {}: {}'.format(self.epoch, loss))
        self.epoch += 1
        pass

    pass


# model = Word2Vec(common_texts, size=100, window=5, min_count=1, 
#                  compute_loss=True, callbacks=[callback()])

# import plotly.graph_objects as go

# fig = go.Figure()

# fig.add_trace(go.Scatter(
#     x=[0, 1, 2],
#     y=[1, 1, 1],
#     mode="lines+markers+text",
#     name="Lines, Markers and Text",
#     text=["Text A", "Text B", "Text C"],
#     textposition="top right",
#     textfont=dict(
#         family="sans serif",
#         size=18,
#         color="crimson"
#     )
# ))

# fig.add_trace(go.Scatter(
#     x=[0, 1, 2],
#     y=[2, 2, 2],
#     mode="lines+markers+text",
#     name="Lines and Text",
#     text=["Text G", "Text H", "Text I"],
#     textposition="bottom center",
#     textfont=dict(
#         family="sans serif",
#         size=18,
#         color="LightSeaGreen"
#     )
# ))
        
# # model = gensim.models.Word2Vec(min_count=5, window=5, sg=0, vector_size=50, epochs=20, seed=0)
# # model.build_vocab(tabulation.sentence)
# # model.train(tabulation.sentence, total_examples=model.corpus_count, epochs=model.epochs)