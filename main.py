import sys
from PySide2 import QtWidgets
from Interface import Interface
from notification import Notification


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Interface()
        self.ui.UI_Setup(self)
        self.list = []
        self.flag = 0
        self.ui.pushButton.clicked.connect(self.trigger)

    def trigger(self):
        if self.ui.AScheckbox.isChecked():
            self.flag = 1
            a = Notification()
            a.parser(self.list, self.flag)
        else:

            self.list.append(self.ui.CBstate1.currentText())
            self.list.append(self.ui.CBstate2.currentText())
            self.list.append(self.ui.CBstate3.currentText())
            a = Notification()
            a.parser(self.list, self.flag)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())