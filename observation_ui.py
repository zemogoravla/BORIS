# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'observation.ui'
#
# Created: Wed Apr 16 14:59:05 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(574, 714)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.leObservationId = QtGui.QLineEdit(Form)
        self.leObservationId.setObjectName("leObservationId")
        self.horizontalLayout_2.addWidget(self.leObservationId)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.dteDate = QtGui.QDateTimeEdit(Form)
        self.dteDate.setCalendarPopup(True)
        self.dteDate.setObjectName("dteDate")
        self.horizontalLayout_3.addWidget(self.dteDate)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.teDescription = QtGui.QPlainTextEdit(Form)
        self.teDescription.setMaximumSize(QtCore.QSize(16777215, 50))
        self.teDescription.setObjectName("teDescription")
        self.verticalLayout_2.addWidget(self.teDescription)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.twIndepVariables = QtGui.QTableWidget(Form)
        self.twIndepVariables.setObjectName("twIndepVariables")
        self.twIndepVariables.setColumnCount(3)
        self.twIndepVariables.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(2, item)
        self.verticalLayout_3.addWidget(self.twIndepVariables)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbTimeOffset = QtGui.QLabel(Form)
        self.lbTimeOffset.setObjectName("lbTimeOffset")
        self.horizontalLayout_6.addWidget(self.lbTimeOffset)
        self.leTimeOffset = QtGui.QLineEdit(Form)
        self.leTimeOffset.setObjectName("leTimeOffset")
        self.horizontalLayout_6.addWidget(self.leTimeOffset)
        self.teTimeOffset = QtGui.QTimeEdit(Form)
        self.teTimeOffset.setObjectName("teTimeOffset")
        self.horizontalLayout_6.addWidget(self.teTimeOffset)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabProjectType = QtGui.QTabWidget(Form)
        self.tabProjectType.setEnabled(True)
        self.tabProjectType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabProjectType.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabProjectType.setUsesScrollButtons(False)
        self.tabProjectType.setDocumentMode(False)
        self.tabProjectType.setTabsClosable(False)
        self.tabProjectType.setMovable(False)
        self.tabProjectType.setObjectName("tabProjectType")
        self.tabVideo = QtGui.QWidget()
        self.tabVideo.setObjectName("tabVideo")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabVideo)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.rbVLC = QtGui.QRadioButton(self.tabVideo)
        self.rbVLC.setEnabled(False)
        self.rbVLC.setChecked(True)
        self.rbVLC.setObjectName("rbVLC")
        self.verticalLayout_7.addWidget(self.rbVLC)
        self.rbOpenCV = QtGui.QRadioButton(self.tabVideo)
        self.rbOpenCV.setEnabled(False)
        self.rbOpenCV.setObjectName("rbOpenCV")
        self.verticalLayout_7.addWidget(self.rbOpenCV)
        self.label_5 = QtGui.QLabel(self.tabVideo)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lwVideo = QtGui.QListWidget(self.tabVideo)
        self.lwVideo.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lwVideo.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lwVideo.setObjectName("lwVideo")
        self.horizontalLayout_4.addWidget(self.lwVideo)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbAddVideo = QtGui.QPushButton(self.tabVideo)
        self.pbAddVideo.setObjectName("pbAddVideo")
        self.verticalLayout.addWidget(self.pbAddVideo)
        self.pbRemoveVideo = QtGui.QPushButton(self.tabVideo)
        self.pbRemoveVideo.setObjectName("pbRemoveVideo")
        self.verticalLayout.addWidget(self.pbRemoveVideo)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.label_2 = QtGui.QLabel(self.tabVideo)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lwVideo_2 = QtGui.QListWidget(self.tabVideo)
        self.lwVideo_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lwVideo_2.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lwVideo_2.setObjectName("lwVideo_2")
        self.horizontalLayout_5.addWidget(self.lwVideo_2)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pbAddVideo_2 = QtGui.QPushButton(self.tabVideo)
        self.pbAddVideo_2.setObjectName("pbAddVideo_2")
        self.verticalLayout_6.addWidget(self.pbAddVideo_2)
        self.pbRemoveVideo_2 = QtGui.QPushButton(self.tabVideo)
        self.pbRemoveVideo_2.setObjectName("pbRemoveVideo_2")
        self.verticalLayout_6.addWidget(self.pbRemoveVideo_2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.tabProjectType.addTab(self.tabVideo, "")
        self.tabLive = QtGui.QWidget()
        self.tabLive.setObjectName("tabLive")
        self.tabProjectType.addTab(self.tabLive, "")
        self.verticalLayout_9.addWidget(self.tabProjectType)
        self.verticalLayout_3.addLayout(self.verticalLayout_9)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pbCancel = QtGui.QPushButton(Form)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout.addWidget(self.pbCancel)
        self.pbOK = QtGui.QPushButton(Form)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout.addWidget(self.pbOK)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.tabProjectType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "New observation", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Observation id", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.dteDate.setDisplayFormat(QtGui.QApplication.translate("Form", "yyyy-MM-dd hh:mm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Independent variables", None, QtGui.QApplication.UnicodeUTF8))
        self.twIndepVariables.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.twIndepVariables.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.twIndepVariables.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.lbTimeOffset.setText(QtGui.QApplication.translate("Form", "Time offset", None, QtGui.QApplication.UnicodeUTF8))
        self.leTimeOffset.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.teTimeOffset.setDisplayFormat(QtGui.QApplication.translate("Form", "hh:mm:ss.zzz", None, QtGui.QApplication.UnicodeUTF8))
        self.rbVLC.setText(QtGui.QApplication.translate("Form", "VLC media player", None, QtGui.QApplication.UnicodeUTF8))
        self.rbOpenCV.setText(QtGui.QApplication.translate("Form", "OpenCV", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Media file names", None, QtGui.QApplication.UnicodeUTF8))
        self.pbAddVideo.setText(QtGui.QApplication.translate("Form", "Add media", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRemoveVideo.setText(QtGui.QApplication.translate("Form", "Remove media", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Media file names for second player (will be played simultaneously)", None, QtGui.QApplication.UnicodeUTF8))
        self.pbAddVideo_2.setText(QtGui.QApplication.translate("Form", "Add media", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRemoveVideo_2.setText(QtGui.QApplication.translate("Form", "Remove media", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProjectType.setTabText(self.tabProjectType.indexOf(self.tabVideo), QtGui.QApplication.translate("Form", "Media", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProjectType.setTabText(self.tabProjectType.indexOf(self.tabLive), QtGui.QApplication.translate("Form", "Live", None, QtGui.QApplication.UnicodeUTF8))
        self.pbCancel.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbOK.setText(QtGui.QApplication.translate("Form", "OK", None, QtGui.QApplication.UnicodeUTF8))

