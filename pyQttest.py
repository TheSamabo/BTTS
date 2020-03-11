import sys
from PyQt5.QtWidgets import *  
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView , QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
from auth_url import auth_request_url

class Authorize(QWebView):
    def __init__(self):
        self.view = QWebView.__init__(self)
        self.setWindowTitle("Auth")
        self.resize(600,400)
    def load(self,url):
        self.setUrl(QUrl(url))


    def user_auth(self):
        self.showNormal()
        print("imworking")



if __name__ == "__main__":
 
    
    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(300,300)
    w.setWindowTitle("igm")
    w.show()

    label = QLabel(w)
    label.setText("Ligma")
    label.show()

    
    authurl = auth_request_url()


    auth = Authorize()
    auth.load(authurl)

    auth_button = QPushButton(w)
    auth_button.setText("Login through here")
    auth_button.move(80,150)
    auth_button.show()
    auth_button.clicked.connect(auth.user_auth)
        
        

    sys.exit(app.exec_())