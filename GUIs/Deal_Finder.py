import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QListView, QWidget, QDialog
from PyQt5.QtCore import Qt, QStringListModel
import sqlite3

from GUIs.Home import Ui_MainWindow
from GUIs.Post_deal import Ui_Dialog1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.PostDeal.clicked.connect(self.open_dialog)




        # Load the UI file created in Qt Designer
        self.ui_widget = Ui_MainWindow()
        self.ui_widget.setupUi(self)

        # Set up SQLite database connection
        self.conn = sqlite3.connect('deals_db.db')  # Change the database name as needed
        self.create_table()

        # Set up QListView
        self.model = QStringListModel()
        self.ui_widget.results.setModel(self.model)

        # Connect button click signals to slots
        self.ui_widget.pushButton_10.clicked.connect(self.add_deal)
        self.ui_widget.pushButton.clicked.connect(self.perform_search)

    def create_table(self):
        # Create a table if it doesn't exist
        query = '''
                CREATE TABLE IF NOT EXISTS deals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT,
                    discount INTEGER
                )
                '''
        with self.conn:
            self.conn.execute(query)

    def add_deal(self):
        # Get deal details from line edits
        product_name = self.ui_widget.lineEdit_3.text()
        discount = self.ui_widget.lineEdit_7.value()

        # Insert the deal into the database
        with self.conn:
            self.conn.execute('INSERT INTO deals (product_name, discount) VALUES (?, ?)', (product_name, discount))

        # Clear input fields
        self.ui_widget.lineEdit_3.clear()
        self.ui_widget.lineEdit_7.setValue(0)

        # Refresh the deal list
        self.update_deal_list()

    def perform_search(self):
        # Get the search query from the line edit
        search_query = self.ui_widget.search.text()

        # Fetch and display search results from the database
        with self.conn:
            cursor = self.conn.execute('SELECT product_name, discount FROM deals WHERE product_name LIKE ?', (f'%{search_query}%',))
            results = [f'{row[0]} - {row[1]}% off' for row in cursor.fetchall()]

        # Update the QListView model with search results
        self.model.setStringList(results)

    def update_deal_list(self):
        # Fetch all deals from the database and update the list
        with self.conn:
            cursor = self.conn.execute('SELECT product_name, discount FROM deals')
            deals = [f'{row[0]} - {row[1]}% off' for row in cursor.fetchall()]

        # Update the QListView model with all deals
        self.model.setStringList(deals)

    def open_dialog(self):
        dialog = QDialog()
        dialog_ui = Ui_Dialog1()
        dialog_ui.setupUi(dialog)
        dialog.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
