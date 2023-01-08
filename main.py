import sys
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QSystemTrayIcon, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from modules.interface import SignIn, SignUp
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtCore import pyqtSignal, pyqtSlot

app = QApplication(sys.argv)
trayIcon = QSystemTrayIcon(QIcon('newdawn.png'), parent=app)
trayIcon.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.setStyleSheet("background-color: rgb(8, 29, 55)")
        self.setWindowTitle('New Dawn')
        self.networkmanager = QNetworkAccessManager()
        #self.setCentralWidget(SignIn(self))
        self.goSignIn()
        self.show()

    @pyqtSlot()
    def goSignIn(self):
        widget = SignIn(self)
        self.setCentralWidget(widget)

    @pyqtSlot()
    def goSignUp(self):
        widget = SignUp(self)
        self.setCentralWidget(widget)

    @pyqtSlot()
    def goConversation(self):
        widget = ConversationWindow(self)
        self.setCentralWidget(widget)

#NetworkAccessManager = QNetworkAccessManager()
#mainwindow = SignIn(NetworkAccessManager)
mainWindow = MainWindow()
app.setWindowIcon(QIcon('newdawn.png'))
widget = QtWidgets.QWidget()
#mainWindow.showMaximized()
#mainWindow.setWindowTitle('New Dawn')
#mainWindow.setCentralWidget(SignIn(NetworkAccessManager))

#mainwindow.setWidget(widget)
sys.exit(app.exec_())
