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

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.resize(400,400)
        self.setWindowTitle("Auth")
       
        self.login_b = QPushButton(self)
        self.login_b.setText("Login through here")
        self.login_b.move(10,10)
        self.login_b.show()

        self.code_box = QInputDialog(self)
        #self.code_box.InputDialogOption(0x00000001)
        self.code_box.getText(self,"lol","input")
        self.code_box.setOptions(self.code_box.NoButtons,bool(True))
        self.code_box.move(200,200)

        
       
       
       
       
       
       
        self.show()
if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = UI()
    authurl = auth_request_url()
    auth = Authorize()
    auth.load(authurl)
    w.login_b.clicked.connect(auth.user_auth)
    sys.exit(app.exec_())