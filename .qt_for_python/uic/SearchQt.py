# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Master Degree\Lesson\web crawler\Project\gui\SearchQt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabIRsys = QtWidgets.QTabWidget(self.centralwidget)
        self.tabIRsys.setGeometry(QtCore.QRect(0, 0, 721, 641))
        self.tabIRsys.setObjectName("tabIRsys")
        self.tab_hw1 = QtWidgets.QWidget()
        self.tab_hw1.setObjectName("tab_hw1")
        self.textEdit = QtWidgets.QTextEdit(self.tab_hw1)
        self.textEdit.setGeometry(QtCore.QRect(1, 230, 711, 381))
        self.textEdit.setObjectName("textEdit")
        self.lbl_Wds = QtWidgets.QLabel(self.tab_hw1)
        self.lbl_Wds.setGeometry(QtCore.QRect(320, 50, 61, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Wds.sizePolicy().hasHeightForWidth())
        self.lbl_Wds.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_Wds.setFont(font)
        self.lbl_Wds.setScaledContents(False)
        self.lbl_Wds.setObjectName("lbl_Wds")
        self.lbl_MSens = QtWidgets.QLabel(self.tab_hw1)
        self.lbl_MSens.setGeometry(QtCore.QRect(320, 120, 61, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_MSens.sizePolicy().hasHeightForWidth())
        self.lbl_MSens.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_MSens.setFont(font)
        self.lbl_MSens.setScaledContents(False)
        self.lbl_MSens.setObjectName("lbl_MSens")
        self.btn_SetRoot = QtWidgets.QPushButton(self.tab_hw1)
        self.btn_SetRoot.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.btn_SetRoot.setObjectName("btn_SetRoot")
        self.label_4 = QtWidgets.QLabel(self.tab_hw1)
        self.label_4.setGeometry(QtCore.QRect(250, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.tab_hw1)
        self.label_3.setGeometry(QtCore.QRect(250, 70, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbl_Chars = QtWidgets.QLabel(self.tab_hw1)
        self.lbl_Chars.setGeometry(QtCore.QRect(320, 70, 61, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Chars.sizePolicy().hasHeightForWidth())
        self.lbl_Chars.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_Chars.setFont(font)
        self.lbl_Chars.setScaledContents(False)
        self.lbl_Chars.setObjectName("lbl_Chars")
        self.TV_Root = QtWidgets.QTreeView(self.tab_hw1)
        self.TV_Root.setGeometry(QtCore.QRect(1, 30, 241, 192))
        self.TV_Root.setObjectName("TV_Root")
        self.txt_Root = QtWidgets.QLineEdit(self.tab_hw1)
        self.txt_Root.setGeometry(QtCore.QRect(80, 0, 611, 20))
        self.txt_Root.setObjectName("txt_Root")
        self.btn_SearchKey = QtWidgets.QPushButton(self.tab_hw1)
        self.btn_SearchKey.setGeometry(QtCore.QRect(247, 90, 75, 23))
        self.btn_SearchKey.setObjectName("btn_SearchKey")
        self.txt_keyword = QtWidgets.QLineEdit(self.tab_hw1)
        self.txt_keyword.setGeometry(QtCore.QRect(327, 90, 361, 20))
        self.txt_keyword.setObjectName("txt_keyword")
        self.label = QtWidgets.QLabel(self.tab_hw1)
        self.label.setGeometry(QtCore.QRect(250, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_hw1)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lbl_Sens = QtWidgets.QLabel(self.tab_hw1)
        self.lbl_Sens.setGeometry(QtCore.QRect(320, 30, 61, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Sens.sizePolicy().hasHeightForWidth())
        self.lbl_Sens.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_Sens.setFont(font)
        self.lbl_Sens.setScaledContents(False)
        self.lbl_Sens.setObjectName("lbl_Sens")
        self.tabIRsys.addTab(self.tab_hw1, "")
        self.tab_hw1_add1 = QtWidgets.QWidget()
        self.tab_hw1_add1.setObjectName("tab_hw1_add1")
        self.btn_ATC_GetRoot1 = QtWidgets.QPushButton(self.tab_hw1_add1)
        self.btn_ATC_GetRoot1.setGeometry(QtCore.QRect(0, 3, 75, 23))
        self.btn_ATC_GetRoot1.setObjectName("btn_ATC_GetRoot1")
        self.txt_ATC_Root1 = QtWidgets.QLineEdit(self.tab_hw1_add1)
        self.txt_ATC_Root1.setGeometry(QtCore.QRect(80, 3, 611, 20))
        self.txt_ATC_Root1.setObjectName("txt_ATC_Root1")
        self.txt_ATC_Root2 = QtWidgets.QLineEdit(self.tab_hw1_add1)
        self.txt_ATC_Root2.setGeometry(QtCore.QRect(80, 30, 611, 20))
        self.txt_ATC_Root2.setObjectName("txt_ATC_Root2")
        self.btn_ATC_GetRoot2 = QtWidgets.QPushButton(self.tab_hw1_add1)
        self.btn_ATC_GetRoot2.setGeometry(QtCore.QRect(0, 30, 75, 23))
        self.btn_ATC_GetRoot2.setObjectName("btn_ATC_GetRoot2")
        self.TV_Root_2 = QtWidgets.QTreeView(self.tab_hw1_add1)
        self.TV_Root_2.setGeometry(QtCore.QRect(10, 70, 331, 192))
        self.TV_Root_2.setObjectName("TV_Root_2")
        self.TV_Root_3 = QtWidgets.QTreeView(self.tab_hw1_add1)
        self.TV_Root_3.setGeometry(QtCore.QRect(370, 70, 321, 192))
        self.TV_Root_3.setObjectName("TV_Root_3")
        self.label_5 = QtWidgets.QLabel(self.tab_hw1_add1)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_hw1_add1)
        self.label_6.setGeometry(QtCore.QRect(370, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txt_ATC_Monitor = QtWidgets.QTextEdit(self.tab_hw1_add1)
        self.txt_ATC_Monitor.setGeometry(QtCore.QRect(20, 350, 671, 261))
        self.txt_ATC_Monitor.setObjectName("txt_ATC_Monitor")
        self.label_7 = QtWidgets.QLabel(self.tab_hw1_add1)
        self.label_7.setGeometry(QtCore.QRect(0, 330, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox = QtWidgets.QGroupBox(self.tab_hw1_add1)
        self.groupBox.setGeometry(QtCore.QRect(10, 267, 681, 61))
        self.groupBox.setObjectName("groupBox")
        self.rbt_ATC_Cheat = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_ATC_Cheat.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.rbt_ATC_Cheat.setChecked(True)
        self.rbt_ATC_Cheat.setObjectName("rbt_ATC_Cheat")
        self.rbt_ATC_CharCheck = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_ATC_CharCheck.setGeometry(QtCore.QRect(90, 20, 61, 16))
        self.rbt_ATC_CharCheck.setObjectName("rbt_ATC_CharCheck")
        self.gb_ATC_charMode = QtWidgets.QGroupBox(self.groupBox)
        self.gb_ATC_charMode.setEnabled(False)
        self.gb_ATC_charMode.setGeometry(QtCore.QRect(170, 5, 111, 55))
        self.gb_ATC_charMode.setTitle("")
        self.gb_ATC_charMode.setObjectName("gb_ATC_charMode")
        self.cb_ATC_Char_IgnoreSpace = QtWidgets.QCheckBox(self.gb_ATC_charMode)
        self.cb_ATC_Char_IgnoreSpace.setGeometry(QtCore.QRect(20, 10, 73, 16))
        self.cb_ATC_Char_IgnoreSpace.setObjectName("cb_ATC_Char_IgnoreSpace")
        self.cb_ATC_Char_IgnoreWardUL = QtWidgets.QCheckBox(self.gb_ATC_charMode)
        self.cb_ATC_Char_IgnoreWardUL.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.cb_ATC_Char_IgnoreWardUL.setObjectName("cb_ATC_Char_IgnoreWardUL")
        self.rbt_ATC_WardCheck = QtWidgets.QRadioButton(self.groupBox)
        self.rbt_ATC_WardCheck.setGeometry(QtCore.QRect(290, 20, 71, 16))
        self.rbt_ATC_WardCheck.setObjectName("rbt_ATC_WardCheck")
        self.gb_ATC_wordMode = QtWidgets.QGroupBox(self.groupBox)
        self.gb_ATC_wordMode.setEnabled(False)
        self.gb_ATC_wordMode.setGeometry(QtCore.QRect(371, 7, 111, 55))
        self.gb_ATC_wordMode.setTitle("")
        self.gb_ATC_wordMode.setObjectName("gb_ATC_wordMode")
        self.cb_ATC_Word_IgnoreWardUL = QtWidgets.QCheckBox(self.gb_ATC_wordMode)
        self.cb_ATC_Word_IgnoreWardUL.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.cb_ATC_Word_IgnoreWardUL.setObjectName("cb_ATC_Word_IgnoreWardUL")
        self.btn_ATC_query = QtWidgets.QPushButton(self.groupBox)
        self.btn_ATC_query.setGeometry(QtCore.QRect(540, 20, 75, 23))
        self.btn_ATC_query.setObjectName("btn_ATC_query")
        self.tabIRsys.addTab(self.tab_hw1_add1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabIRsys.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_Wds.setText(_translate("MainWindow", "0"))
        self.lbl_MSens.setText(_translate("MainWindow", "0"))
        self.btn_SetRoot.setText(_translate("MainWindow", "Get Root..."))
        self.label_4.setText(_translate("MainWindow", "Sentences :"))
        self.label_3.setText(_translate("MainWindow", "Chars : "))
        self.lbl_Chars.setText(_translate("MainWindow", "0"))
        self.btn_SearchKey.setText(_translate("MainWindow", "Search"))
        self.txt_keyword.setText(_translate("MainWindow", "KEYWORD"))
        self.label.setText(_translate("MainWindow", "Sentences :"))
        self.label_2.setText(_translate("MainWindow", "Wards :"))
        self.lbl_Sens.setText(_translate("MainWindow", "0"))
        self.tabIRsys.setTabText(self.tabIRsys.indexOf(self.tab_hw1), _translate("MainWindow", "HW1"))
        self.btn_ATC_GetRoot1.setText(_translate("MainWindow", "Get Root 1..."))
        self.btn_ATC_GetRoot2.setText(_translate("MainWindow", "Get Root 2..."))
        self.label_5.setText(_translate("MainWindow", "Source"))
        self.label_6.setText(_translate("MainWindow", "Check"))
        self.label_7.setText(_translate("MainWindow", "Result."))
        self.groupBox.setTitle(_translate("MainWindow", "Analysis Mode."))
        self.rbt_ATC_Cheat.setText(_translate("MainWindow", "全比對"))
        self.rbt_ATC_CharCheck.setText(_translate("MainWindow", "逐字元"))
        self.cb_ATC_Char_IgnoreSpace.setText(_translate("MainWindow", "忽略空白"))
        self.cb_ATC_Char_IgnoreWardUL.setText(_translate("MainWindow", "忽略大小寫"))
        self.rbt_ATC_WardCheck.setText(_translate("MainWindow", "逐詞比對"))
        self.cb_ATC_Word_IgnoreWardUL.setText(_translate("MainWindow", "忽略大小寫"))
        self.btn_ATC_query.setText(_translate("MainWindow", "Query"))
        self.tabIRsys.setTabText(self.tabIRsys.indexOf(self.tab_hw1_add1), _translate("MainWindow", "HW1-ArticleCompare"))