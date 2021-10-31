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


            #Words = KeyWordBase.SplitWords(data)
            #for Word in Words :
            #    Stem = PS.stem(PS,Word)

            #    if PortDic.__contains__(Word) != True :
            #        PortDic.setdefault(Word,Stem)

            #    if Stems.__contains__(Stem) :
            #        Stems[Stem] += 1
            #    else :
            #        Stems.setdefault(Stem,1)

            #    if WordDic.__contains__(Word) :
            #        WordDic[Word] += 1
            #    else :
            #        WordDic.setdefault(Word,1)

            #    if Index.__contains__(Word) :
            #        if str(i) not in Index[Word] :
            #            Index[Word].append(str(i))
            #    else :
            #        Index.setdefault(Word,[])
            #        Index[Word].append(str(i))