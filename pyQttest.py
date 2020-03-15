import sys
from PyQt5.QtWidgets import *  
from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtNetwork import *
from auth_url import auth



class WebPage(QWebPage):
    def userAgentForUrl(self, url):
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
class Authorize(QWebView):
    auth_code = ""
    def __init__(self):
        
        self.view = QWebView.__init__(self)
        self.setWindowTitle("Authorization")
        self.resize(600,600)
        self.setPage(WebPage())
        self.s1 = QScrollBar()
        self.s1.setDisabled(True)
       
    def load(self,url):
        
        self.setUrl(QUrl(url))


    def user_auth(self, url):
        self.showNormal()
        print("imworking")
        auth.load(authurl)
        self.urlChanged.connect(self.get_code)

    def get_token():
        token = auth.auth_request_code()
        return token


    def get_code(self, url):
        if authurl != url:
            e = QUrlQuery(url)
            value = e.queryItemValue("code")
            print("Code: " +value)
            print(url)

            # RECEIVE auth_code as value, need to send it to auth_url.py 

            if value:
                auth_code = value
                w.insertCode(value)
                self.close()
                
class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.resize(400,400)
        self.setWindowTitle("ChPTTS")
       
        self.login_b = QPushButton(self)
        self.login_b.setText("Login through here")
        self.login_b.move(10,10)
        self.login_b.show()
 
        self.code_box = QLineEdit(self)
        self.code_box.setReadOnly(True)
        self.code_box.setPlaceholderText("Auth_code")
        self.code_box.move(10,50)
        self.code_box.resize(250,30)

        
        self.show()
    
    def insertCode(self, var):
        self.code_box.setText(var)
        self.code_box.setAlignment(Qt.AlignCenter)

    def getCode(self):
        return self.code_box.text()
       
       
       
       
       
        
if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = UI()
    authurl = auth.auth_request_url()
    auth = Authorize()
    
    w.login_b.clicked.connect(auth.user_auth)
    sys.exit(app.exec_())
  