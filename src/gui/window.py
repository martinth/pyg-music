# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Tue Aug  9 22:29:09 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1100, 700)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(Dialog)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.previousTrack = QtGui.QPushButton(Dialog)
        self.previousTrack.setEnabled(False)
        self.previousTrack.setMinimumSize(QtCore.QSize(0, 40))
        self.previousTrack.setObjectName(_fromUtf8("previousTrack"))
        self.horizontalLayout.addWidget(self.previousTrack)
        self.playPause = QtGui.QPushButton(Dialog)
        self.playPause.setEnabled(False)
        self.playPause.setMinimumSize(QtCore.QSize(0, 40))
        self.playPause.setObjectName(_fromUtf8("playPause"))
        self.horizontalLayout.addWidget(self.playPause)
        self.nextTrack = QtGui.QPushButton(Dialog)
        self.nextTrack.setEnabled(False)
        self.nextTrack.setMinimumSize(QtCore.QSize(0, 40))
        self.nextTrack.setObjectName(_fromUtf8("nextTrack"))
        self.horizontalLayout.addWidget(self.nextTrack)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Google Music", None, QtGui.QApplication.UnicodeUTF8))
        self.previousTrack.setText(QtGui.QApplication.translate("Dialog", "<< Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.playPause.setText(QtGui.QApplication.translate("Dialog", "Play >", None, QtGui.QApplication.UnicodeUTF8))
        self.nextTrack.setText(QtGui.QApplication.translate("Dialog", "Next >>", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
