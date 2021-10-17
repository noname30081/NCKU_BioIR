from re import split
from xml.etree.ElementTree import XML
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ArticleCompare import MapMode, Setting

import gui.Ui_SearchQt as ui
from SearchEngine import SearchEngine as engine
from SearchEngine import LoadMode
from fulltextBase import Format
from SearchEngine import SearchEngine 

class Main(QMainWindow, ui.Ui_MainWindow):
    bb = ''
    def __init__(self):
         super().__init__()
         self.setupUi(self)
         self.Delegent_Static_SingleSlot()
         SearchEngine.StartEngine(engine)
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
    

if __name__ == '__main__':
    import sys    
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())