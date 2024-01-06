import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys,resources

from dealalerts import Ui_Dialog
from Home import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):




    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.DealAlert.clicked.connect(self.open_dialog)

    def open_dialog(self):
        dialog = QDialog()
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
