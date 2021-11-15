import sys
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QSystemTrayIcon, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

class SignIn(QMainWindow):
    def __init__(self):
        super(SignIn, self).__init__()
        loadUi("SignIn.ui", self)
        self.signin.clicked.connect(self.signin_function)
        self.signup.clicked.connect(self.signup_function)
        self.forgot.clicked.connect(self.forgot_function)

    def signin_function(self):
        if not (self.email.text()):
            print("Email or username was not provided!")
        query.prepare("SELECT COUNT(*), password FROM user WHERE email = ? OR username = ?")
        query.addBindValue(self.email.text())
        query.addBindValue(self.email.text())
        if not query.exec_():
            print(query.lastError().text())
        query.first()
        row_count = query.value(0)
        password = query.value(1)
        if not(row_count or password):
            print("Incorrect entries!")
        elif(password == self.password.text()):    
            signedin = ConversationWindow()
            widget.addWidget(signedin)
            widget.setCurrentIndex(widget.currentIndex()+1)
    
        #pass

    def signup_function(self):
        signUp = SignUp()
        widget.addWidget(signUp)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def forgot_function(self):
        pass


class SignUp(QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("SignUp.ui", self)
        self.signup.clicked.connect(self.signup_function)
        self.forgot.clicked.connect(self.forgot_function)

    def signup_function(self):
        if not (self.password.text() == self.password_conf.text()):
            print("Passwords are not the same!")
            print(self.password.text())
            print(self.password_conf.text())
            return
        elif not (self.email.text()):
            print("Email was not provided!")
            return
        query.prepare("SELECT COUNT(*) FROM user WHERE email = ?")
        query.addBindValue(self.email.text())
        query.exec_()
        query.first()
        row_count = query.value(0)
        query.prepare("SELECT COUNT(*) FROM user WHERE username = ?")
        query.addBindValue(self.username.text())
        query.exec_()
        query.first()
        second_row_count = query.value(0)
        if not(row_count == 0):
            print("An account with such email already exists!")
        elif not(second_row_count == 0):
            print("An account with such username already exists!")
        else:
            query.prepare("INSERT INTO user (email, username, password) VALUES(?, ?, ?)")
            query.addBindValue(self.email.text())
            query.addBindValue(self.username.text())
            query.addBindValue(self.password.text())
            if not query.exec_():
                print(query.lastError().text())
            signIn = SignIn()
            widget.addWidget(signIn)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def forgot_function(self):
        signIn = SignIn()
        widget.addWidget(signIn)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ConversationWindow(QMainWindow):
    def __init__(self):
        super(ConversationWindow, self).__init__()
        loadUi("ConvWindow.ui", self)
        self.new_doc.clicked.connect(self.new_doc_function)

    def from_popup(self, dprivacy, dtype, dsave):
        print(dprivacy, dtype, dsave)

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
        if self.save_to_loc.isChecked():
            dsave = 1
        self.parent.from_popup(privacy, dtype, dsave)
        self.accept()

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("tabelki.db")
app = QApplication(sys.argv)
trayIcon = QSystemTrayIcon(QIcon('newdawn.png'), parent=app)
trayIcon.show()
if not con.open():
    print("Unable to connect to the database")
    sys.exit(1)

query = QSqlQuery()
sql = ""
f = open("tabelki.sql", "r")
for x in f:
    sql += x
    if ";" in x:
        if not query.exec(sql):
            print(query.lastError().text())
            print(sql)
        sql = ""
f.close()
mainwindow = SignIn()
app.setWindowIcon(QIcon('newdawn.png'))
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showMaximized()
widget.setWindowTitle('New_Dawn')
sys.exit(app.exec_())
