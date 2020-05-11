import sys
import os
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

app = QtWidgets.QApplication(sys.argv)
view = QtWebEngineWidgets.QWebEngineView()
window = QtWidgets.QWidget()
window.setGeometry(0,0,280,400)
view.setGeometry(0,0,2000,2000)

layout = QtWidgets.QVBoxLayout(window)


#view.load(QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'C:\Users\SREERAM\Desktop\project\test.html'))
#web = QWebEngineView()
#web.load(QUrl(r"C:\Users\SREERAM\Desktop\project\test.html"))
#htmlView.setSource(QtCore.QUrl.fromLocalFile("test.html"))
#web.show()

tw = QtWidgets.QTreeWidget()
tw.setHeaderLabels(['Drone','Command'])
#tw.setGeometry(0,0,100,300)

cg = QtWidgets.QTreeWidgetItem(tw,['Drone1'])
c1 = QtWidgets.QTreeWidgetItem(cg,['', 'RTL'])
c2 = QtWidgets.QTreeWidgetItem(cg,['', 'LAND'])
ch = QtWidgets.QTreeWidgetItem(tw,['Drone2'])
c3 = QtWidgets.QTreeWidgetItem(ch,['', 'RTL'])
c4 = QtWidgets.QTreeWidgetItem(ch,['', 'LAND'])
ci = QtWidgets.QTreeWidgetItem(tw,['Drone3'])
c5 = QtWidgets.QTreeWidgetItem(ci,['', 'RTL'])
c6 = QtWidgets.QTreeWidgetItem(ci,['', 'LAND'])
fname =  os.getcwd()+ '/npntfinal.html'
url = QUrl.fromLocalFile(fname)
layout.addWidget(tw)
view.setUrl(url)
view.show()
window.show()
sys.exit(app.exec_())
