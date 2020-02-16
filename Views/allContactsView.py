from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from ui.mainWindow_ui import Ui_MainWindow


class AllContactsView(QMainWindow):
    contact_clicked = pyqtSignal(int)

    def __init__(self, model):
        super(AllContactsView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # db of contacts
        self.model = model
        self.showContacts()

        # connect buttons to slots
        # self.ui.newContact_pb.clicked.connect(self.createNewContact)
        self.ui.sort_combobox.currentIndexChanged.connect(self.sortBy)

        self.model.contact_added.connect(self.refreshContacts)

    def showContacts(self, contacts_=None):
        contacts = (contacts_ if contacts_ is not None else self.model.getAllContacts())
        for id, contact in enumerate(contacts):
            new_contact = QtWidgets.QPushButton(self.ui.contacts_scrollAreaW)
            new_contact.setFlat(True)
            # new_label.setParent(self.ui.contacts_scrollAreaW)
            new_contact.setText(contact[1] + ' ' + contact[2])
            new_contact.setObjectName(str(contact[0]))
            if id != 0:
                line = QtWidgets.QFrame(self.ui.contacts_scrollAreaW)
                line.setFrameShape(QtWidgets.QFrame.HLine)
                line.setFrameShadow(QtWidgets.QFrame.Sunken)
                line.setObjectName("line")
                self.ui.contacts_layout.addWidget(line)
            self.ui.contacts_layout.addWidget(new_contact)
            new_contact.clicked.connect(lambda: self.clicked(new_contact))

    def refreshContacts(self, contacts=None):
        for i in reversed(range(self.ui.contacts_layout.count())):
            item = self.ui.contacts_layout.itemAt(i).widget()
            item.deleteLater()
            # self.ui.contacts_layout.removeWidget(item)
        print('removed all contacts', self.ui.contacts_layout.count())
        self.showContacts(contacts)

    def sortBy(self, field, mode='ASC'):
        # field to sort by
        # print('sort by', field)
        field_to_sort = ('name' if field == 0 else 'surname')
        contacts = self.model.getAllContacts(field_to_sort)
        self.refreshContacts(contacts)
        pass

    def clicked(self, contact):
        # contact_id = int(contact.objectName())
        sender_id = int(self.sender().objectName())
        print('contact clicked, sender_id: ', sender_id)
        # print('sender_id', contact_id, ' ', sender_id, ' ', type(sender_id))
        # contact_info = self.model.getContactInfo(sender_id)
        # send id of the contact
        self.contact_clicked.emit(sender_id)