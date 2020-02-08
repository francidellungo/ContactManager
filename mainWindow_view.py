from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout
from mainWindow_ui import Ui_MainWindow
from formDialog_ui import Ui_Dialog
import sys

class contactManagerView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.newContact_pb.clicked.connect(self.onClick)

    def add_row(self, name, surname):
        # self.horiz = QHBoxLayout(self)
        # self.label_2 = QtWidgets.QLabel(self.ui.contacts_scrollAreaW)
        # self.label_2.setText(name)
        # self.ui.contacts_scrollAreaW
        pass

    def onClick(self):
        self.add_row('Name', 'Surname')

if __name__== "__main__":
    app = QApplication(sys.argv)
    window = contactManagerView()
    window.show()
    sys.exit(app.exec_())
