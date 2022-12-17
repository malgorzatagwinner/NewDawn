from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QByteArray, QUrl
from PyQt5.QtNetwork import QNetworkRequest, QNetworkReply
import json

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("tabelki.db")
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
slownik = []
class MySignal:
    def __init__(self, error_fun, ok_fun, reply):
        self.error_fun = error_fun
        self.ok_fun = ok_fun
        self.reply = reply
        reply.finished.connect(self.finished)
        slownik.append(self)


    def finished(self):
        print("finiszed")
        if self.reply.error() == QNetworkReply.NetworkError.NoError:
            self.ok_fun()
            
        else:
            body = self.reply.readAll()
            self.error_fun(body)
        try:
            slownik.remove(self)
        except:
            pass


def signin_sql(email, password):
    if not (email):
        return False, "Email or username was not provided!"
        
    query.prepare("SELECT COUNT(*), password FROM user WHERE email = ? OR username = ?")
    query.addBindValue(email)
    query.addBindValue(email)
    if not query.exec_():
        return query.lastError().text()
    query.first()
    row_count = query.value(0)
    passw = query.value(1)
    if not(row_count or passw):
        return False, "Incorrect entries!"
    elif(passw == password):    
        return True, ""
    else:
        return False, "Incorrect entries!"
    
def signup_sql(email, username, password, password_conf, networkmanager, signup_onerror, signup_onok):
    if not (password == password_conf):
        print("Passwords are not the same!")
        print(password)
        print(password_conf)
        return False, "Passwords are not the same!"
        print(password)
    elif not (email):
        print("Email was not provided!")
        return False, "Email was not provided!"
    elif not (username):
        print("Username was not provided!")
        return False, "Username was not provided!"
    elif not (password):
        print("Password was not provided!")
        return False, "Password was not provided!"
    """ query.prepare("SELECT COUNT(*) FROM user WHERE email = ?")
    query.addBindValue(email)
    query.exec_()
    query.first()
    row_count = query.value(0)
    query.prepare("SELECT COUNT(*) FROM user WHERE username = ?")
    query.addBindValue(username)
    query.exec_()
    query.first()
    second_row_count = query.value(0)
    if not(row_count == 0):
        print("An account with such email already exists!")
        return False, "An account with such email already exists!"
    elif not(second_row_count == 0):
        print("An account with such username already exists!")
        return False, "An account with such username already exists!"
    else:
        query.prepare("INSERT INTO user (email, username, password) VALUES(?, ?, ?)")
        query.addBindValue(email)
        query.addBindValue(username)
        query.addBindValue(password)
        if not query.exec_():
            print(query.lastError().text())
"""
    data = {}
    for info in ["email", "username", "password", "password_conf"]:
        data[info] = eval(info)
    data = json.dumps(data)
    print(data)
    request = QNetworkRequest(QUrl("http://127.0.0.1:8000/app/signup/"))
    request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
    reply = networkmanager.post(request, QByteArray(data.encode()))
    mySignal = MySignal(signup_onerror, signup_onok, reply)
