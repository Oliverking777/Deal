import sys
from PyQt5.QtWidgets import QApplication, QDialog
from Post_deal import Ui_Dialog1


class Ui_Dialog1(QDialog):
    def __init__(self):
        super().__init__()

        # Create an instance of the generated QDialog
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create an instance of the main QDialog
    my_dialog = Ui_Dialog1()

    # Show the dialog
    my_dialog.show()

    sys.exit(app.exec_())