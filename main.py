import sys
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton, \
    QLabel, QCheckBox, QApplication, QDialogButtonBox
from PyQt5 import QtGui, QtCore

# from allContactsView import ContactManagerView
from contactsModel import ContactsListModel
from Views.newContactView import NewContactView
from Views.detailContactView import ContactDetails
from Views.allContactsView import AllContactsView
from tagModel import TagsModel


class StackedWindow(QWidget):
    def __init__(self, contacts_model, tags_model):  # contacts_tags_model
        super(StackedWindow, self).__init__()
        self.setWindowTitle('Contact Manager')
        self.windows = {'allContacts': 0,
                        'newContact': 1,
                        'detailContact': 2}

        # current_contact = None
        self.contacts_model = contacts_model
        self.tags_model = tags_model
        # self.contacts_tags_model = contacts_tags_model

        # set window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/icon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # create stack with different windows
        self.Stack = QStackedWidget(self)

        self.all_contacts_window = AllContactsView(self.contacts_model, self.tags_model)
        self.new_contacts_window = NewContactView(self.contacts_model, self.tags_model)
        self.details_contact = ContactDetails(self.contacts_model)

        # add windows to stack
        self.Stack.addWidget(self.all_contacts_window)
        self.Stack.addWidget(self.new_contacts_window)
        self.Stack.addWidget(self.details_contact)

        # self.Stack.setCurrentIndex(windows['allContacts'])
        # self.Stack.addWidget(self.stack3)

        # behavior (when change stack item visualized)
        self.all_contacts_window.ui.newContact_pb.clicked.connect(lambda: self.display(self.windows['newContact']))
        self.all_contacts_window.ui.newContact_pb.clicked.connect(lambda: self.new_contacts_window.setTags())
        self.all_contacts_window.ui.newContact_pb.clicked.connect(lambda: self.new_contacts_window.setContact(None))

        self.new_contacts_window.ui.buttonBox.accepted.connect(lambda: self.display(self.windows['allContacts'])) #, self.new_contacts_window.contact
        self.new_contacts_window.ui.buttonBox.accepted.connect(self.all_contacts_window.showContacts)
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
        # self.contacts_model.contact_removed.connect(self.all_contacts_window.refreshContacts)
        self.contacts_model.contact_removed.connect(self.details_contact.clearLines)
        # signal emitted when window changes

        # signal for tag_added
        self.new_contacts_window.tag_added.connect(self.all_contacts_window.refreshTags)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Stack)
        self.setLayout(hbox)
        self.setMaximumSize(QtCore.QSize(350, 650))
        self.setFixedWidth(450)
        self.show()


    def display(self, window_id, contact_id=None):
        self.Stack.setCurrentIndex(window_id)

        self.setMaximumSize(QtCore.QSize(350, 650))
        # TODO: two instances no refresh in all contacts when one is changed (maybe delete contact_added,
        #  contact_removed and contact_updated and add these rows below (to refresh all contacts window) or
        #  get notifications from db when it is modified
        # update list of all contacts
        # if self.Stack.currentIndex() == self.windows['allContacts']:
        #     self.Stack.currentWidget().showContacts()

        if contact_id is not None:
            self.Stack.currentWidget().setContact(contact_id)
            contact_info = self.contacts_model.getContactInfofromId(contact_id)
            self.setWindowTitle(contact_info[1] + ' ' + contact_info[2])
        else:
            self.setWindowTitle('Contact Manager')
        print('display: ', window_id, contact_id)



def main():
    app = QApplication(sys.argv)
    model = ContactsListModel()
    tags_m = TagsModel()
    ex = StackedWindow(model, tags_m)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
