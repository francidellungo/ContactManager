import sys
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton, \
    QLabel, QCheckBox, QApplication
from PyQt5 import QtGui

from allContactsView import ContactManagerView, NewContactView
from contactsModel import ContactsModel


class StackedWindow(QWidget):
    def __init__(self, model):
        super(StackedWindow, self).__init__()
        windows = {'allContacts': 0,
                   'newContact': 1}

        # set window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/icon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # create stack with different windows
        self.Stack = QStackedWidget(self)
        self.all_contacts_window = ContactManagerView(model)
        self.new_contacts_window = NewContactView(model)

        # add windows to stack
        self.Stack.addWidget(self.all_contacts_window)
        self.Stack.addWidget(self.new_contacts_window)
        # self.Stack.addWidget(self.stack3)

        # behavior (when change stack item visualized)
        self.all_contacts_window.ui.newContact_pb.clicked.connect(lambda: self.display(windows['newContact']))
        self.new_contacts_window.ui.buttonBox.accepted.connect(lambda: self.display(windows['allContacts']))
        self.new_contacts_window.ui.buttonBox.rejected.connect(lambda: self.display(windows['allContacts']))



        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Stack)
        self.setLayout(hbox)
        self.show()


    def display(self, i):
        self.Stack.setCurrentIndex(i)


class stackedExample(QWidget):

    def __init__(self):
        super(stackedExample, self).__init__()
        self.leftlist = QListWidget()

        self.leftlist.insertItem(0, 'Contact')
        self.leftlist.insertItem(1, 'Personal')
        self.leftlist.insertItem(2, 'Educational')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()


    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        # self.setTabText(0,"Contact Details")
        self.stack1.setLayout(layout)


    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("Date of Birth", QLineEdit())

        self.stack2.setLayout(layout)


    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.stack3.setLayout(layout)


    def display(self, i):
        self.Stack.setCurrentIndex(i)


def main():
    app = QApplication(sys.argv)
    model = ContactsModel()
    ex = StackedWindow(model)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
