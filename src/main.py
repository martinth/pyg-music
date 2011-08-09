# -*- coding: utf-8 -*-
'''
.. module:: main
   :synopsis: main dialog controller

.. moduleauthor:: "Martin Thurau <martin.thurau@gmail.com>"
'''
import cookie

from PyQt4 import QtGui
from PyQt4.QtCore import QObject, SIGNAL, QUrl, QTimer, pyqtSlot, QString
from gui.window import Ui_Dialog


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MainDialog(QtGui.QDialog):
    
    WINDOW_TITLE = "Google Music"
    UPDATE_TIMEOUT = 1000
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # load cookies and setup webview
        self.cookie_jar = cookie.load_cookies()
        self.ui.webView.page().networkAccessManager().setCookieJar(self.cookie_jar)
        self.ui.webView.loadFinished.connect(self.load_finished)
        
        # connect buttons
        self.ui.nextTrack.clicked.connect(lambda: self._doCommand("nextSong"))
        self.ui.previousTrack.clicked.connect(lambda: self._doCommand("prevSong"))
        self.ui.playPause.clicked.connect(lambda: self._doCommand("playPause"))
        
        # this timer will update the gui
        self.update_timer = QTimer()
        QObject.connect(self.update_timer, SIGNAL("timeout()"), self._update_gui)
        
        # load the google music page
        self.ui.webView.load(QUrl("http://music.google.com"))
        
        self.finished.connect(self._dialog_close)


    
    @pyqtSlot()    
    def load_finished(self, ok=True):
        '''Slot when a page loaded completely.''' 
        url = self.ui.webView.url()
        if url.host() == "music.google.com":
            self.enable_music_controls(True)
            self.update_timer.start(self.UPDATE_TIMEOUT)
        else:
            self.enable_music_controls(False)
            self.update_timer.stop()

    @pyqtSlot()
    def _dialog_close(self):
        '''Slot for the dialog close. Saves cookies'''
        cookie.save_cookies(self.cookie_jar)        
        
    def _doCommand(self, command):
        '''excutes a command on the page and triggers an GUI update'''
        doc = self.ui.webView.page().currentFrame().documentElement()
        doc.evaluateJavaScript("location.assign('javascript:SJBpost(\"" + command + "\");void 0')")
        QTimer.singleShot(200, self._update_gui)
       
        
    @pyqtSlot()
    def _update_gui(self):
        '''Update the GUI. Set window title and buttons to state of the page'''
        doc = self.ui.webView.page().currentFrame().documentElement()
        self.ui.playPause.setText( doc.findFirst("div#playPause").attribute("title") )
                
        title = doc.findFirst("div#playerSongTitle").findFirst("div.fade-out-content").toPlainText()
        artist = doc.findFirst("div#playerArtist").findFirst("div.fade-out-content").toPlainText()
        elapsed = doc.findFirst("span#currentTime").toPlainText()
        duration = doc.findFirst("span#duration").toPlainText()
        
        if "" != title and "" != artist:
            self.setWindowTitle(_fromUtf8("%s | %s - %s (%s / %s)" % (self.WINDOW_TITLE, artist, title, elapsed, duration)))
        else:
            self.setWindowTitle(self.WINDOW_TITLE)
            
      
    def enable_music_controls(self, enabled):
        '''enable the music controls'''
        self.ui.previousTrack.setEnabled(enabled)
        self.ui.nextTrack.setEnabled(enabled)
        self.ui.playPause.setEnabled(enabled)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    
    dialog = MainDialog()
    dialog.exec_()
    