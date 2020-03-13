import sys
from PyQt5.QtWidgets import *  
from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtNetwork import *
from auth_url import auth_request_url

"""class deconst_url(url):
    pass"""
    

class WebPage(QWebPage):
    def userAgentForUrl(self, url):
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
class Authorize(QWebView):

    def __init__(self):
        
        self.view = QWebView.__init__(self)
        self.setWindowTitle("Auth")
        self.resize(600,400)
        self.setPage(WebPage())
        self.s1 = QScrollBar()
        self.s1.setDisabled(True)
       
    def load(self,url):
        
        self.setUrl(QUrl(url))
        

    def user_auth(self, url):
        self.showNormal()
        print("imworking")
        self.urlChanged.connect(self.get_code)
        
# NEEDS MORE TESTING / DEBUGING
    def get_code(self, url):
        if authurl != url:
            e = QUrlQuery(url)
            value = e.queryItemValue("code")
            print(value)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(300,300)
    w.setWindowTitle("igm")
    w.show()
    
    authurl = auth_request_url()




    auth = Authorize()
    auth.load(authurl)

    auth_button = QPushButton(w)
    auth_button.setText("Login through here")
    auth_button.move(80,150)
    auth_button.show()
    auth_button.clicked.connect(auth.user_auth)
        
        

    sys.exit(app.exec_())