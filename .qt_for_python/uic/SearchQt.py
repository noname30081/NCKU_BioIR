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
        MainWindow.resize(816, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabIRsys = QtWidgets.QTabWidget(self.centralwidget)
        self.tabIRsys.setGeometry(QtCore.QRect(0, 0, 811, 851))
        self.tabIRsys.setAutoFillBackground(False)
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
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_HW2_Root = QtWidgets.QPushButton(self.tab)
        self.btn_HW2_Root.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.btn_HW2_Root.setObjectName("btn_HW2_Root")
        self.HS_IDX_TotalNum = QtWidgets.QSlider(self.tab)
        self.HS_IDX_TotalNum.setEnabled(False)
        self.HS_IDX_TotalNum.setGeometry(QtCore.QRect(80, 60, 621, 22))
        self.HS_IDX_TotalNum.setMinimum(1)
        self.HS_IDX_TotalNum.setMaximum(2048)
        self.HS_IDX_TotalNum.setProperty("value", 1)
        self.HS_IDX_TotalNum.setOrientation(QtCore.Qt.Horizontal)
        self.HS_IDX_TotalNum.setObjectName("HS_IDX_TotalNum")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.txt_IDX_Root = QtWidgets.QLineEdit(self.tab)
        self.txt_IDX_Root.setGeometry(QtCore.QRect(80, 2, 621, 20))
        self.txt_IDX_Root.setObjectName("txt_IDX_Root")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txt_IDX_tagname = QtWidgets.QLineEdit(self.tab)
        self.txt_IDX_tagname.setGeometry(QtCore.QRect(80, 30, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.txt_IDX_tagname.setFont(font)
        self.txt_IDX_tagname.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_IDX_tagname.setObjectName("txt_IDX_tagname")
        self.cb_IDX_tagname = QtWidgets.QComboBox(self.tab)
        self.cb_IDX_tagname.setEnabled(False)
        self.cb_IDX_tagname.setGeometry(QtCore.QRect(220, 30, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.cb_IDX_tagname.setFont(font)
        self.cb_IDX_tagname.setEditable(True)
        self.cb_IDX_tagname.setObjectName("cb_IDX_tagname")
        self.cb_IDX_tagname.addItem("")
        self.tb_IDX_show = QtWidgets.QTableWidget(self.tab)
        self.tb_IDX_show.setGeometry(QtCore.QRect(0, 90, 231, 521))
        self.tb_IDX_show.setColumnCount(0)
        self.tb_IDX_show.setObjectName("tb_IDX_show")
        self.tb_IDX_show.setRowCount(0)
        self.tb_IDX_show.horizontalHeader().setDefaultSectionSize(85)
        self.wg_IDX_chart = QtWidgets.QWidget(self.tab)
        self.wg_IDX_chart.setGeometry(QtCore.QRect(240, 150, 471, 311))
        self.wg_IDX_chart.setObjectName("wg_IDX_chart")
        self.cb_Porter = QtWidgets.QCheckBox(self.tab)
        self.cb_Porter.setGeometry(QtCore.QRect(240, 120, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.cb_Porter.setFont(font)
        self.cb_Porter.setObjectName("cb_Porter")
        self.cb_CC = QtWidgets.QCheckBox(self.tab)
        self.cb_CC.setGeometry(QtCore.QRect(240, 90, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.cb_CC.setFont(font)
        self.cb_CC.setObjectName("cb_CC")
        self.cb_IDX_doLog10 = QtWidgets.QCheckBox(self.tab)
        self.cb_IDX_doLog10.setGeometry(QtCore.QRect(430, 120, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.cb_IDX_doLog10.setFont(font)
        self.cb_IDX_doLog10.setObjectName("cb_IDX_doLog10")
        self.HS_IDX_swrate = QtWidgets.QSlider(self.tab)
        self.HS_IDX_swrate.setEnabled(True)
        self.HS_IDX_swrate.setGeometry(QtCore.QRect(240, 510, 461, 22))
        self.HS_IDX_swrate.setMinimum(0)
        self.HS_IDX_swrate.setMaximum(100)
        self.HS_IDX_swrate.setProperty("value", 0)
        self.HS_IDX_swrate.setOrientation(QtCore.Qt.Horizontal)
        self.HS_IDX_swrate.setObjectName("HS_IDX_swrate")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(240, 470, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(240, 490, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(680, 490, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txt_IDX_swrate = QtWidgets.QLineEdit(self.tab)
        self.txt_IDX_swrate.setEnabled(False)
        self.txt_IDX_swrate.setGeometry(QtCore.QRect(320, 470, 41, 20))
        self.txt_IDX_swrate.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_IDX_swrate.setObjectName("txt_IDX_swrate")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(240, 553, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txt_IDX_ifrate = QtWidgets.QLineEdit(self.tab)
        self.txt_IDX_ifrate.setEnabled(False)
        self.txt_IDX_ifrate.setGeometry(QtCore.QRect(320, 530, 41, 20))
        self.txt_IDX_ifrate.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_IDX_ifrate.setObjectName("txt_IDX_ifrate")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(240, 533, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(680, 553, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.HS_IDX_ifrate = QtWidgets.QSlider(self.tab)
        self.HS_IDX_ifrate.setEnabled(True)
        self.HS_IDX_ifrate.setGeometry(QtCore.QRect(240, 573, 461, 22))
        self.HS_IDX_ifrate.setMinimum(0)
        self.HS_IDX_ifrate.setMaximum(100)
        self.HS_IDX_ifrate.setProperty("value", 0)
        self.HS_IDX_ifrate.setOrientation(QtCore.Qt.Horizontal)
        self.HS_IDX_ifrate.setObjectName("HS_IDX_ifrate")
        self.cb_IDX_doLn = QtWidgets.QCheckBox(self.tab)
        self.cb_IDX_doLn.setGeometry(QtCore.QRect(430, 90, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.cb_IDX_doLn.setFont(font)
        self.cb_IDX_doLn.setObjectName("cb_IDX_doLn")
        self.cb_IDX_editDis = QtWidgets.QCheckBox(self.tab)
        self.cb_IDX_editDis.setEnabled(False)
        self.cb_IDX_editDis.setGeometry(QtCore.QRect(500, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.cb_IDX_editDis.setFont(font)
        self.cb_IDX_editDis.setObjectName("cb_IDX_editDis")
        self.btn_IDX_PorterNote = QtWidgets.QPushButton(self.tab)
        self.btn_IDX_PorterNote.setEnabled(False)
        self.btn_IDX_PorterNote.setGeometry(QtCore.QRect(400, 120, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.btn_IDX_PorterNote.setFont(font)
        self.btn_IDX_PorterNote.setObjectName("btn_IDX_PorterNote")
        self.cb_IDX_sppkg = QtWidgets.QCheckBox(self.tab)
        self.cb_IDX_sppkg.setGeometry(QtCore.QRect(500, 90, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.cb_IDX_sppkg.setFont(font)
        self.cb_IDX_sppkg.setObjectName("cb_IDX_sppkg")
        self.btn_IDX_Indexing = QtWidgets.QPushButton(self.tab)
        self.btn_IDX_Indexing.setEnabled(False)
        self.btn_IDX_Indexing.setGeometry(QtCore.QRect(670, 80, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.btn_IDX_Indexing.setFont(font)
        self.btn_IDX_Indexing.setObjectName("btn_IDX_Indexing")
        self.btn_IDX_test = QtWidgets.QPushButton(self.tab)
        self.btn_IDX_test.setEnabled(True)
        self.btn_IDX_test.setGeometry(QtCore.QRect(670, 120, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.btn_IDX_test.setFont(font)
        self.btn_IDX_test.setText("")
        self.btn_IDX_test.setObjectName("btn_IDX_test")
        self.tabIRsys.addTab(self.tab, "")
        self.tab_hw3 = QtWidgets.QWidget()
        self.tab_hw3.setObjectName("tab_hw3")
        self.txt_HW3_model = QtWidgets.QLineEdit(self.tab_hw3)
        self.txt_HW3_model.setGeometry(QtCore.QRect(80, 2, 721, 20))
        self.txt_HW3_model.setObjectName("txt_HW3_model")
        self.btn_HW3_GetModel = QtWidgets.QPushButton(self.tab_hw3)
        self.btn_HW3_GetModel.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.btn_HW3_GetModel.setObjectName("btn_HW3_GetModel")
        self.tb_HW3_w2v = QtWidgets.QTableWidget(self.tab_hw3)
        self.tb_HW3_w2v.setGeometry(QtCore.QRect(420, 30, 381, 161))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tb_HW3_w2v.setFont(font)
        self.tb_HW3_w2v.setColumnCount(0)
        self.tb_HW3_w2v.setObjectName("tb_HW3_w2v")
        self.tb_HW3_w2v.setRowCount(0)
        self.tb_HW3_w2v.horizontalHeader().setDefaultSectionSize(85)
        self.txt_HW3_quarytxt = QtWidgets.QLineEdit(self.tab_hw3)
        self.txt_HW3_quarytxt.setEnabled(False)
        self.txt_HW3_quarytxt.setGeometry(QtCore.QRect(150, 110, 221, 31))
        self.txt_HW3_quarytxt.setObjectName("txt_HW3_quarytxt")
        self.label_15 = QtWidgets.QLabel(self.tab_hw3)
        self.label_15.setGeometry(QtCore.QRect(80, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.txt_HW3_qNear = QtWidgets.QLineEdit(self.tab_hw3)
        self.txt_HW3_qNear.setGeometry(QtCore.QRect(150, 70, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_HW3_qNear.setFont(font)
        self.txt_HW3_qNear.setObjectName("txt_HW3_qNear")
        self.txt_HW3_result = QtWidgets.QTextEdit(self.tab_hw3)
        self.txt_HW3_result.setGeometry(QtCore.QRect(80, 200, 721, 631))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_HW3_result.setFont(font)
        self.txt_HW3_result.setObjectName("txt_HW3_result")
        self.label_16 = QtWidgets.QLabel(self.tab_hw3)
        self.label_16.setGeometry(QtCore.QRect(80, 180, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.cb_HW3_quarytxt = QtWidgets.QComboBox(self.tab_hw3)
        self.cb_HW3_quarytxt.setGeometry(QtCore.QRect(150, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_HW3_quarytxt.setFont(font)
        self.cb_HW3_quarytxt.setObjectName("cb_HW3_quarytxt")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_hw3)
        self.groupBox_2.setGeometry(QtCore.QRect(80, 140, 331, 41))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rto_Paras = QtWidgets.QRadioButton(self.groupBox_2)
        self.rto_Paras.setGeometry(QtCore.QRect(70, 14, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rto_Paras.setFont(font)
        self.rto_Paras.setChecked(True)
        self.rto_Paras.setObjectName("rto_Paras")
        self.rto_Sents = QtWidgets.QRadioButton(self.groupBox_2)
        self.rto_Sents.setGeometry(QtCore.QRect(200, 13, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rto_Sents.setFont(font)
        self.rto_Sents.setObjectName("rto_Sents")
        self.tabIRsys.addTab(self.tab_hw3, "")
        self.tab_HW3_add = QtWidgets.QWidget()
        self.tab_HW3_add.setObjectName("tab_HW3_add")
        self.btn_HW3_add_GetModel = QtWidgets.QPushButton(self.tab_HW3_add)
        self.btn_HW3_add_GetModel.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.btn_HW3_add_GetModel.setObjectName("btn_HW3_add_GetModel")
        self.btn_HW3_cauTF = QtWidgets.QPushButton(self.tab_HW3_add)
        self.btn_HW3_cauTF.setGeometry(QtCore.QRect(0, 30, 75, 23))
        self.btn_HW3_cauTF.setObjectName("btn_HW3_cauTF")
        self.btn_HW3_cauIDF = QtWidgets.QPushButton(self.tab_HW3_add)
        self.btn_HW3_cauIDF.setGeometry(QtCore.QRect(0, 60, 75, 23))
        self.btn_HW3_cauIDF.setObjectName("btn_HW3_cauIDF")
        self.btn_HW3_TrainModel = QtWidgets.QPushButton(self.tab_HW3_add)
        self.btn_HW3_TrainModel.setGeometry(QtCore.QRect(0, 90, 75, 23))
        self.btn_HW3_TrainModel.setObjectName("btn_HW3_TrainModel")
        self.tabIRsys.addTab(self.tab_HW3_add, "")
        self.tab_final = QtWidgets.QWidget()
        self.tab_final.setObjectName("tab_final")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_final)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 10, 171, 241))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.rbtn_rash = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_rash.setGeometry(QtCore.QRect(10, 15, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.rbtn_rash.setFont(font)
        self.rbtn_rash.setChecked(True)
        self.rbtn_rash.setObjectName("rbtn_rash")
        self.rbtn_skin = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_skin.setGeometry(QtCore.QRect(10, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.rbtn_skin.setFont(font)
        self.rbtn_skin.setObjectName("rbtn_skin")
        self.rbtn_urticaria = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_urticaria.setGeometry(QtCore.QRect(10, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.rbtn_urticaria.setFont(font)
        self.rbtn_urticaria.setObjectName("rbtn_urticaria")
        self.rbtn_face = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_face.setGeometry(QtCore.QRect(10, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.rbtn_face.setFont(font)
        self.rbtn_face.setObjectName("rbtn_face")
        self.rbtn_maculopapular = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_maculopapular.setGeometry(QtCore.QRect(10, 110, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.rbtn_maculopapular.setFont(font)
        self.rbtn_maculopapular.setObjectName("rbtn_maculopapular")
        self.rbtn_organization = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_organization.setGeometry(QtCore.QRect(10, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.rbtn_organization.setFont(font)
        self.rbtn_organization.setObjectName("rbtn_organization")
        self.rbtn_zoster = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_zoster.setGeometry(QtCore.QRect(10, 170, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.rbtn_zoster.setFont(font)
        self.rbtn_zoster.setObjectName("rbtn_zoster")
        self.rbtn_erythema = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtn_erythema.setGeometry(QtCore.QRect(10, 200, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.rbtn_erythema.setFont(font)
        self.rbtn_erythema.setObjectName("rbtn_erythema")
        self.tb_article_rank = QtWidgets.QTableWidget(self.tab_final)
        self.tb_article_rank.setGeometry(QtCore.QRect(180, 30, 621, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_article_rank.sizePolicy().hasHeightForWidth())
        self.tb_article_rank.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.tb_article_rank.setFont(font)
        self.tb_article_rank.setAutoFillBackground(True)
        self.tb_article_rank.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_article_rank.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_article_rank.setShowGrid(True)
        self.tb_article_rank.setWordWrap(True)
        self.tb_article_rank.setCornerButtonEnabled(True)
        self.tb_article_rank.setRowCount(6)
        self.tb_article_rank.setColumnCount(2)
        self.tb_article_rank.setObjectName("tb_article_rank")
        self.tb_article_rank.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_article_rank.horizontalHeader().setDefaultSectionSize(200)
        self.tb_article_rank.horizontalHeader().setMinimumSectionSize(10)
        self.tb_article_rank.verticalHeader().setDefaultSectionSize(45)
        self.tb_article_rank.verticalHeader().setSortIndicatorShown(False)
        self.txt_fin_articleDetail = QtWidgets.QTextEdit(self.tab_final)
        self.txt_fin_articleDetail.setGeometry(QtCore.QRect(10, 410, 791, 411))
        self.txt_fin_articleDetail.setObjectName("txt_fin_articleDetail")
        self.label_17 = QtWidgets.QLabel(self.tab_final)
        self.label_17.setGeometry(QtCore.QRect(180, 10, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.btn_fin_test = QtWidgets.QPushButton(self.tab_final)
        self.btn_fin_test.setGeometry(QtCore.QRect(727, 383, 75, 23))
        self.btn_fin_test.setObjectName("btn_fin_test")
        self.btn_fin_subjectQ = QtWidgets.QPushButton(self.tab_final)
        self.btn_fin_subjectQ.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.btn_fin_subjectQ.setCheckable(False)
        self.btn_fin_subjectQ.setChecked(False)
        self.btn_fin_subjectQ.setObjectName("btn_fin_subjectQ")
        self.tabIRsys.addTab(self.tab_final, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabIRsys.setCurrentIndex(5)
        self.cb_IDX_tagname.setCurrentIndex(0)
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
        self.btn_HW2_Root.setText(_translate("MainWindow", "Get Root..."))
        self.lineEdit.setText(_translate("MainWindow", "1"))
        self.label_8.setText(_translate("MainWindow", "Tagname :"))
        self.txt_IDX_tagname.setText(_translate("MainWindow", "title"))
        self.cb_IDX_tagname.setCurrentText(_translate("MainWindow", "null"))
        self.cb_IDX_tagname.setItemText(0, _translate("MainWindow", "null"))
        self.cb_Porter.setText(_translate("MainWindow", "Porter Stemmer Algorithm"))
        self.cb_CC.setText(_translate("MainWindow", "Compare Curve"))
        self.cb_IDX_doLog10.setText(_translate("MainWindow", "Log10"))
        self.label_9.setText(_translate("MainWindow", "Stopword"))
        self.label_10.setText(_translate("MainWindow", "0%"))
        self.label_11.setText(_translate("MainWindow", "100%"))
        self.txt_IDX_swrate.setText(_translate("MainWindow", "0%"))
        self.label_12.setText(_translate("MainWindow", "0%"))
        self.txt_IDX_ifrate.setText(_translate("MainWindow", "0%"))
        self.label_13.setText(_translate("MainWindow", "Infrequently"))
        self.label_14.setText(_translate("MainWindow", "100%"))
        self.cb_IDX_doLn.setText(_translate("MainWindow", "Ln"))
        self.cb_IDX_editDis.setText(_translate("MainWindow", "Edit Distance"))
        self.btn_IDX_PorterNote.setText(_translate("MainWindow", "?"))
        self.cb_IDX_sppkg.setText(_translate("MainWindow", "Stop-Word PKG"))
        self.btn_IDX_Indexing.setText(_translate("MainWindow", "IDX"))
        self.tabIRsys.setTabText(self.tabIRsys.indexOf(self.tab), _translate("MainWindow", "HW2"))
        self.btn_HW3_GetModel.setText(_translate("MainWindow", "Get Model"))
        self.label_15.setText(_translate("MainWindow", "Quary Text"))
        self.label_16.setText(_translate("MainWindow", "Content Sentences"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Rank"))
        self.rto_Paras.setText(_translate("MainWindow", "Paragraph tf-idf"))
        self.rto_Sents.setText(_translate("MainWindow", "Sentences tf-idf"))
        self.tabIRsys.setTabText(self.tabIRsys.indexOf(self.tab_hw3), _translate("MainWindow", "HW3"))
        self.btn_HW3_add_GetModel.setText(_translate("MainWindow", "Get Model"))
        self.btn_HW3_cauTF.setText(_translate("MainWindow", "Get TF"))
        self.btn_HW3_cauIDF.setText(_translate("MainWindow", "Get IDF"))
        self.btn_HW3_TrainModel.setText(_translate("MainWindow", "Train Model"))
        self.tabIRsys.setTabText(self.tabIRsys.indexOf(self.tab_HW3_add), _translate("MainWindow", "HW3-Add"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Subject-X"))
        self.rbtn_rash.setText(_translate("MainWindow", "Rash"))
        self.rbtn_skin.setText(_translate("MainWindow", "Skin"))
        self.rbtn_urticaria.setText(_translate("MainWindow", "Urticaria"))
        self.rbtn_face.setText(_translate("MainWindow", "Face"))
        self.rbtn_maculopapular.setText(_translate("MainWindow", "Maculopapular"))
        self.rbtn_organization.setText(_translate("MainWindow", "Organization"))
        self.rbtn_zoster.setText(_translate("MainWindow", "Zoster"))
        self.rbtn_erythema.setText(_translate("MainWindow", "Erythema"))
        self.tb_article_rank.setSortingEnabled(True)
        self.label_17.setText(_translate("MainWindow", "Article Ranking"))
        self.btn_fin_test.setText(_translate("MainWindow", "Test Button"))
        self.btn_fin_subjectQ.setText(_translate("MainWindow", "Query"))
        self.tabIRsys.setTabText(self.tabIRsys.indexOf(self.tab_final), _translate("MainWindow", "FinalProject"))
