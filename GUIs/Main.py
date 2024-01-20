import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog,QMainWindow

import sys,resources

from Post_deal import Ui_MainWindow1

class MainWindow1(QMainWindow,Ui_MainWindow1):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.browsefiles)

        connection=sqlite3.connect('Postdeal.db')


    def browsefiles(self):
        fname= QFileDialog.getOpenFileName(self,'Open File','D:\codefirst.io','PNG FILES(*.png)')
        self.lineEdit_4.setText(fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow1()
    main_window.show()
    sys.exit(app.exec_())
