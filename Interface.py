from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *


class Interface(object):
    def UI_Setup(self, Interface):
        if Interface.objectName():
            Interface.setObjectName(u"Interface")
        Interface.setFixedSize(712, 340)
        self.CBstate1 = QComboBox(Interface)
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.addItem("")
        self.CBstate1.setObjectName(u"CBstate1")
        self.CBstate1.setGeometry(QRect(20, 150, 181, 21))
        self.label = QLabel(Interface)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 651, 41))
        self.label_2 = QLabel(Interface)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 60, 621, 31))
        self.label_3 = QLabel(Interface)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 91, 21))
        self.label_4 = QLabel(Interface)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 120, 91, 21))
        self.label_5 = QLabel(Interface)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 120, 91, 21))
        self.CBstate2 = QComboBox(Interface)
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.addItem("")
        self.CBstate2.setObjectName(u"CBstate2")
        self.CBstate2.setGeometry(QRect(270, 150, 181, 21))
        self.CBstate3 = QComboBox(Interface)
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.addItem("")
        self.CBstate3.setObjectName(u"CBstate3")
        self.CBstate3.setGeometry(QRect(510, 150, 191, 21))
        self.label_6 = QLabel(Interface)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 180, 41, 31))
        self.label_7 = QLabel(Interface)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 220, 141, 31))
        self.AScheckbox = QCheckBox(Interface)
        self.AScheckbox.setObjectName(u"AScheckbox")
        self.AScheckbox.setGeometry(QRect(120, 225, 101, 21))
        self.pushButton = QPushButton(Interface)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 280, 221, 41))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)

        self.retranslateUi(Interface)

        QMetaObject.connectSlotsByName(Interface)

    def retranslateUi(self, Interface):
        Interface.setWindowTitle(QCoreApplication.translate("Interface", u"Form", None))
        self.CBstate1.setItemText(0, QCoreApplication.translate("Interface", u"-Select-", None))
        self.CBstate1.setItemText(1, QCoreApplication.translate("Interface", u"Andhra Pradesh", None))
        self.CBstate1.setItemText(2, QCoreApplication.translate("Interface", u"Andaman and Nicobar Islands	", None))
        self.CBstate1.setItemText(3, QCoreApplication.translate("Interface", u"Arunachal Pradesh", None))
        self.CBstate1.setItemText(4, QCoreApplication.translate("Interface", u"Assam", None))
        self.CBstate1.setItemText(5, QCoreApplication.translate("Interface", u"Bihar", None))
        self.CBstate1.setItemText(6, QCoreApplication.translate("Interface", u"Chandigarh", None))
        self.CBstate1.setItemText(7, QCoreApplication.translate("Interface", u"Chhattisgarh", None))
        self.CBstate1.setItemText(8, QCoreApplication.translate("Interface", u"Delhi", None))
        self.CBstate1.setItemText(9, QCoreApplication.translate("Interface", u"Goa", None))
        self.CBstate1.setItemText(10, QCoreApplication.translate("Interface", u"Gujarat", None))
        self.CBstate1.setItemText(11, QCoreApplication.translate("Interface", u"Haryana", None))
        self.CBstate1.setItemText(12, QCoreApplication.translate("Interface", u"Himachal Pradesh", None))
        self.CBstate1.setItemText(13, QCoreApplication.translate("Interface", u"Jammu and Kashmir", None))
        self.CBstate1.setItemText(14, QCoreApplication.translate("Interface", u"Jharkhand", None))
        self.CBstate1.setItemText(15, QCoreApplication.translate("Interface", u"Karnataka", None))
        self.CBstate1.setItemText(16, QCoreApplication.translate("Interface", u"Kerala", None))
        self.CBstate1.setItemText(17, QCoreApplication.translate("Interface", u"Ladakh", None))
        self.CBstate1.setItemText(18, QCoreApplication.translate("Interface", u"Madhya Pradesh", None))
        self.CBstate1.setItemText(19, QCoreApplication.translate("Interface", u"Maharashtra", None))
        self.CBstate1.setItemText(20, QCoreApplication.translate("Interface", u"Manipur", None))
        self.CBstate1.setItemText(21, QCoreApplication.translate("Interface", u"Mizoram", None))
        self.CBstate1.setItemText(22, QCoreApplication.translate("Interface", u"Odisha", None))
        self.CBstate1.setItemText(23, QCoreApplication.translate("Interface", u"Puducherry", None))
        self.CBstate1.setItemText(24, QCoreApplication.translate("Interface", u"Punjab", None))
        self.CBstate1.setItemText(25, QCoreApplication.translate("Interface", u"Rajasthan", None))
        self.CBstate1.setItemText(26, QCoreApplication.translate("Interface", u"Tamil Nadu", None))
        self.CBstate1.setItemText(27, QCoreApplication.translate("Interface", u"Telengana", None))
        self.CBstate1.setItemText(28, QCoreApplication.translate("Interface", u"Uttarakhand", None))
        self.CBstate1.setItemText(29, QCoreApplication.translate("Interface", u"Uttar Pradesh", None))
        self.CBstate1.setItemText(30, QCoreApplication.translate("Interface", u"West Bengal", None))

        self.CBstate1.setCurrentText(QCoreApplication.translate("Interface", u"-Select-", None))
        self.label.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Corona Virus Desktop Notification</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Select three States or tick to all : -</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State 1</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State 2</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State 3</span></p></body></html>", None))
        self.CBstate2.setItemText(0, QCoreApplication.translate("Interface", u"-Select-", None))
        self.CBstate2.setItemText(1, QCoreApplication.translate("Interface", u"Andhra Pradesh", None))
        self.CBstate2.setItemText(2, QCoreApplication.translate("Interface", u"Andaman and Nicobar Islands	", None))
        self.CBstate2.setItemText(3, QCoreApplication.translate("Interface", u"Arunachal Pradesh", None))
        self.CBstate2.setItemText(4, QCoreApplication.translate("Interface", u"Assam", None))
        self.CBstate2.setItemText(5, QCoreApplication.translate("Interface", u"Bihar", None))
        self.CBstate2.setItemText(6, QCoreApplication.translate("Interface", u"Chandigarh", None))
        self.CBstate2.setItemText(7, QCoreApplication.translate("Interface", u"Chhattisgarh", None))
        self.CBstate2.setItemText(8, QCoreApplication.translate("Interface", u"Delhi", None))
        self.CBstate2.setItemText(9, QCoreApplication.translate("Interface", u"Goa", None))
        self.CBstate2.setItemText(10, QCoreApplication.translate("Interface", u"Gujarat", None))
        self.CBstate2.setItemText(11, QCoreApplication.translate("Interface", u"Haryana", None))
        self.CBstate2.setItemText(12, QCoreApplication.translate("Interface", u"Himachal Pradesh", None))
        self.CBstate2.setItemText(13, QCoreApplication.translate("Interface", u"Jammu and Kashmir", None))
        self.CBstate2.setItemText(14, QCoreApplication.translate("Interface", u"Jharkhand", None))
        self.CBstate2.setItemText(15, QCoreApplication.translate("Interface", u"Karnataka", None))
        self.CBstate2.setItemText(16, QCoreApplication.translate("Interface", u"Kerala", None))
        self.CBstate2.setItemText(17, QCoreApplication.translate("Interface", u"Ladakh", None))
        self.CBstate2.setItemText(18, QCoreApplication.translate("Interface", u"Madhya Pradesh", None))
        self.CBstate2.setItemText(19, QCoreApplication.translate("Interface", u"Maharashtra", None))
        self.CBstate2.setItemText(20, QCoreApplication.translate("Interface", u"Manipur", None))
        self.CBstate2.setItemText(21, QCoreApplication.translate("Interface", u"Mizoram", None))
        self.CBstate2.setItemText(22, QCoreApplication.translate("Interface", u"Odisha", None))
        self.CBstate2.setItemText(23, QCoreApplication.translate("Interface", u"Puducherry", None))
        self.CBstate2.setItemText(24, QCoreApplication.translate("Interface", u"Punjab", None))
        self.CBstate2.setItemText(25, QCoreApplication.translate("Interface", u"Rajasthan", None))
        self.CBstate2.setItemText(26, QCoreApplication.translate("Interface", u"Tamil Nadu", None))
        self.CBstate2.setItemText(27, QCoreApplication.translate("Interface", u"Telengana", None))
        self.CBstate2.setItemText(28, QCoreApplication.translate("Interface", u"Uttarakhand", None))
        self.CBstate2.setItemText(29, QCoreApplication.translate("Interface", u"Uttar Pradesh", None))
        self.CBstate2.setItemText(30, QCoreApplication.translate("Interface", u"West Bengal", None))

        self.CBstate2.setCurrentText(QCoreApplication.translate("Interface", u"-Select-", None))
        self.CBstate3.setItemText(0, QCoreApplication.translate("Interface", u"-Select-", None))
        self.CBstate3.setItemText(1, QCoreApplication.translate("Interface", u"Andhra Pradesh", None))
        self.CBstate3.setItemText(2, QCoreApplication.translate("Interface", u"Andaman and Nicobar Islands	", None))
        self.CBstate3.setItemText(3, QCoreApplication.translate("Interface", u"Arunachal Pradesh", None))
        self.CBstate3.setItemText(4, QCoreApplication.translate("Interface", u"Assam", None))
        self.CBstate3.setItemText(5, QCoreApplication.translate("Interface", u"Bihar", None))
        self.CBstate3.setItemText(6, QCoreApplication.translate("Interface", u"Chandigarh", None))
        self.CBstate3.setItemText(7, QCoreApplication.translate("Interface", u"Chhattisgarh", None))
        self.CBstate3.setItemText(8, QCoreApplication.translate("Interface", u"Delhi", None))
        self.CBstate3.setItemText(9, QCoreApplication.translate("Interface", u"Goa", None))
        self.CBstate3.setItemText(10, QCoreApplication.translate("Interface", u"Gujarat", None))
        self.CBstate3.setItemText(11, QCoreApplication.translate("Interface", u"Haryana", None))
        self.CBstate3.setItemText(12, QCoreApplication.translate("Interface", u"Himachal Pradesh", None))
        self.CBstate3.setItemText(13, QCoreApplication.translate("Interface", u"Jammu and Kashmir", None))
        self.CBstate3.setItemText(14, QCoreApplication.translate("Interface", u"Jharkhand", None))
        self.CBstate3.setItemText(15, QCoreApplication.translate("Interface", u"Karnataka", None))
        self.CBstate3.setItemText(16, QCoreApplication.translate("Interface", u"Kerala", None))
        self.CBstate3.setItemText(17, QCoreApplication.translate("Interface", u"Ladakh", None))
        self.CBstate3.setItemText(18, QCoreApplication.translate("Interface", u"Madhya Pradesh", None))
        self.CBstate3.setItemText(19, QCoreApplication.translate("Interface", u"Maharashtra", None))
        self.CBstate3.setItemText(20, QCoreApplication.translate("Interface", u"Manipur", None))
        self.CBstate3.setItemText(21, QCoreApplication.translate("Interface", u"Mizoram", None))
        self.CBstate3.setItemText(22, QCoreApplication.translate("Interface", u"Odisha", None))
        self.CBstate3.setItemText(23, QCoreApplication.translate("Interface", u"Puducherry", None))
        self.CBstate3.setItemText(24, QCoreApplication.translate("Interface", u"Punjab", None))
        self.CBstate3.setItemText(25, QCoreApplication.translate("Interface", u"Rajasthan", None))
        self.CBstate3.setItemText(26, QCoreApplication.translate("Interface", u"Tamil Nadu", None))
        self.CBstate3.setItemText(27, QCoreApplication.translate("Interface", u"Telengana", None))
        self.CBstate3.setItemText(28, QCoreApplication.translate("Interface", u"Uttarakhand", None))
        self.CBstate3.setItemText(29, QCoreApplication.translate("Interface", u"Uttar Pradesh", None))
        self.CBstate3.setItemText(30, QCoreApplication.translate("Interface", u"West Bengal", None))

        self.CBstate3.setCurrentText(QCoreApplication.translate("Interface", u"-Select-", None))
        self.label_6.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">OR</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">All States </span></p></body></html>", None))
        self.AScheckbox.setText("")
        self.pushButton.setText(QCoreApplication.translate("Interface", u"Start Notifications", None))
