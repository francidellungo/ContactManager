import os
from PyQt5 import Qt, QtCore
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QCheckBox, QHBoxLayout, QWidget
from ui.contactDetails_ui import Ui_Dialog


class ContactDetails(QDialog):
    def __init__(self, model):
        super(ContactDetails, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.contact_id = None

        self.model = model

        self.icons = [
            './img/phoneIcon.png',
            './img/emailIcon.png',
            './img/notesIcon.png',
            './img/tagIcon.png'
        ]

        self.setTagIcon()

        # when window is closed clear lines
        self.ui.back_pb.clicked.connect(self.clearLines)
        self.ui.edit_pb.clicked.connect(self.clearLines)

        # delete contact behavior
        self.ui.delete_pb.clicked.connect(self.deleteContact)

    def setTagIcon(self):
        # set tag icon
        icon_label = QtWidgets.QLabel()
        # todo fix
        pixmap = QPixmap(self.icons[3])
        pixmap = pixmap.scaledToWidth(20)
        pixmap = pixmap.scaledToHeight(20)
        icon_label.setPixmap(pixmap)
        icon_label.setFixedWidth(40)
        icon_label.setAlignment(QtCore.Qt.AlignTop)

        self.ui.tag_h_layout.insertWidget(0, icon_label)

    def deleteContact(self):
        buttonReply = QMessageBox.question(self, 'Remove contact', "Are you sure you want to delete " + self.ui.contact_label.text() + "?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.model.deleteContact(self.contact_id)
        # if buttonReply == QMessageBox.No:
        #     print('No clicked.')

    def showDetails(self, contact_id):
        # get contact info from model
        contact_details = list(self.model.getContactInfofromId(contact_id))[1:]
        # set window title: contact name and surname
        self.ui.contact_label.setText(contact_details[0] + ' ' + contact_details[1])

        # set contact details (icon and text)
        for detail_idx, detail in enumerate(contact_details):
            # TODO fix here detail_idx != 0 and detail_idx != 1
            if detail != '' and detail_idx != 0 and detail_idx != 1:
                # no icon for name and surname
                if detail_idx != 0 and detail_idx != 1:
                    icon = self.icons[detail_idx - 2]
                else:
                    icon = None
                name = (str(detail) if detail is not None else ' ')
                row = Row(icon, name, detail_idx)
                self.ui.contact_info_layout.addWidget(row)

        # show contact tags
        all_tags = self.model.getAllTags()
        contact_tags = self.model.getContactTags(contact_id)




        for tag in all_tags:
            tag_w = QCheckBox()
            tag_w.setObjectName(tag)
            tag_w.setText(tag)
            if tag in contact_tags:
                tag_w.setChecked(True)
            tag_w.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

            # add tag to tag layout
            self.ui.tags_layout.addWidget(tag_w)

            # if detail != '':
                # layout = QtWidgets.QHBoxLayout()
                # field_icon = QtWidgets.QLabel()
                # pixmap = QPixmap('img/phoneIcon2.png')
                # field_icon.setPixmap(pixmap.scaledToWidth(30))
                # # self.resize(pixmap.width(), pixmap.height())
                # layout.addWidget(field_icon)
                # layout.addWidget(QtWidgets.QLabel((str(detail) if detail is not None else ' ')))
                # self.ui.contact_info_layout.addWidget(QtWidgets.QLabel((str(detail) if detail is not None else ' ')))
                # self.ui.contact_info_layout.addWidget(layout.widget())

                # self.horiz = QtWidgets.QHBoxLayout(self)
                # self.img_label = QLabel()
                # self.img_label.setScaledContents(True)
                # pixmap = QPixmap(os.path.join('img', 'phoneIcon2.png'))
                # self.img_label.setPixmap(pixmap)
                # self.img_label.setFixedSize(150, 150)
                # self.horiz.addWidget(self.img_label)
                # self.horiz.addWidget(QtWidgets.QLabel(str(detail)))
                # self.ui.contact_info_layout.addWidget(self.horiz.widget())

    def clearLines(self):
        self.ui.contact_label.clear()
        for i in reversed(range(self.ui.contact_info_layout.count())):
            item = self.ui.contact_info_layout.itemAt(i).widget()
            item.deleteLater()
        for i in range(self.ui.tags_layout.count()):
            self.ui.tags_layout.itemAt(i).widget().deleteLater()

    def setContact(self, contact_id):
        self.contact_id = contact_id


class Row(QWidget):
    def __init__(self, icon=None, text=None, detail_idx=None):
        super(Row, self).__init__()
        self.horiz = QHBoxLayout(self)
        self.detail_idx = detail_idx

        # set element icon
        if icon is not None:
            self.setIcon(icon)

        # add text to horizontal layout
        if text is not None:
            # set element text
            # todo fix here
            if self.detail_idx != 4:
                self.text = QtWidgets.QLabel(text)
            else:
                self.text = QtWidgets.QTextBrowser()
                self.text.setText(text)
                self.text.setMaximumSize(self.width(), 100)

            self.horiz.addWidget(self.text)

    def setIcon(self, icon):
        self.icon = QtWidgets.QLabel()
        pixmap = QPixmap(icon)
        pixmap = pixmap.scaledToWidth(20)
        pixmap = pixmap.scaledToHeight(20)
        self.icon.setPixmap(pixmap)
        self.icon.setFixedWidth(30)

        # add icon to horizontal layout
        self.horiz.addWidget(self.icon)
