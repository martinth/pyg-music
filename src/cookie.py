# -*- coding: utf-8 -*-
'''
.. module:: cookie
   :synopsis: save and load cookies by pickle (yeah, that's lame)

.. moduleauthor:: "Martin Thurau <martin.thurau@gmail.com>"
'''
import pickle
from os.path import expanduser, join
from PyQt4.QtNetwork import QNetworkCookieJar, QNetworkCookie
from PyQt4.QtCore import QUrl

COOKIE_FILE = ".pyg-music-cookie"
COOKIE_URL = "http://music.google.com"

def homedir():
    '''return the homedir of the user'''
    try:
        from win32com.shell import shellcon, shell            
        return shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, 0, 0)
    except ImportError: # quick semi-nasty fallback for non-windows/win32com case
        return expanduser("~")
    
def save_cookies(cookie_jar):
    '''pickle the cookie jar'''
    cookies = [(c.name(), c.value()) for c in cookie_jar.cookiesForUrl(QUrl(COOKIE_URL)) ]
    with open(join(homedir(), COOKIE_FILE), "w") as file:
        pickle.dump(cookies, file)    

def load_cookies():
    '''unpickle the cookie jar'''
    jar = QNetworkCookieJar()
    try:
        with open(join(homedir(), COOKIE_FILE)) as file:           
            cookies = []
            for name, value in pickle.load(file):
                cookies.append(QNetworkCookie(name, value))
            jar.setCookiesFromUrl(cookies, QUrl(COOKIE_URL))
    except IOError:
        pass # no cookie file is okay
    return jar
    