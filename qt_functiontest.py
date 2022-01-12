from codecs import StreamWriter
from operator import invert
from re import split
from xml.etree.ElementTree import XML
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from ArticleCompare import MapMode, Setting
from PyQt5 import QtChart
from PyQt5 import QtWidgets

import gui.Ui_SearchQt as ui
import gui.Ui_Indexing_note as idxnote
from SearchEngine import SearchEngine as engine
from SearchEngine import LoadMode
from fulltextBase import Format
from SearchEngine import SearchEngine 
from Indexing import Indexing as idxing

from LoadData import LoadData
from LoadData import LoadData as ld

import glob
import pandas as pd
from keywordBase import KeyWordBase
import pymongo as pymong
from DataSet import DataSet
from DataSet import DataSet as ds

import tensorflow as tf
import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense, Embedding, Lambda
from keras.preprocessing import text
from keras.utils import np_utils
from keras.preprocessing import sequence
from IPython.display import SVG

from Word2Vec import Word2Vec
from stop_words import get_stop_words

import math
import time


class Main(QMainWindow, ui.Ui_MainWindow):
    bb = ''
    myclient = DataSet('localhost','27017')
    #myclient = pymong.MongoClient("mongodb://localhost:27017/")
    #mydb = myclient["local"]
    lay = QtWidgets.QHBoxLayout()
    def __init__(self):
         super().__init__()
         self.setupUi(self)
         self.Delegent_Static_SingleSlot()
         self.QCharWidget()
         SearchEngine.StartEngine(engine)
         self.DataBase()
    #Qt Form to Python Method
    def Delegent_Static_SingleSlot(self) :
        self.btn_SetRoot.clicked.connect(self.btn_SetRoot_Click)
        self.TV_Root.clicked.connect(self.TV_Root_Click)
        self.btn_SearchKey.clicked.connect(self.btn_search_click)
        self.rbt_ATC_Cheat.clicked.connect(self.rbt_ATC_Cheat_click)
        self.rbt_ATC_CharCheck.clicked.connect(self.rbt_ATC_CharCheck_click)
        self.rbt_ATC_WardCheck.clicked.connect(self.rbt_ATC_WordCheck_click)
        self.btn_ATC_GetRoot1.clicked.connect(self.btn_ATC_GetRoot1_click)
        self.btn_ATC_GetRoot2.clicked.connect(self.btn_ATC_GetRoot2_click)   
        self.TV_Root_2.clicked.connect(self.TV_Root2_Click)
        self.TV_Root_3.clicked.connect(self.TV_Root3_Click)  
        self.btn_ATC_query.clicked.connect(self.btn_ATC_query_Click)
        self.btn_HW2_Root.clicked.connect(self.btn_HW2_Root_Click)
        self.lineEdit.returnPressed.connect(self.LineEditreturnPressed)
        self.HS_IDX_TotalNum.valueChanged.connect(self.HS_IDX_TotalNum_valueChanged)
        self.HS_IDX_swrate.valueChanged.connect(self.HS_IDX_swrate_valueChanged)
        self.HS_IDX_ifrate.valueChanged.connect(self.HS_IDX_ifrate_valueChanged)
        self.btn_IDX_PorterNote.clicked.connect(self.btn_IDX_PorterNote_clicked)
        self.btn_IDX_Indexing.clicked.connect(self.btn_IDX_Indexing_clicked)
        self.btn_IDX_test.clicked.connect(self.btn_IDX_test_clicked)
        self.btn_HW3_add_GetModel.clicked.connect(self.btn_HW3_add_GetModel_clicked)
        self.btn_HW3_cauTF.clicked.connect(self.btn_HW3_cauTF_clicked)
        self.btn_HW3_cauIDF.clicked.connect(self.btn_HW3_cauIDF_clicked)
        self.btn_HW3_TrainModel.clicked.connect(self.btn_HW3_TrainModel_clicked)
        self.cb_HW3_quarytxt.currentTextChanged.connect(self.cb_HW3_quarytxt_currentTextChanged)
        self.tb_HW3_w2v.clicked.connect(self.tb_HW3_w2v_clicked)
        self.txt_HW3_qNear.returnPressed.connect(self.txt_HW3_qNear_returnPressed)
    def QCharWidget(self) :
        self.serials = QLineSeries()
        self.Chart = QChart()     
        self.Chart.addSeries(self.serials)
        self.chartview = QtChart.QChartView(self.Chart)
        self.lay = QtWidgets.QHBoxLayout(self.wg_IDX_chart)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.chartview)      
        return
    def DataBase(self) : 
        self.myclient.LinktoDB("local")
        self.myclient.LinktoCollection("local",'testColl')
        self.myclient.LinktoCollection("local",'BioIR_covid19')
        self.myclient.LinktoCollection("local",'BioIR_covid19_index')
        self.myclient.LinktoCollection("local",'BioIR_LoadData')
        self.myclient.LinktoCollection("local",'tf-idf')
        self.myclient.LinktoCollection("local",'Atopic_dermatitis')
    #region <WH1>
    def btn_SetRoot_Click(self) :
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Video Directory", QDir.currentPath());
        self.txt_Root.setText(directory)
        model = QFileSystemModel()
        model.setRootPath(directory)
        model.setFilter(QDir.Files | QDir.Dirs | QDir.NoDotDot)
        idx = model.index(directory)
        self.TV_Root.setModel(model)
        self.TV_Root.setRootIndex(idx)
    def TV_Root_Click(self,Qmodelidx) :
        model = (QFileSystemModel)(self.TV_Root.model()) 
        self.bb = model.filePath(Qmodelidx)
        SearchEngine.LoadSource(engine,self.bb,LoadMode.Local)
        tagname = 'AbstractText'
        form = Format.XML
        if(self.bb[-4:] == 'json') : tagname = 'tweet_text';form = Format.JSON;       
        Sents,keysents,parawordsum,chall = SearchEngine.ParaGraphInfo(engine,tagname,"",form)
        self.lbl_Sens.setText(str(len(Sents)))
        self.lbl_Wds.setText(str(parawordsum)) 
        self.lbl_Chars.setText(str(chall))
    def btn_search_click(self):
        tagname = 'AbstractText'
        form = Format.XML
        if(self.bb[-4:] == 'json') : tagname = 'tweet_text';form = Format.JSON;  
        Sents,keysents,parawordsum,chall = SearchEngine.ParaGraphInfo(engine,tagname,self.txt_keyword.text(),form)
        keywords = []
        keyword = self.txt_keyword.text()
        keyword = keyword[:1].upper() + keyword[1:].lower()
        keywords.append(self.txt_keyword.text())
        if(self.txt_keyword.text() != keyword) :
            keywords.append(keyword)
        cssformat = self.SentencesBrKeyWords(keysents,keywords)
        strColor = '<span style="margin-right:12px;color:white">{}</span>'.format(cssformat)
        font = QFont("Microsoft JhengHei",11,11,False)
        self.textEdit.setFont(font)
        self.textEdit.setHtml(strColor)
        self.textEdit.setStyleSheet("background-color:black")
        self.lbl_MSens.setText(str(len(keysents)))
    def SentencesBrKeyWords(self, sent , keywords ) :
        strOut = ''
        for sen in sent :
            for kw in keywords :
                sen = sen.replace(kw,'<span style="background-color:white;color:black">{}</span>'.format(kw))
            strOut+='{}<br><br>'.format(sen)
        return strOut
    #endregion
    #region <WH1 - Addition Work>
    def rbt_ATC_Cheat_click(self) :
        self.gb_ATC_charMode.setEnabled(False)
        self.gb_ATC_wordMode.setEnabled(False)
    def rbt_ATC_CharCheck_click(self) :
        self.gb_ATC_charMode.setEnabled(True)
        self.gb_ATC_wordMode.setEnabled(False)   
    def rbt_ATC_WordCheck_click(self) :
        self.gb_ATC_charMode.setEnabled(False)
        self.gb_ATC_wordMode.setEnabled(True)                
    def btn_ATC_GetRoot1_click(self) :
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Video Directory", QDir.currentPath());
        self.txt_ATC_Root1.setText(directory)
        model = QFileSystemModel()
        model.setRootPath(directory)
        model.setFilter(QDir.Files | QDir.Dirs | QDir.NoDotDot)
        idx = model.index(directory)
        self.TV_Root_2.setModel(model)
        self.TV_Root_2.setRootIndex(idx)        
    def btn_ATC_GetRoot2_click(self) :
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Video Directory", QDir.currentPath());
        self.txt_ATC_Root2.setText(directory)
        model = QFileSystemModel()
        model.setRootPath(directory)
        model.setFilter(QDir.Files | QDir.Dirs | QDir.NoDotDot)
        idx = model.index(directory)
        self.TV_Root_3.setModel(model)
        self.TV_Root_3.setRootIndex(idx)     
    ATC_SRootPath = ''
    ATC_TRootPath = ''
    Source_Sdata = ''
    Source_Sents = []
    Target_Sdata = ''
    Target_Sents = []
    def TV_Root2_Click(self,Qmodelidx) :
        model = (QFileSystemModel)(self.TV_Root_2.model()) 
        self.ATC_SRootPath = model.filePath(Qmodelidx)
        SearchEngine.LoadSource(engine,self.ATC_SRootPath,LoadMode.Local)
        tagname = 'AbstractText'
        form = Format.XML
        if(self.ATC_SRootPath[-4:] == 'json') : tagname = 'tweet_text';form = Format.JSON;       
        self.Source_Sdata,self.Source_Sents,chall = SearchEngine.ParaGraphByTag(engine,tagname,form)
        print(self.Source_Sdata)
    def TV_Root3_Click(self,Qmodelidx) :
        model = (QFileSystemModel)(self.TV_Root_3.model()) 
        self.ATC_TRootPath = model.filePath(Qmodelidx)
        SearchEngine.LoadSource(engine,self.ATC_TRootPath,LoadMode.Local)
        tagname = 'AbstractText'
        form = Format.XML
        if(self.ATC_TRootPath[-4:] == 'json') : tagname = 'tweet_text';form = Format.JSON;       
        self.Target_Sdata,self.Target_Sents,chall = SearchEngine.ParaGraphByTag(engine,tagname,form)
        print(self.Target_Sdata)
    def btn_ATC_query_Click(self) : 
        match = False
        cssformat = ''
        setting = None
        if(self.rbt_ATC_Cheat.isChecked()) :
            match,cssformat = SearchEngine.CompareArticles(engine,self.Source_Sdata,self.Target_Sdata,MapMode.Paragraph,setting)
        elif(self.rbt_ATC_CharCheck.isChecked()) :
            if(self.cb_ATC_Char_IgnoreSpace.isChecked()) : 
                if(setting is None) :
                    setting = Setting.SKIP_SPACE
                else :
                    setting |= Setting.SKIP_SPACE
            if(self.cb_ATC_Char_IgnoreWardUL.isChecked()) : 
                if(setting is None) :
                    setting = Setting.SKIP_WORD_UL      
                else :          
                    setting |= Setting.SKIP_WORD_UL
            match,cssformat = SearchEngine.CompareArticles(engine,self.Source_Sdata,self.Target_Sdata,MapMode.char,setting)
        elif(self.rbt_ATC_WardCheck.isChecked()) :
            if(self.cb_ATC_Word_IgnoreWardUL.isChecked()) : 
                if(setting is None) :
                    setting = Setting.SKIP_WORD_UL
                else :
                    setting |= Setting.SKIP_WORD_UL
            match,cssformat = SearchEngine.CompareArticles(engine,self.Source_Sdata,self.Target_Sdata,MapMode.Ward,setting)            
        strColor = '<span style="margin-right:12px;color:white">{}</span>'.format(cssformat)
        font = QFont("Microsoft JhengHei",11,11,False)
        self.txt_ATC_Monitor.setFont(font)
        self.txt_ATC_Monitor.setHtml(strColor)
        self.txt_ATC_Monitor.setStyleSheet("background-color:black")
        return    
    #endregion
    #region <HW2>
    dataset = pd.DataFrame([], columns=[])
    csvfiles = []
    MAX = 2048
    def btn_HW2_Root_Click(self) :
        #說明視窗
        self.idxnote = IDX_Sub()
        self.btn_IDX_PorterNote.setEnabled(True)
        self.btn_IDX_Indexing.setEnabled(True)
        #Load csv
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Video Directory", QDir.currentPath());
        self.txt_IDX_Root.setText(directory)
        files = glob.glob(r'{}/{}'.format(directory,'*.csv'))
        i = 0
        for file in files :
            files[i] = file.replace('\\','/')
            i+=1
        if len(files) == 0 :
            self.HS_IDX_TotalNum.setEnabled(False)
            self.lineEdit.setEnabled(False)
            return
        self.csvfiles = files
        self.HS_IDX_TotalNum.setEnabled(True)
        self.lineEdit.setEnabled(True)
        tags = LoadData.GetTags(files[0])
        self.cb_IDX_tagname.clear()
        self.cb_IDX_tagname.addItems(tags)
        self.cb_IDX_tagname.setEnabled(True)
        self.cb_IDX_tagname.setCurrentIndex(1)

        Columns = tags
        rows = []
        for file in files :
            Rows = LoadData.GetRowsByCsvTag(file)
            for row in Rows :
                rows.append(row)
                #self.InsertDat(file,0,tags,row,'local','BioIR_covid19')
        self.dataset = pd.DataFrame(rows, columns=Columns)
        self.MAX = len(rows)
        self.HS_IDX_TotalNum.setMaximum(self.MAX)
        return
    def LineEditreturnPressed(self):
        try :
            count = int(self.lineEdit.text())
            if count < 1 :
                count = 1
            elif count > self.MAX :
                count = self.MAX
            va = self.HS_IDX_TotalNum.value()
            self.HS_IDX_TotalNum.setValue(count)
            self.lineEdit.setText(str(count))
            if(va == count) :
                self.DataSetting(count)
        except Exception as ex:
            self.lineEdit.setText('1')
            print(ex)
    def HS_IDX_TotalNum_valueChanged(self,value):
        self.lineEdit.setText(str(value))
        self.DataSetting(value)
    ft = False
    def DataSetting(self,count : int) :
        paras = self.dataset.loc[0:count-1,self.cb_IDX_tagname.currentText()]
        wrsort,worddic,Index,StemsSort,Stems,PortDic = idxing.ParagraphicByList_(idxing,paras,self.cb_IDX_sppkg.isChecked())
        self.tb_IDX_show.setColumnCount(2)
        header = ['Word','Sum']
        self.tb_IDX_show.setHorizontalHeaderLabels(header)
        sortedDic = []
        sumwds = 0
        if self.cb_Porter.isChecked() :
            sortedDic = StemsSort
        else :
            sortedDic = wrsort
        sumwd = [i[1] for i in sortedDic]
        sumwds = sum(sumwd)
        rows = len(sortedDic)
        self.tb_IDX_show.setRowCount(int(rows))    
        ser = QLineSeries()
        serName = ''
        if self.cb_Porter.isChecked():
            serName = 'Po-'    
        serName += 'Words[{}-{}%-{}%]'.format(str(count),str(self.HS_IDX_swrate.value()),str(self.HS_IDX_ifrate.value()))
        ser.setName(serName)
        su = 0
        j=0
        for i in range(rows) :
            su += int(sortedDic[i][1])
            if su >= int(sumwds*(1-self.HS_IDX_ifrate.value()*0.01)) :
                break
            if su <=int(sumwds*self.HS_IDX_swrate.value()*0.01) and self.HS_IDX_swrate.value() != 0:
                j = i+1
                continue
            self.tb_IDX_show.setItem(int(i-j),0,QtWidgets.QTableWidgetItem(str(sortedDic[i][0])))
            self.tb_IDX_show.setItem(int(i-j),1,QtWidgets.QTableWidgetItem(str(sortedDic[i][1])))   
            if self.cb_IDX_doLn.isChecked() :
                if i-j > 0 :
                    ser.append(math.log(i-j),math.log(sortedDic[i][1]))
                else :
                    ser.append(0,math.log(sortedDic[i][1]))
            elif self.cb_IDX_doLog10.isChecked() :
                ser.append(math.log10(i-j),math.log10(sortedDic[i][1]))
            else :
                ser.append(i-j,sortedDic[i][1])
        
        if self.cb_CC.isChecked() != True : 
            self.Chart.removeAllSeries()
        self.Chart.addSeries(ser)
        self.Chart.setAnimationOptions(QChart.SeriesAnimations)

        self.Chart.legend().setVisible(True)
        self.Chart.legend().setAlignment(Qt.AlignBottom)
        font = self.Chart.legend().font()
        font.setPointSize(18)
        self.Chart.legend().setFont(font)
        self.Chart.legend().setFont(QFont('Calibri'))
        self.Chart.setTitle('Zipf')

        x_Aix = QValueAxis()
        x_Aix.setRange(0,rows)
        x_Aix.setTickCount(rows)
        x_Aix.setMinorTickCount(0)
        x_Aix.setLabelFormat('%d')
        
        y_Aix = QValueAxis()
        y_Aix.setRange(0,wrsort[i][1])
        y_Aix.setTickCount(100)
        y_Aix.setMinorTickCount(0)
        y_Aix.setLabelFormat('%d')

        self.chartview.chart().setAxisX(x_Aix)
        self.chartview.chart().setAxisX(y_Aix)
        self.chartview.chart().createDefaultAxes()

        self.polist = sorted(PortDic.items() , key=lambda x:x[0])
        self.idxlist = sorted(Index.items() , key=lambda x:x[0])

    def HS_IDX_swrate_valueChanged(self,value):
        self.txt_IDX_swrate.setText('{}%'.format(str(value)))
    def HS_IDX_ifrate_valueChanged(self,value):
        self.txt_IDX_ifrate.setText('{}%'.format(str(value)))
    def btn_IDX_PorterNote_clicked(self) :
        self.idxnote.tb_IDX_show.setColumnCount(2)
        noteheader = ['Word','Po-Word']
        self.idxnote.tb_IDX_show.setHorizontalHeaderLabels(noteheader)
        self.idxnote.tb_IDX_show.setRowCount(len(self.polist))
        for i in range(len(self.polist)) :
            self.idxnote.tb_IDX_show.setItem(int(i),0,QtWidgets.QTableWidgetItem(str(self.polist[i][0])))
            self.idxnote.tb_IDX_show.setItem(int(i),1,QtWidgets.QTableWidgetItem(str(self.polist[i][1])))
        self.idxnote.show()
    def btn_IDX_Indexing_clicked(self) :
        self.idxnote.tb_IDX_show.setColumnCount(2)
        noteheader = ['Word','Index']
        self.idxnote.tb_IDX_show.setHorizontalHeaderLabels(noteheader)
        self.idxnote.tb_IDX_show.setRowCount(len(self.idxlist))
        for i in range(len(self.idxlist)) :
            self.idxnote.tb_IDX_show.setItem(int(i),0,QtWidgets.QTableWidgetItem(str(self.idxlist[i][0])))
            self.idxnote.tb_IDX_show.setItem(int(i),1,QtWidgets.QTableWidgetItem(str(sorted(self.idxlist[i][1] , key=lambda x:int(x)))))
        self.idxnote.show()
    def btn_IDX_test_clicked(self) :
        #gg = list(self.myclient.dbs['local']["Collections"]['BioIR_covid19'].find({},no_cursor_timeout=True))
        #Word2Vec.VectToken(Word2Vec,gg)
        #Word2Vec.LoadModel(Word2Vec,gg)
        #gg = open(r'../pubmed_query/zoonoses_1000.txt', mode='r')
        #Word2Vec.VectToken2(Word2Vec,gg.read(),'Cross-species transmission')
        #Word2Vec.LoadModel2(Word2Vec,gg.read(),'Cross-species transmission')
        #Word2Vec.SkipGram_Training_2(Word2Vec,gg.read(),'zoonoses')
        #Word2Vec.LoadModel3(Word2Vec,gg.read(),'zoonoses')
        #gg.close()

        #gg = open(r'../pubmed_query/Atopic dermatitis_250.txt', mode='r')
        #Word2Vec.SkipGram_Training_2(Word2Vec,gg.read(),'Atopic_dermatitis')
        #Word2Vec.LoadModel3(Word2Vec,gg.read(),'Atopic_dermatitis')
        #gg.close()
        rownum = self.tb_IDX_show.rowCount()
        header = "{},{},{}\n".format("Idx","Word","Num")
        wr = ""
        for i in range(rownum) :
            wr += "{},{},{}\n".format(i,self.tb_IDX_show.item(i,0).text() ,self.tb_IDX_show.item(i,1).text())
        wr = header + wr

        localtime = time.localtime()
        result = time.strftime("%Y%m%d%I%M%S", localtime)

        f = open(r'D:/Master Degree/Lesson/web crawler/Final/Dataset/statics/{}.csv'.format(result), mode='w')
        f.write(wr)
        f.close()
        pass
    def generate_context_word_pairs(self,corpus, window_size, vocab_size):
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
    #to Dataset
    def InsertDat(self,sour,idx,tags,row,dbname,collection) :
        Tags = {}
        i = 0
        for tag in tags :
            if Tags.__contains__(tag) == False:
                Tags.setdefault(tag,{})
            if Tags[tag].__contains__('ORIG') == False :
                Tags[tag].setdefault('ORIG',row[i])
            wlist,stems,stemlist = idxing.splitAndstemWords(row[i])
            if Tags[tag].__contains__('WORDS') == False :
                Tags[tag].setdefault('WORDS',wlist)
            if Tags[tag].__contains__('STEMS') == False :
                Tags[tag].setdefault('STEMS',stems)      
            i += 1
        query = {}
        #idx = len(list(self.myclient.dbs['local']["Collections"]['BioIR_covid19'].find(query)))
        idx = len(list(self.myclient.dbs['local']["Collections"][collection].find(query)))
        dataInset = {"source":sour,"IDX":idx,"Tags":Tags}
        #self.myclient.InsertData('local','BioIR_covid19',dataInset)
        self.myclient.InsertData(dbname,collection,dataInset)
    #endregion
    #region <HW3>
    def btn_HW3_add_GetModel_clicked(self) :
        '''
        source = r'../pubmed_query/Atopic dermatitis_250.txt'
        txt = open(source, mode='r').read()
        paralist = Word2Vec.PudmedStructive(Word2Vec,txt)
        for para in paralist:
            self.InsertDatPubmed(source,para,'local','Atopic_dermatitis')
        pass
        '''

    def InsertDatPubmed(self,sour,para,dbname,collection) :
        Tags = {}
        i = 0
        paraIndex = int(para['index'])
        sentIndex = 0
        sentlist = para['sentences']      
        for sent in sentlist :
            if sent is None :
                continue
            if len(sent) < 5 :
                continue
            dataInset = {"source":sour,"ParaIndex":paraIndex}
            query = {}
            sentIndex = len(list(self.myclient.dbs['local']["Collections"][collection].find(query)))
            if dataInset.__contains__('SentIndex') == False :
                dataInset.setdefault('SentIndex',sentIndex)            
            if dataInset.__contains__('ORIG') == False :
                dataInset.setdefault('ORIG',sent)
            wlist,stems,stemlist = idxing.splitAndstemWordsByKeras(sent)
            if dataInset.__contains__('WORDS') == False :
                dataInset.setdefault('WORDS',wlist)
            if dataInset.__contains__('STEMS') == False :
                dataInset.setdefault('STEMS',stems)      
            self.myclient.InsertData(dbname,collection,dataInset)
    def btn_HW3_cauTF_clicked(self) :
        myQuary = {'ParaIndex':0}
        rt = self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({})
        SumWords = {}
        for duc in rt :
            for key in duc['WORDS'].keys() :
                if key in SumWords :
                    SumWords[key] += duc['WORDS'][key]
                else :
                    SumWords.setdefault(key,duc['WORDS'][key])
        
        rt = self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({})
        for duc in rt :
            tfparas = list(self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({'ParaIndex':duc['ParaIndex']}))
            tfnew = {}
            for key in SumWords.keys() :
                sumtemp = 0
                for tfpara in tfparas:
                    if key in tfpara['WORDS'] :
                        sumtemp += tfpara['WORDS'][key]
                if sumtemp != 0 :
                    sumtemp = 1 + math.log(sumtemp)
                tfnew.setdefault(key,sumtemp)
            self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].update_one({'_id':duc['_id']},{'$set':{'tf_para':tfnew}})

        rt = self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({})
        for duc in rt :
            tfparas = list(self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({'SentIndex':duc['SentIndex']}))
            tfnew = {}
            for key in SumWords.keys() :
                sumtemp = 0
                for tfpara in tfparas:
                    if key in tfpara['WORDS'] :
                        sumtemp += tfpara['WORDS'][key]
                if sumtemp != 0 :
                    sumtemp = 1 + math.log(sumtemp)
                tfnew.setdefault(key,sumtemp)
            self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].update_one({'_id':duc['_id']},{'$set':{'tf_sent':tfnew}})

        rt = self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({})
        for duc in rt :
            tfparas = list(self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({'ParaIndex':duc['ParaIndex']}))
            tfnew = {}
            for key in SumWords.keys() :
                sumtemp = 0
                for tfpara in tfparas:
                    if key in tfpara['WORDS'] :
                        sumtemp += tfpara['WORDS'][key]
                if sumtemp == 0:
                    sumtemp = 0
                else :
                    sumtemp = math.log(SumWords[key]/sumtemp)
                tfnew.setdefault(key,sumtemp)
            self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].update_one({'_id':duc['_id']},{'$set':{'idf_para':tfnew}})

        rt = self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({})
        for duc in rt :
            tfparas = list(self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({'SentIndex':duc['SentIndex']}))
            tfnew = {}
            for key in SumWords.keys() :
                sumtemp = 0
                for tfpara in tfparas:
                    if key in tfpara['WORDS'] :
                        sumtemp += tfpara['WORDS'][key]
                if sumtemp == 0:
                    sumtemp = 0
                else :
                    sumtemp = math.log(SumWords[key]/sumtemp)
                tfnew.setdefault(key,sumtemp)
            self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].update_one({'_id':duc['_id']},{'$set':{'idf_sent':tfnew}})
        pass
    def btn_HW3_cauIDF_clicked(self) :
        rt = self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find({})
        SumWords = {}
        gg = open(r'../pubmed_query/Atopic dermatitis_250.txt', mode='r')
        parag = gg.read()
        gg.close()
        for duc in rt :
            for key in duc['WORDS'].keys() :
                if key in SumWords :
                    SumWords[key] += duc['WORDS'][key]
                else :
                    SumWords.setdefault(key,duc['WORDS'][key])        
        self.labelDic = {}
        labelMax = 40
        count = 0
        stoplist = get_stop_words('en')
        sorted_ = sorted(SumWords.items(), key=lambda x:x[1],reverse=True)
        #for key in SumWords.keys() :
        for key in sorted_ :
            if key[0] in stoplist :
                continue
            if len(key[0]) == 1 :
                continue            
            Exist = False
            for labelkey in self.labelDic.keys() :
                if key[0] in self.labelDic[labelkey] :
                    Exist = True
                    break
            if Exist == False :    
                isKey , smillar = Word2Vec.createLabel(Word2Vec,parag,key[0],'Atopic_dermatitis')
                if isKey == False :
                    continue
                self.labelDic.setdefault(key[0],smillar)
                count += 1
            if count >= labelMax :
                break
        self.cb_HW3_quarytxt.addItems(self.labelDic.keys())
        pass
    def btn_HW3_TrainModel_clicked(self) :
        pass
    def cb_HW3_quarytxt_currentTextChanged(self,value) :
        self.tb_HW3_w2v.clear()
        self.tb_HW3_w2v.setColumnCount(2)
        header = ['Word','Distance']
        self.tb_HW3_w2v.setHorizontalHeaderLabels(header)
        self.tb_HW3_w2v.setRowCount(len(self.labelDic[value].keys()))
        i = 0
        for key in self.labelDic[value].keys() :
            self.tb_HW3_w2v.setItem(int(i),0,QtWidgets.QTableWidgetItem(str(key)))
            self.tb_HW3_w2v.setItem(int(i),1,QtWidgets.QTableWidgetItem(str(self.labelDic[value][key])))   
            i += 1   
    def tb_HW3_w2v_clicked(self,item) :     
        self.txt_HW3_qNear.setText(self.tb_HW3_w2v.item(item.row(),0).text())
        print(self.tb_HW3_w2v.item(item.row(),0).text())
    def txt_HW3_qNear_returnPressed(self) :
        self.txt_HW3_result.clear()
        myQuery = {'$or':[]}
        for key in self.labelDic[self.cb_HW3_quarytxt.currentText()].keys() :
            qu = {'WORDS.{}'.format(key):{'$gt':0}}
            myQuery['$or'].append(qu)
            #myQuery.setdefault('tf_para.{}'.format(key),'>0')
        rt = self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find(myQuery)    
        self.qre = list(rt)
        print(len(self.qre))

        ranklist = []
        for ducs in self.qre :
            ranking = {}
            score_para = 0
            score_sent = 0
            for key in ducs['WORDS'].keys() :
                if key == self.cb_HW3_quarytxt.currentText() :
                    score_para += (ducs['tf_para'][key] * ducs['idf_para'][key])
                    score_sent += (ducs['tf_sent'][key] * ducs['idf_sent'][key])
                elif key == self.txt_HW3_qNear.text() :
                    score_para += (ducs['tf_para'][key] * ducs['idf_para'][key])
                    score_sent += (ducs['tf_sent'][key] * ducs['idf_sent'][key])
                elif key in self.labelDic[self.cb_HW3_quarytxt.currentText()].keys() :
                    score_para += math.pow(ducs['tf_para'][key] * ducs['idf_para'][key],2) / (len(ducs['WORDS'].keys()))
                    score_sent += math.pow(ducs['tf_sent'][key] * ducs['idf_sent'][key],2) / (len(ducs['WORDS'].keys()))
            ranking.setdefault('SentIndex',ducs['SentIndex'])
            ranking.setdefault('Score_para',score_para)
            ranking.setdefault('Score_sent',score_sent)
            ranklist.append(ranking)
        if self.rto_Paras.isChecked() :
            ranklist.sort(key=lambda r:r['Score_para'] ,reverse=True)
        else :
            ranklist.sort(key=lambda r:r['Score_sent'] ,reverse=True)
    
        cssformat = ''
        count = 0
        for ran in ranklist :
            myQuery = {'SentIndex' : ran['SentIndex']}
            select = list(self.myclient.dbs['local']["Collections"]['Atopic_dermatitis'].find(myQuery))
            css = ''
            css += select[0]['ORIG']
            for key in self.labelDic[self.cb_HW3_quarytxt.currentText()].keys() :
                if len(key) == 1 :
                    continue
                if (key == self.cb_HW3_quarytxt.currentText()) or (key == self.txt_HW3_qNear.text()) :
                    css = css.replace(' {} '.format(key),' <span style="background-color:yellow;color:black">{}</span> '.format(key))
                    css = css.replace(' {}.'.format(key),' <span style="background-color:yellow;color:black">{}</span>.'.format(key))
                    css = css.replace(' {}-'.format(key),' <span style="background-color:yellow;color:black">{}</span>-'.format(key))
                    css = css.replace('-{} '.format(key),'-<span style="background-color:yellow;color:black">{}</span> '.format(key))
                    css = css.replace('-{}-'.format(key),'-<span style="background-color:yellow;color:black">{}</span>-'.format(key))
                    css = css.replace(' {},'.format(key),' <span style="background-color:yellow;color:black">{}</span>,'.format(key))
                else :
                    if(self.cb_HW3_quarytxt.currentText().__contains__(key) or self.txt_HW3_qNear.text().__contains__(key)) :
                        continue
                    css = css.replace(' {} '.format(key),' <span style="background-color:white;color:black">{}</span> '.format(key))
                    css = css.replace(' {}.'.format(key),' <span style="background-color:white;color:black">{}</span>.'.format(key))
                    css = css.replace(' {}-'.format(key),' <span style="background-color:white;color:black">{}</span>-'.format(key))
                    css = css.replace('-{} '.format(key),'-<span style="background-color:white;color:black">{}</span> '.format(key))
                    css = css.replace('-{}-'.format(key),'-<span style="background-color:white;color:black">{}</span>-'.format(key))
                    css = css.replace(' {},'.format(key),' <span style="background-color:white;color:black">{}</span>,'.format(key))                    
            css += ' Para Score : {} , Sent Score : {} , ParaIndex : {} , SentIndex{}.'.format(ran['Score_para'],ran['Score_sent'],select[0]['ParaIndex'],select[0]['SentIndex'])
            css += '<br><br>'
            cssformat += css
            count += 1
            if count >= 10 :
                break;

        strColor = '<span style="margin-right:12px;color:white">{}</span>'.format(cssformat)
        font = QFont("Microsoft JhengHei",11,11,False)
        self.txt_HW3_result.setFont(font)
        self.txt_HW3_result.setHtml(strColor)
        self.txt_HW3_result.setStyleSheet("background-color:black")
        pass
    #endregion

class IDX_Sub(QMainWindow, idxnote.Ui_MW_IDX_Note):
    def __init__(self):
        super().__init__()
        self.setupUi(self)     
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

if __name__ == '__main__':
    import sys    
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())