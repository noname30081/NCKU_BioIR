import tensorflow as tf
import keras
import keras.backend as K
from keras.models import Model,Sequential
from keras.layers import Dense, Embedding, Lambda,Reshape,dot,Input
from keras.layers.merge import concatenate
from keras.preprocessing import text
from keras.utils import np_utils
from keras.preprocessing import sequence
from keras.preprocessing.sequence import skipgrams
from IPython.display import SVG
from sklearn.metrics.pairwise import euclidean_distances
from keras.utils.vis_utils import model_to_dot
import os

from tensorboard.plugins import projector

import pandas as pd
import numpy as np

from stop_words import get_stop_words
from keywordBase import KeyWordBase

class Word2Vec():
    def VectToken(self,paragraphics):
        tokenizer = text.Tokenizer()
        tx=[]
        stoplist = get_stop_words('en')
        for para in paragraphics :
            pa = para['Tags']['abstract']['ORIG']
            for stopword in stoplist :
                pa = pa.replace(' {} '.format(stopword),' ')
            tx.append(pa)
        tokenizer.fit_on_texts(tx)
        word2id = tokenizer.word_index  

        word2id['PAD'] = 0
        id2word = {v:k for k, v in word2id.items()}
        wids = [[word2id[w] for w in text.text_to_word_sequence(doc)] for doc in tx]

        vocab_size = len(word2id)
        embed_size = 100
        window_size = 2 # context window size

        print('Vocabulary Size:', vocab_size)
        print('Vocabulary Sample:', list(id2word.items())[:10]) 

        # build CBOW architecture
        self.cbow = Sequential()
        self.cbow.add(Embedding(vocab_size, embed_size, input_length=window_size*2))
        self.cbow.add(Lambda(lambda x: K.mean(x, axis=1), output_shape=(embed_size,)))
        self.cbow.add(Dense(vocab_size, activation='softmax'))
        self.cbow.compile(loss='categorical_crossentropy', optimizer='rmsprop')

        for epoch in range(1, 10):
            loss = 0.
            i = 0
            for x, y in self.generate_context_word_pairs(corpus=wids, window_size=window_size, vocab_size=vocab_size):
                i += 1
                loss += self.cbow.train_on_batch(x, y)
                if i % 1000 == 0:
                    print('Processed {} (context, word) pairs'.format(i))
                #print('i:',i,'\tLoss:', loss)

            print('Epoch:', epoch, '\tLoss:', loss)
            print()    
        self.cbow.save('../HW3/Covid_cbow.h5')  
    def generate_context_word_pairs(corpus, window_size, vocab_size):
        context_length = window_size*2
        for words in corpus:
            sentence_length = len(words)
            for index, word in enumerate(words):
                context_words = []
                label_word   = []            
                start = index - window_size
                end = index + window_size + 1
                
                context_words.append([words[i] 
                                    for i in range(start, end) 
                                    if 0 <= i < sentence_length 
                                    and i != index])
                label_word.append(word)

                x = sequence.pad_sequences(context_words, maxlen=context_length)
                y = np_utils.to_categorical(label_word, vocab_size)
                yield (x, y)  
    def LoadModel(self,paragraphics):
        tokenizer = text.Tokenizer()
        tx=[]
        stoplist = get_stop_words('en')
        for para in paragraphics :
            pa = para['Tags']['abstract']['ORIG']
            for stopword in stoplist :
                pa = pa.replace(' {} '.format(stopword),' ')
            tx.append(pa)
        tokenizer.fit_on_texts(tx)
        word2id = tokenizer.word_index  

        word2id['PAD'] = 0
        id2word = {v:k for k, v in word2id.items()}
        wids = [[word2id[w] for w in text.text_to_word_sequence(doc)] for doc in tx]

        model = keras.models.load_model('../HW3/Covid_cbow.h5')

        weights = model.get_weights()[0]
        weights = weights[1:]
        print(weights.shape)

        # Set up a logs directory, so Tensorboard knows where to look for files.
        log_dir='./logs/imdb-example/'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Save Labels separately on a line-by-line manner.
        with open(os.path.join(log_dir, 'metadata.tsv'), "w",encoding="utf-8") as f:
            for subwords in word2id.keys():
                f.write("{}\n".format(subwords))

        weights_ = tf.Variable(model.layers[0].get_weights()[0][0:])
        # Create a checkpoint from embedding, the filename and key are the
        # name of the tensor.
        checkpoint = tf.train.Checkpoint(embedding=weights_)
        checkpoint.save(os.path.join(log_dir, "embedding.ckpt"))

        # Set up config.
        config = projector.ProjectorConfig()
        embedding = config.embeddings.add()
        # The name of the tensor will be suffixed by `/.ATTRIBUTES/VARIABLE_VALUE`.
        embedding.tensor_name = "embedding/.ATTRIBUTES/VARIABLE_VALUE"
        embedding.metadata_path = 'metadata.tsv'
        projector.visualize_embeddings(log_dir, config)

        print(pd.DataFrame(weights, index=list(id2word.values())[1:]).head(40))
        print(weights.shape)

        # compute pairwise distance matrix
        distance_matrix = euclidean_distances(weights)
        print(distance_matrix.shape)

        # view contextually similar words
        similar_words = {search_term: [id2word[idx] for idx in distance_matrix[word2id[search_term]-1].argsort()[0:10]+1] 
                        for search_term in ['species', 'cov','covid19','sars','testing','disease']}

        print(similar_words)      
    def VectToken2(self,paragraphics,keyword):  
        tokenizer = text.Tokenizer()
        tx=paragraphics.split('\n')
        stoplist = get_stop_words('en')
        tokenizer.fit_on_texts(tx)
        word2id = tokenizer.word_index  

        word2id['PAD'] = 0
        id2word = {v:k for k, v in word2id.items()}
        wids = [[word2id[w] for w in text.text_to_word_sequence(doc)] for doc in tx]

        vocab_size = len(word2id)
        embed_size = 10
        window_size = 2 # context window size

        print('Vocabulary Size:', vocab_size)
        print('Vocabulary Sample:', list(id2word.items())[:10]) 

        # build CBOW architecture
        cbow = Sequential()
        cbow.add(Embedding(vocab_size, embed_size, input_length=window_size*2))
        cbow.add(Lambda(lambda x: K.mean(x, axis=1), output_shape=(embed_size,)))
        cbow.add(Dense(vocab_size, activation='softmax'))
        cbow.compile(loss='categorical_crossentropy', optimizer='rmsprop')

        for epoch in range(1, 10):
            loss = 0.
            i = 0
            for x, y in self.generate_context_word_pairs(corpus=wids, window_size=window_size, vocab_size=vocab_size):
                i += 1
                loss += cbow.train_on_batch(x, y)
                if i % 1000 == 0:
                    print('Processed {} (context, word) pairs'.format(i))
                #print('i:',i,'\tLoss:', loss)

            print('Epoch:', epoch, '\tLoss:', loss)
            print()    
        cbow.save('../HW3/{}_cbow.h5'.format(keyword))  
    def LoadModel2(self,paragraphics,keyword):
        tokenizer = text.Tokenizer()
        tx=paragraphics.split('\n')
        stoplist = get_stop_words('en')
        tokenizer.fit_on_texts(tx)
        word2id = tokenizer.word_index  

        word2id['PAD'] = 0
        id2word = {v:k for k, v in word2id.items()}
        wids = [[word2id[w] for w in text.text_to_word_sequence(doc)] for doc in tx]

        model = keras.models.load_model('../HW3/{}_cbow.h5'.format(keyword))

        weights = model.get_weights()[0]
        weights = weights[1:]
        print(weights.shape)

        # Set up a logs directory, so Tensorboard knows where to look for files.
        log_dir='./logs/imdb-example/'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Save Labels separately on a line-by-line manner.
        with open(os.path.join(log_dir, 'metadata.tsv'), "w",encoding="utf-8") as f:
            for subwords in word2id.keys():
                f.write("{}\n".format(subwords))

        weights_ = tf.Variable(model.layers[0].get_weights()[0][0:])
        # Create a checkpoint from embedding, the filename and key are the
        # name of the tensor.
        checkpoint = tf.train.Checkpoint(embedding=weights_)
        checkpoint.save(os.path.join(log_dir, "embedding.ckpt"))

        # Set up config.
        config = projector.ProjectorConfig()
        embedding = config.embeddings.add()
        # The name of the tensor will be suffixed by `/.ATTRIBUTES/VARIABLE_VALUE`.
        embedding.tensor_name = "embedding/.ATTRIBUTES/VARIABLE_VALUE"
        embedding.metadata_path = 'metadata.tsv'
        projector.visualize_embeddings(log_dir, config)

        print(pd.DataFrame(weights, index=list(id2word.values())[1:]).head(40))
        print(weights.shape)

        # compute pairwise distance matrix
        distance_matrix = euclidean_distances(weights)
        print(distance_matrix.shape)

        # view contextually similar words
        similar_words = {search_term: [id2word[idx] for idx in distance_matrix[word2id[search_term]-1].argsort()[0:10]+1] 
                        for search_term in ['species', 'cov','covid19','sars','testing','disease']}

        print(similar_words)         

    def SkipGram_Training(self,paragraphics,keyword):  
        tokenizer = text.Tokenizer()
        tx=paragraphics.split('\n')
        stoplist = get_stop_words('en')
        tokenizer.fit_on_texts(tx)
        word2id = tokenizer.word_index
        id2word = {v:k for k, v in word2id.items()}

        vocab_size = len(word2id) + 1 
        embed_size = 100

        wids = [[word2id[w] for w in text.text_to_word_sequence(doc)] for doc in tx]

        # generate skip-grams
        skip_grams = [skipgrams(wid, vocabulary_size=vocab_size, window_size=10) for wid in wids]

        # view sample skip-grams
        pairs, labels = skip_grams[0][0], skip_grams[0][1]
        for i in range(10):
            print("({:s} ({:d}), {:s} ({:d})) -> {:d}".format(
                id2word[pairs[i][0]], pairs[i][0], 
                id2word[pairs[i][1]], pairs[i][1], 
                labels[i])) 

        # build skip-gram architecture
        word_model = Sequential()
        word_model.add(Embedding(vocab_size, embed_size,
                                embeddings_initializer="glorot_uniform",
                                input_length=1))
        word_model.add(Reshape((embed_size, )))

        context_model = Sequential()
        context_model.add(Embedding(vocab_size, embed_size,
                        embeddings_initializer="glorot_uniform",
                        input_length=1))
        context_model.add(Reshape((embed_size,)))

        concatenated = concatenate(inputs=[word_model.outputs, context_model.outputs])
        out = Dense(1, activation='softmax', name='output_layer')(concatenated)

        model = Model([word_model.inputs, context_model.inputs], out)

        #model = Sequential()
        #model.add(Dot((1))([word_model, context_model]))
        model.add(Dense(1, kernel_initializer="glorot_uniform", activation="sigmoid"))
        model.compile(loss="mean_squared_error", optimizer="rmsprop")

        # view model summary
        print(model.summary())


        SVG(model_to_dot(model, show_shapes=True, show_layer_names=False, 
                        rankdir='TB').create(prog='dot', format='svg'))
        
        for epoch in range(1, 10):
            loss = 0
            for i, elem in enumerate(skip_grams):
                pair_first_elem = np.array(list(zip(*elem[0]))[0], dtype='int32')
                pair_second_elem = np.array(list(zip(*elem[0]))[1], dtype='int32')
                labels = np.array(elem[1], dtype='int32')
                X = [pair_first_elem, pair_second_elem]
                Y = labels
                if i % 1000 == 0:
                    print('Processed {} (skip_first, skip_second, relevance) pairs'.format(i))
                loss += model.train_on_batch(X,Y)  

            print('Epoch:', epoch, 'Loss:', loss)
        model.save('../HW3/{}_sg.h5'.format(keyword))  

    def SkipGram_Training_2(self,paragraphics,keyword):  
        tokenizer = text.Tokenizer()
        stoplist = get_stop_words('en')
        for sp in stoplist :
            paragraphics = paragraphics.lower().replace(' {} '.format(sp.lower()),'')
            paragraphics = paragraphics.lower().replace(' {}.'.format(sp.lower()),'')
            paragraphics = paragraphics.lower().replace('.{} '.format(sp.lower()),'')
        tx=paragraphics.split('\n')     
        tokenizer.fit_on_texts(tx)
        word2id = tokenizer.word_index
        id2word = {v:k for k, v in word2id.items()}

        vocab_size = len(word2id) + 1 
        embed_size = 100

        wids = [[word2id[w] for w in text.text_to_word_sequence(doc)] for doc in tx]

        # generate skip-grams
        skip_grams = [skipgrams(wid, vocabulary_size=vocab_size, window_size=20) for wid in wids]

        # view sample skip-grams
        pairs, labels = skip_grams[0][0], skip_grams[0][1]
        #for i in range(10):
        #    print("({:s} ({:d}), {:s} ({:d})) -> {:d}".format(
        #        id2word[pairs[i][0]], pairs[i][0], 
        #        id2word[pairs[i][1]], pairs[i][1], 
        #        labels[i])) 

        input_target = Input((1,))
        input_context = Input((1,))

        embedding = Embedding(vocab_size, embed_size, input_length=1, name='embedding')

        word_model = embedding(input_target)
        word_model = Reshape((embed_size, 1))(word_model)

        context_model = embedding(input_context)
        context_model = Reshape((embed_size, 1))(context_model)

        # now perform the dot product operation  
        dot_product = dot([word_model, context_model], axes=1)
        dot_product = Reshape((1,))(dot_product)
        
        # add the sigmoid output layer
        output = Dense(1, activation='sigmoid')(dot_product)

        model = Model(inputs=[input_target, input_context], outputs=output)
        model.compile(loss='mean_squared_error', optimizer='rmsprop')

        # view model summary
        print(model.summary())


        SVG(model_to_dot(model, show_shapes=True, show_layer_names=False, 
                        rankdir='TB').create(prog='dot', format='svg'))
        
        for epoch in range(1, 150):
            loss = 0
            for i, elem in enumerate(skip_grams):
                try:
                    pair_first_elem = np.array(list(zip(*elem[0]))[0], dtype='int32')
                    pair_second_elem = np.array(list(zip(*elem[0]))[1], dtype='int32')
                    labels = np.array(elem[1], dtype='int32')
                    X = [pair_first_elem, pair_second_elem]
                    Y = labels
                    if i % 1000 == 0:
                        print('Processed {} (skip_first, skip_second, relevance) pairs'.format(i))
                    loss += model.train_on_batch(X,Y)  
                except Exception as ex :
                    print('Exception at {}[{}]'.format(i,elem))

            print('Epoch:', epoch, 'Loss:', loss)
        model.save('../HW3/{}_sg.h5'.format(keyword))  

    def LoadModel3(self,paragraphics,keyword):
        tokenizer = text.Tokenizer()
        stoplist = get_stop_words('en')
        for sp in stoplist :
            paragraphics = paragraphics.replace(' {} '.format(sp),'')
            paragraphics = paragraphics.replace(' {}.'.format(sp),'')
        tx=paragraphics.split('\n')
        tokenizer.fit_on_texts(tx)
        word2id = tokenizer.word_index  

        word2id['PAD'] = 0
        id2word = {v:k for k, v in word2id.items()}
        wids = [[word2id[w] for w in text.text_to_word_sequence(doc)] for doc in tx]

        model = keras.models.load_model('../HW3/{}_sg.h5'.format(keyword))

        weights = model.get_weights()[0]
        weights = weights[1:]
        print(weights.shape)

        # Set up a logs directory, so Tensorboard knows where to look for files.
        log_dir='./logs/imdb-example/'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Save Labels separately on a line-by-line manner.
        with open(os.path.join(log_dir, 'metadata.tsv'), "w",encoding="utf-8") as f:
            for subwords in word2id.keys():
                f.write("{}\n".format(subwords))

        weights_ = tf.Variable(model.layers[2].get_weights()[0][0:])
        # Create a checkpoint from embedding, the filename and key are the
        # name of the tensor.
        checkpoint = tf.train.Checkpoint(embedding=weights_)
        checkpoint.save(os.path.join(log_dir, "embedding.ckpt"))

        # Set up config.
        config = projector.ProjectorConfig()
        embedding = config.embeddings.add()
        # The name of the tensor will be suffixed by `/.ATTRIBUTES/VARIABLE_VALUE`.
        embedding.tensor_name = "embedding/.ATTRIBUTES/VARIABLE_VALUE"
        embedding.metadata_path = 'metadata.tsv'
        projector.visualize_embeddings(log_dir, config)

        print(pd.DataFrame(weights, index=list(id2word.values())[1:]).head(40))
        print(weights.shape)

        # compute pairwise distance matrix
        distance_matrix = euclidean_distances(weights)
        print(distance_matrix.shape)

        # view contextually similar words
        similar_words = {search_term: [id2word[idx] for idx in distance_matrix[word2id[search_term]-1].argsort()[0:10]+1] 
                        for search_term in ['atopic', 'dermatitis','skin','disease']}

        print(similar_words) 
    def PudmedStructive(self,paragraphics):
        paragraphics = paragraphics.replace('BACKGROUND: ','')
        paragraphics = paragraphics.replace('INTRODUCTION: ','')
        paragraphics = paragraphics.replace('?\n','')
        tx=paragraphics.split('\n')
        parawordslist = []
        i = 0
        for tt in tx :
            parawords = {'index':i,'sentences':KeyWordBase.SplitSentences(tt)}
            parawordslist.append(parawords)
            i=i+1
        return parawordslist
    def createLabel(self,paragraphics,word,keyword):
        isKey = True
        model = keras.models.load_model('../HW3/{}_sg.h5'.format(keyword))
        weights = model.get_weights()[0]
        weights = weights[1:]
        
        #print(weights.shape)

        distance_matrix = euclidean_distances(weights)
        #print(distance_matrix)
        #print(distance_matrix.shape)

        tokenizer = text.Tokenizer()
        stoplist = get_stop_words('en')
        for sp in stoplist :
            paragraphics = paragraphics.lower().replace(' {} '.format(sp.lower()),'')
            paragraphics = paragraphics.lower().replace(' {}.'.format(sp.lower()),'')
            paragraphics = paragraphics.lower().replace('.{} '.format(sp.lower()),'')
        tx=paragraphics.split('\n')     
        tokenizer.fit_on_texts(tx)
        word2id = tokenizer.word_index
        id2word = {v:k for k, v in word2id.items()}
        #print(pd.DataFrame(weights, index=list(id2word.values())[0:]).head(40))

        similar_words = {}
        try :
            i = 0
            #print(sorted(distance_matrix[word2id[word]-1]))
            for idx in distance_matrix[word2id[word]-1].argsort()[0:20]+1 :
                similar_words.setdefault(id2word[idx],sorted(distance_matrix[word2id[word]-1])[i])
            #similar_words =  {id2word[idx] : weights[word2id[word]-1].argsort()[idx] for idx in distance_matrix[word2id[word]-1].argsort()[0:20]+1}
                i += 1
        except :
            isKey = False
        print('{} : {}'.format(word,similar_words)) 
        return isKey,similar_words
        