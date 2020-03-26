import sys
from PyQt5.QtWidgets import *  
from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtNetwork import *
from auth_url import twitch_api


# Need to figure out how to disable/hide the horizontal scroll bar
class WebPage(QWebPage):

    def mainFrame(self, QWebFrame):
        frame = QWebFrame(self)
        frame.setScrollBarPolicy(Horizontal , Qt.ScrollBarAlwaysOff)
 
    def userAgentForUrl(self, url):
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"


            # RECEIVE auth_code as value, need to send it to auth_url

class Authorize(QWebView):
    auth_code = ""
    def __init__(self):
        
        # Creating the TwitchLoginWindow
        self.view = QWebView.__init__(self)
        self.setWindowTitle("Authorization")
        self.resize(500,600)
        self.setPage(WebPage())


       
    def load(self,url):
        
        self.setUrl(QUrl(url))

    # Method that is called after  clicking "Login through here"
    def user_auth(self, url):

        self.showNormal()

        auth.load(authurl)
        self.urlChanged.connect(self.get_code)
        

    def get_token(self):
        self.token = auth.auth_request_code()
        return self.token


    def get_code(self, url):
        e = QUrlQuery(url)

            # Grab the "Code" field from the redirectUrl
        self.value = e.queryItemValue("code")
        # Check if the url changed 
        if self.value:
            
            print("Code: " + self.value)

            # RECEIVE auth_code as value, need to send it to auth_url.py 

            if self.value:

                # Sending "code" to auth_url.p
                Api.setCode(self.value)
                Api.request_token()
                Api.request_channel()

                # Create vars in Object for later use
                self.channel = Api.getChannel()
                self.tokens = Api.getTokens()
                
                # Asign the access_token and code to the UI Lines 
                w.code_box.setText(self.value)
                w.Atoken_LE.setText(self.tokens["access_token"])

                # Close the login window after authentication
                self.close()

# Main UI window
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
        
        self.Atoken_LE = QLineEdit(self)
        self.Atoken_LE.setReadOnly(True)
        self.Atoken_LE.setPlaceholderText("Acces_token")
        self.Atoken_LE.move(10,90)
        self.Atoken_LE.resize(250,30)
        
        self.show()
        

# APP EXEC
if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = UI()
    Api = twitch_api()
    authurl = Api.request_url()
    auth = Authorize()
    w.login_b.clicked.connect(auth.user_auth)
    sys.exit(app.exec_())
  