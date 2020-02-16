import sys
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton, \
    QLabel, QCheckBox, QApplication, QDialogButtonBox
from PyQt5 import QtGui, QtCore

# from allContactsView import ContactManagerView
from contactsModel import ContactsListModel
from Views.newContactView import NewContactView
from Views.detailContactView import ContactDetails
from Views.allContactsView import AllContactsView


class StackedWindow(QWidget):
    def __init__(self, model):
        super(StackedWindow, self).__init__()
        self.windows = {'allContacts': 0,
                        'newContact': 1,
                        'detailContact': 2}

        current_contact = None
        self.contacts_model = model

        # set window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/icon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # create stack with different windows
        self.Stack = QStackedWidget(self)

        self.all_contacts_window = AllContactsView(model)
        self.new_contacts_window = NewContactView(model)
        self.details_contact = ContactDetails(model)

        # add windows to stack
        self.Stack.addWidget(self.all_contacts_window)
        self.Stack.addWidget(self.new_contacts_window)
        self.Stack.addWidget(self.details_contact)

        # self.Stack.setCurrentIndex(windows['allContacts'])
        # self.Stack.addWidget(self.stack3)

        # behavior (when change stack item visualized)
        self.all_contacts_window.ui.newContact_pb.clicked.connect(lambda: self.display(self.windows['newContact']))

        self.new_contacts_window.ui.buttonBox.accepted.connect(lambda: self.display(self.windows['allContacts'])) #, self.new_contacts_window.contact
        self.new_contacts_window.ui.buttonBox.accepted.connect(self.all_contacts_window.refreshContacts)
        self.new_contacts_window.ui.buttonBox.rejected.connect(lambda: self.display(self.windows['allContacts']))
        self.details_contact.ui.back_pb.clicked.connect(lambda: self.display(self.windows['allContacts']))

        self.details_contact.ui.edit_pb.clicked.connect(lambda: self.display(self.windows['newContact'], self.details_contact.contact_id))
        self.details_contact.ui.back_pb.clicked.connect(lambda: self.display(self.windows['allContacts']))

        # self.all_contacts_window.contact_clicked.connect(self.details_contact.setContact)
        self.all_contacts_window.contact_clicked.connect(lambda: self.display(self.windows['detailContact']))

        # TODO fix everything!!!!
        self.all_contacts_window.contact_clicked.connect(self.details_contact.showDetails)
        self.all_contacts_window.contact_clicked.connect(self.details_contact.setContact)
        # self.details_contact.ui.edit_pb.clicked.connect(self)

        self.contacts_model.contact_removed.connect(lambda: self.display(self.windows['allContacts']))
        self.contacts_model.contact_removed.connect(self.all_contacts_window.refreshContacts)
        self.contacts_model.contact_removed.connect(self.details_contact.clearLines)
        # signal emitted when window changes
        self.Stack.currentChanged.connect(self.onCurrentChanged)


        # NEW COMMANDS:::
        # open details of existing contact
        # self.all_contacts_window.contact_clicked.connect(lambda: self.display(windows['detailContact']))
        # self.all_contacts_window.contact_clicked.connect()

        hbox = QHBoxLayout(self)
        # setMaximumSize(QtCore.QSize(483, 16777215))
        hbox.addWidget(self.Stack)
        self.setLayout(hbox)
        self.setMaximumSize(QtCore.QSize(483, 800))
        self.show()

    def onCurrentChanged(self, i):
        print('current window: ', i)
        # if i ==


    def display(self, i, contact=None):
        self.Stack.setCurrentIndex(i)
        # TODO fix setting contact
        if contact is not None:
            self.Stack.currentWidget().setContact(contact)
        print('display: ', i, contact)


# class stackedExample(QWidget):
#
#     def __init__(self):
#         super(stackedExample, self).__init__()
#         self.leftlist = QListWidget()
#
#         self.leftlist.insertItem(0, 'Contact')
#         self.leftlist.insertItem(1, 'Personal')
#         self.leftlist.insertItem(2, 'Educational')
#
#         self.stack1 = QWidget()
#         self.stack2 = QWidget()
#         self.stack3 = QWidget()
#
#         self.stack1UI()
#         self.stack2UI()
#         self.stack3UI()
#
#         self.Stack = QStackedWidget(self)
#         self.Stack.addWidget(self.stack1)
#         self.Stack.addWidget(self.stack2)
#         self.Stack.addWidget(self.stack3)
#
#         hbox = QHBoxLayout(self)
#         hbox.addWidget(self.leftlist)
#         hbox.addWidget(self.Stack)
#
#         self.setLayout(hbox)
#         self.leftlist.currentRowChanged.connect(self.display)
#         self.setGeometry(300, 50, 10, 10)
#         self.setWindowTitle('StackedWidget demo')
#         self.show()
#
#
#     def stack1UI(self):
#         layout = QFormLayout()
#         layout.addRow("Name", QLineEdit())
#         layout.addRow("Address", QLineEdit())
#         # self.setTabText(0,"Contact Details")
#         self.stack1.setLayout(layout)
#
#
#     def stack2UI(self):
#         layout = QFormLayout()
#         sex = QHBoxLayout()
#         sex.addWidget(QRadioButton("Male"))
#         sex.addWidget(QRadioButton("Female"))
#         layout.addRow(QLabel("Sex"), sex)
#         layout.addRow("Date of Birth", QLineEdit())
#
#         self.stack2.setLayout(layout)
#
#
#     def stack3UI(self):
#         layout = QHBoxLayout()
#         layout.addWidget(QLabel("subjects"))
#         layout.addWidget(QCheckBox("Physics"))
#         layout.addWidget(QCheckBox("Maths"))
#         self.stack3.setLayout(layout)
#
#
#     def display(self, i):
#         self.Stack.setCurrentIndex(i)


def main():
    app = QApplication(sys.argv)
    model = ContactsListModel()
    ex = StackedWindow(model)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
