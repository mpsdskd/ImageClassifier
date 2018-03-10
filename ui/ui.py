# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QMainWindow,  QFileDialog,  QProgressBar
from PyQt5.QtGui import QPixmap

from .Ui_ui import Ui_MainWindow

from shutil import move
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.open_files = QFileDialog.getOpenFileNames(
                None,
                "Open Image-file",
                "",
                "Image-File (*.jpg *.png *.bmp *.jpeg)")[0]
        self.image_number=len(self.open_files)
        if self.image_number==0:
            self.close()
        
        self.progressBar = QProgressBar()

        self.update_progress()
        self.statusBar.addPermanentWidget(self.progressBar)

    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        if self.lineEdit_1.text():
            self.move_image(self.lineEdit_1.text())


    @pyqtSlot()
    def on_pushButton_2_clicked(self):

        if self.lineEdit_2.text():
            self.move_image(self.lineEdit_2.text())

    @pyqtSlot()
    def on_pushButton_3_clicked(self):

        if self.lineEdit_3.text():
            self.move_image(self.lineEdit_3.text())

    @pyqtSlot()
    def on_pushButton_4_clicked(self):

        if self.lineEdit_4.text():
            self.move_image(self.lineEdit_4.text())

    def move_image(self,  subfolder):
        print(subfolder)
        if not os.path.isdir(os.path.dirname(self.open_files[0])+"/"+subfolder):
            os.mkdir(os.path.dirname(self.open_files[0])+"/"+subfolder)
        move(self.open_files[0], os.path.dirname(self.open_files[0])+"/"+subfolder+"/"+os.path.basename(self.open_files[0]))
        del self.open_files[0]

        self.update_progress()
    
    def update_progress(self):
        self.progressBar.setValue(round((self.image_number-len(self.open_files))/self.image_number * 100,  2))
        self.statusBar.showMessage("Image "+ str(self.image_number-len(self.open_files))+"/"+str(self.image_number))
        print("Image "+ str(len(self.open_files))+"/"+str(self.image_number))
        
        if len(self.open_files)>0:
            # pixmap=QPixmap()
            self.label.setPixmap(QPixmap(self.open_files[0]))#.scaled(self.label.height(), Qt.KeepAspectRatioByExpanding))
            if self.open_files[1]:
                self.label_2.setPixmap(QPixmap(self.open_files[1]))#.scaled(self.label_2.height(), Qt.KeepAspectRatioByExpanding))
                if self.open_files[2]:
                    self.label_3.setPixmap(QPixmap(self.open_files[2]))            
                    if self.open_files[3]:
                        self.label_4.setPixmap(QPixmap(self.open_files[3]))
                        if self.open_files[4]:
                            self.label_5.setPixmap(QPixmap(self.open_files[4]))
