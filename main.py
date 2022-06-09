import sys, os
import body
import logging
import xml.etree.cElementTree as ET
from ui import *
from PIL import Image
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

'''
TOKEN = 'dfadsg'
MAIN_URL = f'sdsd{TOKEN}'
print(MAIN_URL)
'''

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.chooseSourceFolderButton.clicked.connect(self.choose_source_folder_clicked)
        self.ui.chooseDestinationFolderButton.clicked.connect(self.choose_destination_folder_clicked)
        self.ui.startButton.clicked.connect(self.start_button_clicked)

        # get previous paths
        paths = ET.parse("paths.xml").getroot()
        source_folder = paths[0][0].text
        destination_folder = paths[0][1].text

        self.ui.sourceFolder.setText(source_folder)
        self.ui.destinationFolder.setText(destination_folder)

    def choose_source_folder_clicked(self):
        path = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.ui.sourceFolder.setText(path)

    def choose_destination_folder_clicked(self):
        path = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.ui.destinationFolder.setText(path)

    def test_log_button_clicked(self):
        self.ui.log.appendPlainText("111")

    def start_button_clicked(self):
        source_folder = self.ui.sourceFolder.text()
        destination_folder = self.ui.destinationFolder.text()
        body.process_images(source_folder, destination_folder)

        # write paths xml
        root = ET.Element('root')
        doc = ET.SubElement(root, 'doc')
        ET.SubElement(doc, 'path', name="source_folder").text = source_folder
        ET.SubElement(doc, 'path', name="destination_folder").text = destination_folder
        tree = ET.ElementTree(root)
        tree.write('paths.xml')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyWin()
    myApp.show()
    sys.exit(app.exec())