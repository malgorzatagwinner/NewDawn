from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QSystemTrayIcon, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from modules.database import signin_sql, signup_sql

class SignIn(QWidget):
    def __init__(self, mainWindow):
        super(SignIn, self).__init__()
        loadUi("SignIn.ui", self)
        #self.label.setPixmap(pix.scaled(1181, 1181,Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        self.label.resizeEvent = self.on_resize
        self.signin.clicked.connect(self.signin_function)
        self.signup.clicked.connect(self.signup_function)
        self.forgot.clicked.connect(self.forgot_function)
        self.error.setVisible(False)
        self.networkmanager = mainWindow.networkmanager
        self.mainWindow = mainWindow
        self.showMaximized()
        #self.show()

    def on_resize(self, e):
        size = e.size()
        if (size.width() > size.height()):
            m = (size.width() - size.height()) / 2
            self.label.setContentsMargins(m, 0, m, 0)
        else:
            m = (-size.width() + size.height()) / 2
            self.label.setContentsMargins(0, m, 0, m)
            
    def ifsignedup(self, message, iserror):
        self.error.setText(message)
        if not iserror:
            self.error.setStyleSheet("color:rgb(255,255,255)")
        self.error.setVisible(True)

    def signup_function(self):
        self.mainWindow.goSignUp()
    
    def setWidget(self, widget):
        self.widget = widget
    
    def forgot_function(self):
        pass

    def signin_function(self):
        signin_sql(self.email.text(), self.password.text(), self.networkmanager, self.signin_onerror, self.signin_onok)

    def signin_onok(self):
        print("OK")
        self.mainWindow.goConversation()

    def signin_onerror(self, body):
        print("NIE OK")
        self.error.setText(body.data().decode('utf-8'))
        self.error.setVisible(True)

class SignUp(QWidget):
    def __init__(self, mainWindow):
        super(SignUp, self).__init__()
        loadUi("SignUp.ui", self)
        self.label.resizeEvent = self.on_resize
        self.signup.clicked.connect(self.signup_function)
        self.forgot.clicked.connect(self.forgot_function)
        self.error.setVisible(False)
        self.mainWindow = mainWindow
        self.networkmanager = mainWindow.networkmanager 
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
        self.mainWindow.goSignIn()

    def signup_onok(self):
        print("OK")
        self.mainWindow.goSignIn("Thank you for registering. You can now sign in", False)

    def signup_onerror(self, body):
        print("NIE OK")
        self.error.setText(body.data().decode('utf-8'))
        self.error.setVisible(True)

class ConversationWindow(QWidget):
    def __init__(self, mainWindow):
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


