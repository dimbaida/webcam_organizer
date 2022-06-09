# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 179)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 451, 91))
        self.groupBox.setObjectName("groupBox")
        self.sourceFolder = QtWidgets.QLineEdit(self.groupBox)
        self.sourceFolder.setGeometry(QtCore.QRect(120, 20, 261, 20))
        self.sourceFolder.setObjectName("sourceFolder")
        self.destinationFolder = QtWidgets.QLineEdit(self.groupBox)
        self.destinationFolder.setGeometry(QtCore.QRect(120, 50, 261, 20))
        self.destinationFolder.setObjectName("destinationFolder")
        self.chooseSourceFolderButton = QtWidgets.QPushButton(self.groupBox)
        self.chooseSourceFolderButton.setGeometry(QtCore.QRect(390, 20, 51, 23))
        self.chooseSourceFolderButton.setObjectName("chooseSourceFolderButton")
        self.chooseDestinationFolderButton = QtWidgets.QPushButton(self.groupBox)
        self.chooseDestinationFolderButton.setGeometry(QtCore.QRect(390, 50, 51, 23))
        self.chooseDestinationFolderButton.setObjectName("chooseDestinationFolderButton")
        self.labelSource = QtWidgets.QLabel(self.groupBox)
        self.labelSource.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.labelSource.setObjectName("labelSource")
        self.labelDest = QtWidgets.QLabel(self.groupBox)
        self.labelDest.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.labelDest.setObjectName("labelDest")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(20, 110, 75, 23))
        self.startButton.setObjectName("startButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Choose Folders"))
        self.sourceFolder.setText(_translate("MainWindow", "enter source path"))
        self.destinationFolder.setText(_translate("MainWindow", "enter destination path"))
        self.chooseSourceFolderButton.setText(_translate("MainWindow", "Folder"))
        self.chooseDestinationFolderButton.setText(_translate("MainWindow", "Folder"))
        self.labelSource.setText(_translate("MainWindow", "Source Folder"))
        self.labelDest.setText(_translate("MainWindow", "Destination Folder"))
        self.startButton.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

