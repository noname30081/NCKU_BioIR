from numba import cuda
import fulltextBase
from keywordBase import KeyWordBase
from PorterStemmer import PorterStemmer as PS
import threading
import math
import numpy
from numba import generated_jit,types

from numba.core.decorators import jit_module
from numba.core.types.misc import Object

from stop_words import get_stop_words
from keras.preprocessing import text

mutWord = threading.Lock()
mutStem = threading.Lock()
mutPort = threading.Lock()
mutIdx = threading.Lock()

class Indexing(Object):
    def Statistic_Wards(ParaGraphics) :
        Index = {}
        #for ParaGraphic in ParaGraphics :
        return
    def ParagraphicByList_(self,listdata,stopwordpkg = False):
        self.WordSort = []
        self.WordDic = {}
        self.StemsSort = []
        self.Stems = {}
        self.PortDic = {}
        self.Index = {}
        threads = []
        i = 0     
        for data in listdata :
            Words = KeyWordBase.SplitWords(data)
            thread = threading.Thread(target=self.IndexWords, args=(self,Words,i,stopwordpkg,), name='IndexWords{}'.format(i))
            threads.append(thread)
            threads[i].start()
            i += 1
        for j in range(i) :
            threads[j].join()
        
        self.WordSort = sorted(self.WordDic.items(),reverse=True, key=lambda x:x[1])
        self.StemsSort = sorted(self.Stems.items(),reverse=True, key=lambda x:x[1])
        return self.WordSort,self.WordDic,self.Index,self.StemsSort,self.Stems,self.PortDic
    def IndexWords(self,Words,inddex,stopwordpkg = False) :       
        stoplist = get_stop_words('en')
        for Word in Words :
            if stoplist.__contains__(Word) and stopwordpkg:
                continue

            Stem = PS.stem(PS,Word)

            mutPort.acquire()
            if self.PortDic.__contains__(Word) != True and Stem != Word:                
                self.PortDic.setdefault(Word,Stem)
            mutPort.release()

            mutStem.acquire()
            if self.Stems.__contains__(Stem.lower()) :
                self.Stems[Stem.lower()] += 1
            else :
                self.Stems.setdefault(Stem.lower(),1)
            mutStem.release()

            mutWord.acquire()
            if self.WordDic.__contains__(Word.lower()) :
                self.WordDic[Word.lower()] += 1
            else :
                self.WordDic.setdefault(Word.lower(),1)
            mutWord.release()

            mutIdx.acquire()
            if self.Index.__contains__(Word.lower()) :
                if str(inddex) not in self.Index[Word.lower()] :                  
                    self.Index[Word.lower()].append(str(inddex))
            else :
                self.Index.setdefault(Word.lower(),[])
                self.Index[Word.lower()].append(str(inddex))
            mutIdx.release()        
    def splitAndstemWords(paragraph) :
        #Tokenize
        Words = KeyWordBase.SplitWords(paragraph)
        #Get Stopwords
        stoplist = get_stop_words('en')
        stemlist = {}
        stems = {}
        wlist = {}
        for Word in Words :
            #Statics Words
            if wlist.__contains__(Word.lower()) :
                wlist[Word.lower()] += 1
            else :
                wlist.setdefault(Word.lower(),1)           
            #filte Stop Words
            if stoplist.__contains__(Word):
                continue
            #Do stemming
            Stem = PS.stem(PS,Word)                 
            #Save the stemed words
            if stemlist.__contains__(Word) != True and Stem != Word:                
                stemlist.setdefault(Word,Stem)        
            #Statics Stem Words      
            if stems.__contains__(Stem.lower()) :
                stems[Stem.lower()] += 1
            else :
                stems.setdefault(Stem.lower(),1)
        return wlist,stems,stemlist
    def splitAndstemWordsByKeras(paragraph) :
        #Tokenize
        tokenizer = text.Tokenizer()
        tokenizer.fit_on_texts([paragraph])
        Words = tokenizer.word_index.keys()
        #Get Stopwords
        stoplist = get_stop_words('en')
        stemlist = {}
        stems = {}
        wlist = {}
        for Word in Words :
            try :
                #Statics Words
                if wlist.__contains__(Word.lower()) :
                    wlist[Word.lower()] += 1
                else :
                    wlist.setdefault(Word.lower(),1)           
                #filte Stop Words
                if stoplist.__contains__(Word):
                    continue
                #Do stemming
                Stem = PS.stem(PS,Word)                 
                #Save the stemed words
                if stemlist.__contains__(Word) != True and Stem != Word:                
                    stemlist.setdefault(Word,Stem)        
                #Statics Stem Words      
                if stems.__contains__(Stem.lower()) :
                    stems[Stem.lower()] += 1
                else :
                    stems.setdefault(Stem.lower(),1)
            except :
                continue
        return wlist,stems,stemlist