from re import split
from xml.etree.ElementTree import XML
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
    #endregion
    def SentencesBrKeyWords(self, sent , keywords ) :
        strOut = ''
        for sen in sent :
            for kw in keywords :
                sen = sen.replace(kw,'<span style="background-color:white;color:black">{}</span>'.format(kw))
            strOut+='{}<br><br>'.format(sen)
        return strOut
    def rbt_ATC_Cheat_click(self) :
        self.gb_ATC_charMode.setEnabled(False)
        self.gb_ATC_wordMode.setEnabled(False)
    def rbt_ATC_CharCheck_click(self) :
        self.gb_ATC_charMode.setEnabled(True)
        self.gb_ATC_wordMode.setEnabled(False)   
    def rbt_ATC_WordCheck_click(self) :
        self.gb_ATC_charMode.setEnabled(False)
        self.gb_ATC_wordMode.setEnabled(True)                


if __name__ == '__main__':
    import sys    
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())