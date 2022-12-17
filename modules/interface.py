from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QSystemTrayIcon, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from modules.database import signin_sql, signup_sql

class SignIn(QMainWindow):
    def __init__(self, NetworkAccessManager):
        super(SignIn, self).__init__()
        loadUi("SignIn.ui", self)
        #pix = QPixmap("newdawn.png", )
        #self.label.setPixmap(pix.scaled(1181, 1181,Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        self.label.resizeEvent = self.on_resize
        self.signin.clicked.connect(self.signin_function)
        self.signup.clicked.connect(self.signup_function)
        self.forgot.clicked.connect(self.forgot_function)
        self.error.setVisible(False)
        self.networkmanager = NetworkAccessManager
    def on_resize(self, e):
        size = e.size()
        if (size.width() > size.height()):
            m = (size.width() - size.height()) / 2
            self.label.setContentsMargins(m, 0, m, 0)
        else:
            m = (-size.width() + size.height()) / 2
            self.label.setContentsMargins(0, m, 0, m)
            

    def signin_function(self):
        noerror, txt = signin_sql( self.email.text(), self.password.text())
        print(noerror)
        if(noerror == True):
            signedin = ConversationWindow()
            self.widget.addWidget(signedin)
            self.widget.setCurrentIndex(self.widget.currentIndex()+1)
        else:
            self.error.setText(txt)
            self.error.setVisible(True)

    def signup_function(self):
        signUp = SignUp(self.networkmanager)
        self.widget.addWidget(signUp)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
        signUp.setWidget(self.widget)

    def setWidget(self, widget):
        self.widget = widget

    def forgot_function(self):
        pass

class SignUp(QMainWindow):
    def __init__(self, NetworkAccessManager):
        super(SignUp, self).__init__()
        loadUi("SignUp.ui", self)
        self.label.resizeEvent = self.on_resize
        self.signup.clicked.connect(self.signup_function)
        self.forgot.clicked.connect(self.forgot_function)
        self.error.setVisible(False)
        self.networkmanager = NetworkAccessManager 
    def on_resize(self, e):
        size = e.size()
        if (size.width() > size.height()):
            m = (size.width() - size.height()) / 2
            self.label.setContentsMargins(m, 0, m, 0)
        else:
            m = (-size.width() + size.height()) / 2
            self.label.setContentsMargins(0, m, 0, m)
            
    def setWidget(self, widget):
        self.widget = widget

    def signup_function(self):
        signup_sql(self.email.text(), self.username.text(), self.password.text(), self.password_conf.text(), self.networkmanager, self.signup_onerror, self.signup_onok)

    def forgot_function(self):
        signIn = SignIn()
        self.widget.addWidget(signIn)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
        signIn.setWidget(self.widget)

    def signup_onok(self):
        signIn = SignIn(self.networkmanager)
        self.widget.addWidget(signIn)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
        

    def signup_onerror(self):
        self.error.setText("OK")
        self.error.setVisible(True)

class ConversationWindow(QMainWindow):
    def __init__(self):
        super(ConversationWindow, self).__init__()
        loadUi("ConvWindow.ui", self)
        self.new_doc.clicked.connect(self.new_doc_function)

    def from_popup(self, dprivacy, dtype, dsave, dname = 'Untitled doc'):
        print(dprivacy, dtype, dsave, dname)

    def new_doc_function(self):
        popup = NewDocPopup(self)
        popup.exec()        

class NewDocPopup(QDialog):
    def __init__(self, parent = None):
        super(NewDocPopup, self).__init__()
        self.parent = parent
        loadUi("popup.ui", self)
        self.buttonBox.accepted.connect(self.okclose)
        self.buttonBox.rejected.connect(self.reject)
        
    def okclose(self):
        privacy = 0
        dtype = 0
        dsave = 0
        if self.shared_doc.isChecked():
            privacy = 1
        if self.type_doc.isChecked():
            dtype = 1
        if self.type_mind.isChecked():
            dtype = 2
        if self.save_to_loc.isChecked():
            dsave = 1
        if self.name.text():
            dname = self.name.text()
        self.parent.from_popup(privacy, dtype, dsave, dname)
        self.accept()


