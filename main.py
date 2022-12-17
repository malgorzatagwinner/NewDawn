import sys
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QSystemTrayIcon, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from modules.interface import SignIn
from PyQt5.QtNetwork import QNetworkAccessManager

app = QApplication(sys.argv)
trayIcon = QSystemTrayIcon(QIcon('newdawn.png'), parent=app)
trayIcon.show()

NetworkAccessManager = QNetworkAccessManager()
mainwindow = SignIn(NetworkAccessManager)
app.setWindowIcon(QIcon('newdawn.png'))
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showMaximized()
widget.setWindowTitle('New_Dawn')
mainwindow.setWidget(widget)
sys.exit(app.exec_())
