'''
Created on 23 janv. 2011

@author: epot
'''

import sys
from PyQt4 import QtGui
from widgets.mainwindow import MainWindow

def main():
    app = QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()