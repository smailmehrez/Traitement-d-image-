# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'im.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCan
import matplotlib.pyplot as plt
import cv2
import numpy as np
import statistics as st
import warnings
import time
warnings.filterwarnings("ignore")



def tri_image_nvg(img):
    img_r = img.flatten()
    img_tri = np.sort(img_r)

    return img_tri
def diviser_vecteur(vecteur, k):
    if k == 0:
        return [vecteur]

    n = len(vecteur)
    vecteur1 = vecteur[:n // 2]
    vecteur2 = vecteur[n // 2:]

    sous_vecteurs1 = diviser_vecteur(vecteur1, k - 1)
    sous_vecteurs2 = diviser_vecteur(vecteur2, k - 1)

    # Concaténer les sous-vecteurs
    return sous_vecteurs1 + sous_vecteurs2
def calculer_moyennes_nvg(img, k):
    img_tri = tri_image_nvg(img)
    segments = diviser_vecteur(img_tri, k)

    moyennes = []
    for i in range(2 ** k):
        moyennes.append(np.mean(segments[i]))

    return np.uint16(moyennes)
def remplacer_valeurs_nvg(img, k):
    img2 = np.zeros(img.shape, np.uint8)
    h, w = img.shape
    m = calculer_moyennes_nvg(img, k)
    for i in range(h):
        for j in range(w):
            val = img[i, j]
            indice = np.argmin(abs(np.int16(m - val)))
            img2[i, j] = m[indice]

    return img2
def remplacer_valeurs_clr_v2(img, k):
    b, g, r = cv2.split(img)
    img1 = remplacer_valeurs_nvg(b, k).reshape((b.shape))
    img2 = remplacer_valeurs_nvg(g, k).reshape((g.shape))
    img3 = remplacer_valeurs_nvg(r, k).reshape((r.shape))

    img_res = cv2.merge((img1, img2, img3))

    return img_res
def uniforme_nvg(img, h, w, nb_vals):
    img2 = np.zeros(img.shape, np.uint8)
    diff = 256 / nb_vals
    for i in range(h):
        for j in range(w):
            img2[i, j] = int(img[i, j] / diff) * diff
    return img2
def uniforme_clr(img, h, w, c, nb_vals):
    img2 = np.zeros(img.shape, np.uint8)
    diff = 256 / nb_vals
    for i in range(h):
        for j in range(w):
            for k in range(c):
                img2[i, j, k] = int(img[i, j, k] / diff) * diff
    return img2


class Ui_MainWindow(QDialog):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("#MainWindow {\n"
"    background-color: #F2F4F4;\n"
"\n"
"}\n"
"#widget  {\n"
"    border-radius: 10px;\n"
"}\n"
"#widget_2 {\n"
"    border: 2px solid #F2F4F4; \n"
"    border-radius: 10px;\n"
"}\n"
"#widget_3 {\n"
"     background-color: #E5E8E8;\n"
"    border: 2px solid #F2F4F4; \n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(1, 0, 251, 980))
        self.widget_2.setStyleSheet("background-color: #E5E8E8;")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 230, 30))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browsefiles)
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(0, 10, 250, 250))
        self.widget.setStyleSheet("background-image: url(logo1.png);")
        self.widget.setObjectName("widget")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 340, 230, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Histogramme)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 380, 230, 30))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Histogramme_cumule)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 420, 230, 30))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.Histogramme_normalise)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 460, 230, 30))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.inversion_histogram)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 500, 230, 30))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.segmentation)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(30, 540, 67, 17))
        self.label.setStyleSheet("\n"
"font: 75 oblique 20pt \"Tlwg Typist\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(160, 540, 67, 17))
        self.label_2.setStyleSheet("\n"
"font: 75 oblique 20pt \"Tlwg Typist\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 560, 81, 25))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 670, 81, 30))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 590, 230, 30))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.egalisation)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 630, 230, 30))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.expansion)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 670, 141, 30))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.translation)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 560, 81, 25))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 710, 230, 30))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.quantification)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 750, 230, 30))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.Median)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 790, 230, 30))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.uniforme)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 870, 131, 30))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.impot)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_14.setGeometry(QtCore.QRect(150, 870, 91, 30))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.extract_frame)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 830, 230, 30))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.etiquetage)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 910, 230, 30))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.comress)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(261, 0, 1650, 980))
        self.widget_3.setStyleSheet("\n"
"#widget {\n"
"    background-color: #E5E8E8;\n"
"\n"
"}\n"
"#frame  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#frame_2  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"#frame_3  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"#frame_4  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"#frame_5  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"#frame_6  {\n"
"   \n"
"    border-radius: 20px;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.frame = QtWidgets.QFrame(self.widget_3)
        self.frame.setGeometry(QtCore.QRect(20, 20, 521, 470))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.widget_3)
        self.frame_2.setGeometry(QtCore.QRect(565, 20, 521, 470))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.frame_3 = QtWidgets.QFrame(self.widget_3)
        self.frame_3.setGeometry(QtCore.QRect(1110, 20, 521, 470))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.widget_3)
        self.frame_4.setGeometry(QtCore.QRect(20, 500, 521, 470))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.widget_3)
        self.frame_5.setGeometry(QtCore.QRect(565, 500, 521, 470))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.widget_3)
        self.frame_6.setGeometry(QtCore.QRect(1110, 500, 521, 470))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_11 = QtWidgets.QVBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.figure = plt.figure(facecolor="#E5E8E8")
        self.canvas = FigureCan(self.figure)
        self.horizontalLayout_11.addWidget(self.canvas)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_12 = QtWidgets.QVBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.canvas2 = FigureCan(self.figure)
        self.horizontalLayout_12.addWidget(self.canvas2)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_13 = QtWidgets.QVBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.canvas3 = FigureCan(self.figure)
        self.horizontalLayout_13.addWidget(self.canvas3)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_14 = QtWidgets.QVBoxLayout(self.frame_4)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.canvas4 = FigureCan(self.figure)
        self.horizontalLayout_14.addWidget(self.canvas4)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_15 = QtWidgets.QVBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.canvas5 = FigureCan(self.figure)
        self.horizontalLayout_15.addWidget(self.canvas5)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.canvas6 = FigureCan(self.figure)
        self.horizontalLayout_16.addWidget(self.canvas6)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def browsefiles(self):
        self.figure.clear()
        global image
        global imnb
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'c:\codefirst.io\PyQt5 tutorials\Browse Files', 'Images (*.png, *.xmp *.jpg)')
        print(fname[0])
        img = cv2.imread(fname[0])
        print(fname[0])
        imnb=cv2.imread(fname[0],0)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.xlabel('width')
        plt.ylabel('height')
        plt.title("Image")
        self.canvas.draw()
        image=img
        return (image,imnb)

    def Histogramme(self):
        self.figure.clear()
        #plt.style.use('ggplot')
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        h, w = imnb.shape
        # simple
        H1 = np.zeros((256, 1), np.uint32)
        for i in range(h):
            for j in range(w):
                H1[imnb[i, j]] += 1
        plt.plot(H1)

        plt.xlabel("NG")
        plt.ylabel("NB")
        plt.title("Histogramme")
        self.canvas2.draw()
        return (H1)

    def Histogramme_cumule(self):
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        h, w = imnb.shape
        # simple
        H1 = np.zeros((256, 1), np.uint32)
        for i in range(h):
            for j in range(w):
                H1[imnb[i, j]] += 1
        H2 = np.copy(H1)
        for i in range(1, 256):
            H2[i] = H2[i] + H2[i - 1]
        plt.plot(H2)
        plt.xlabel("NG")
        plt.ylabel("NB")
        plt.title("Histogramme cumulé")
        self.canvas3.draw()

    def Histogramme_normalise(self):
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        h, w = imnb.shape
        nb_pixels = h * w
        # simple
        H1 = np.zeros((256, 1), np.uint32)
        for i in range(h):
            for j in range(w):
                H1[imnb[i, j]] += 1
        H3 = np.copy(H1) / nb_pixels
        plt.plot(H3)
        plt.xlabel("NG")
        plt.ylabel("NB")
        plt.title("Histogramme normalisé")
        self.canvas6.draw()

    def inversion_histogram(self):
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        h, w = imnb.shape
        img2 = np.zeros((h,w), np.uint8)

        for i in range(h):
            for j in range(w):
                img2[i, j] = 255 - imnb[i, j]
        plt.imshow(img2, cmap='gray')
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("Inversion Image")
        self.canvas4.draw()
        self.inver(img2)

    def inver(self,img2):
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        h, w = img2.shape
        # simple
        H6 = np.zeros((256, 1), np.uint32)
        for i in range(h):
            for j in range(w):
                H6[img2[i, j]] += 1
        plt.plot(H6)

        plt.xlabel("NB")
        plt.ylabel("NB")
        plt.title("Inversion Histogram")
        self.canvas5.draw()

    def segmentation(self):
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        h, w = imnb.shape
        img_res = np.zeros(imnb.shape, np.uint8)

        for i in range(h):
            for j in range(w):
                if imnb[i, j] > int(self.lineEdit.text()) and imnb[i, j] < int(self.lineEdit_2.text()):
                    img_res[i, j] = 255
                else:
                    img_res[i, j] = 0
        plt.imshow(img_res, cmap='gray')
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("Segmentation")
        self.canvas4.draw()

    def egalisation(self):
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        h, w = imnb.shape
        nb_pixels = h * w

        # creation du premier histogramme
        H1 = np.zeros((256, 1), np.uint32)
        for i in range(h):
            for j in range(w):
                H1[imnb[i, j]] += 1

        # egalisation
        H_cn = np.cumsum(H1)

        H_cn = H_cn / nb_pixels

        valeurs = imnb.ravel()
        max_val = max(valeurs)

        H_eg = np.copy(H_cn) * max_val

        img_res = np.zeros(imnb.shape, np.uint8)

        for i in range(h):
            for j in range(w):
                img_res[i, j] = H_eg[imnb[i, j]]

        # creation du deuxième histogramme
        H2 = np.zeros((256, 1), np.uint32)
        for i in range(h):
            for j in range(w):
                H2[img_res[i, j]] += 1

        # affichage du deuxième histogramme
        plt.xlabel("NG")
        plt.ylabel("NB")
        plt.title("Histogramme après égalisation")
        plt.plot(H2)
        self.canvas5.draw()

        # img_res_auto = cv2.equalizeHist(img)

        # affichage des deux images
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        plt.imshow(img_res,cmap='gray')
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("Egalisation")
        self.canvas4.draw()

    def expansion(self):
        h, w = imnb.shape
        # creation du premier histogramme
        H1 = np.zeros((256, 1), np.uint32)
        for i in range(h):
            for j in range(w):
                H1[imnb[i, j]] += 1

        # expansion dynamique
        # récupération de l'intensité maximale et minimale dans l'image
        valeurs = imnb.ravel()
        min_val = min(valeurs)
        max_val = max(valeurs)

        img_res = np.zeros(imnb.shape, np.uint8)
        for i in range(h):
            for j in range(w):
                img_res[i, j] = (255 * (imnb[i, j] - min_val)) / (max_val - min_val)

        # creation du deuxième histogramme
        H2 = np.zeros((256, 1), np.uint32)
        for i in range(h):
            for j in range(w):
                H2[img_res[i, j]] += 1

        # affichage du deuxième histogramme
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        plt.xlabel("NG")
        plt.ylabel("NB")
        plt.title("Histogramme après expansion dynamique")
        plt.plot(H2)
        self.canvas5.draw()

        # affichage des deux images
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        plt.imshow(img_res, cmap='gray')
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("Expansion dynamique")
        self.canvas4.draw()

    def translation(self):
        ecart=int(self.lineEdit_3.text())
        img_res = imnb - ecart
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        plt.imshow(img_res, cmap='gray')
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("Translation")
        self.canvas4.draw()

    def quantificationC(self):
        Z = image.reshape((-1, 3))
        Z = np.float32(Z)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 3
        comp, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        img_res = center[label]
        img_res = img_res.reshape((image.shape))
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        plt.imshow(cv2.cvtColor(img_res, cv2.COLOR_BGR2RGB))
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("quantification classification C")
        self.canvas4.draw()
    def quantificationg(self):
        Z=imnb.ravel()
        Z = np.float32(Z)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 3
        comp, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        img_res = center[label]
        img_res = img_res.reshape((imnb.shape))
        self.figure.clear()
        plt.rcParams['axes.facecolor'] = '#E5E8E8'
        plt.imshow(img_res,cmap='gray')
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("quantification classification G")
        self.canvas5.draw()
    def quantification(self):
        self.quantificationC()
        self.quantificationg()

    def medianC(self):
            img = image

            k = 2  # où le nombre de segmenent = 2^k

            img2 = remplacer_valeurs_clr_v2(img, k)

            self.figure.clear()
            plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            plt.xlabel("width")
            plt.ylabel("height")
            plt.title("quantification median C")
            self.canvas4.draw()
    def medianG(self):
            img = imnb

            k = 5  # où le nombre de segmenent = 2^k

            img2 = remplacer_valeurs_nvg(img, k).reshape((img.shape))

            self.figure.clear()
            plt.imshow(img2, cmap='gray')
            plt.xlabel("width")
            plt.ylabel("height")
            plt.title("quantification median G ")
            self.canvas5.draw()
    def Median(self):
            self.medianC()
            self.medianG()

    def uniformeC(self):
        img = image
        h, w, c = img.shape

        img2 = uniforme_clr(img, h, w, c, 32)
        self.figure.clear()
        plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title(" uniforme_clr")
        self.canvas4.draw()
    def uniformeG(self):
        img = imnb
        h, w = img.shape
        img2 = uniforme_nvg(img, h, w, 32)
        self.figure.clear()
        plt.imshow(img2, cmap='gray')
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("uniforme_nvg ")
        self.canvas5.draw()
    def uniforme(self):
        self.uniformeC()
        self.uniformeG()

    def etiquetage(self):
        # Convertir l'image en niveaux de gris
        image_gris = image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Binariser l'image en utilisant un seuillage adaptatif
        _, image_binaire = cv2.threshold(image_gris, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Appliquer l'étiquetage en composantes connexes
        nb_labels, etiquettes = cv2.connectedComponents(image_binaire)

        # Créer une couleur aléatoire pour chaque composante connexe (sauf l'arrière-plan)
        couleurs = []
        for i in range(nb_labels):
            if i == 0:
                # Ignorer l'arrière-plan (étiquette 0)
                couleurs.append((0, 0, 0))
            else:
                # Générer une couleur aléatoire pour les autres composantes connexes
                couleur = np.random.randint(0, 255, size=3)
                couleurs.append(tuple(couleur.tolist()))

        # Créer une image colorée étiquetée
        image_couleur = np.zeros_like(image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                etiquette = etiquettes[i, j]
                image_couleur[i, j] = couleurs[etiquette]
        self.figure.clear()
        plt.imshow(cv2.cvtColor(image_couleur, cv2.COLOR_BGR2RGB))
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title(" Etiquetage")
        self.canvas4.draw()



    def impot(self):
        global im2
        # charger la vidéo dans la variable cap
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 tutorials\Browse Files')
        im2=fname[0]
        global x
        x = time.time()
        self.Vedio()
        return im2

    def Vedio(self):
        cap = cv2.VideoCapture(im2)
        fps = cap.get(cv2.CAP_PROP_FPS)
        dely = int(1000 / fps)
        # boucle infinie
        while (True):
            # stoquer l'image issue de la vidéo à l'instant t dans la variable "frame"
            ret, frame = cap.read()
            # afficher l'image contenue dans "frame"
            cv2.imshow('output', frame)
            if cv2.waitKey(dely) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def extract_frame(self):
        k = time.time()
        t=k-x

        # Open the video file
        video = cv2.VideoCapture(im2)

        # Check if the video file was successfully opened
        if not video.isOpened():
            print("video file not opened")
            return

        # Calculate the frame index for the specific second
        # video.get(cv2.CAP_PROP_FPS) to calculate the fps of the video
        frame_index = int(video.get(cv2.CAP_PROP_FPS) * int(t))

        # Set the video's position to the frame index
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

        # Read the frame at the specified second
        ret, frame = video.read()

        # Check if the frame was successfully read
        if not ret:
            print("Error reading frame")
            video.release()
            return

        # Save the frame as an image file
        cv2.imwrite("./oo.jpg", frame)
        self.figure.clear()
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("Capteur ")
        self.canvas5.draw()

        # Release the video file
        video.release()

        print("Frame extracted successfully")



    def comress(self):
        img = imnb

        # Get the dimensions of the input image
        height, width = img.shape[:2]
        print(height, width)
        # Calculate the number of blocks in each dimension
        num_blocks_y = int(np.ceil(height / 8))
        num_blocks_x = int(np.ceil(width / 8))

        # Pad the image if necessary to make it divisible by 8
        padded_height = num_blocks_y * 8
        padded_width = num_blocks_x * 8
        padded_img = np.zeros((padded_height, padded_width), dtype=np.uint8)
        padded_img[:height, :width] = img

        # Divide the padded image into blocks of 8x8
        blocks = []
        for y in range(num_blocks_y):
            for x in range(num_blocks_x):
                block = padded_img[y * 8:(y + 1) * 8, x * 8:(x + 1) * 8]
                blocks.append(block)

        # Apply the DCT to each block
        dct_blocks = []
        for block in blocks:
            dct_block = cv2.dct(np.float32(block))
            dct_blocks.append(dct_block)

        # Define the quantization matrix
        quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                        [12, 12, 14, 19, 26, 58, 60, 55],
                                        [14, 13, 16, 24, 40, 57, 69, 56],
                                        [14, 17, 22, 29, 51, 87, 80, 62],
                                        [18, 22, 37, 56, 68, 109, 103, 77],
                                        [24, 35, 55, 64, 81, 104, 113, 92],
                                        [49, 64, 78, 87, 103, 121, 120, 101],
                                        [72, 92, 95, 98, 112, 100, 103, 99]])

        # Quantize the DCT coefficients of each block
        quantized_blocks = []
        for dct_block in dct_blocks:
            quantized_block = np.round(dct_block / quantization_matrix)
            quantized_blocks.append(quantized_block)

        # Save the compressed image as a binary file
        with open('compressed_image.bin', 'wb') as f:
            for quantized_block in quantized_blocks:
                np.array(quantized_block, dtype=np.int8).tofile(f)















        # Load the compressed image as a binary file
        with open('compressed_image.bin', 'rb') as f:
            compressed_data = np.fromfile(f, dtype=np.int8)

        # Get the dimensions of the compressed image
        num_blocks = len(compressed_data) // 64
        compressed_height = num_blocks * 8
        compressed_width = 8

        # Reconstruct the quantized DCT coefficients of each block
        quantized_blocks = []
        for i in range(num_blocks):
            quantized_block = np.reshape(compressed_data[i * 64:(i + 1) * 64], (8, 8))
            quantized_blocks.append(quantized_block)

        # Define the quantization matrix
        quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                        [12, 12, 14, 19, 26, 58, 60, 55],
                                        [14, 13, 16, 24, 40, 57, 69, 56],
                                        [14, 17, 22, 29, 51, 87, 80, 62],
                                        [18, 22, 37, 56, 68, 109, 103, 77],
                                        [24, 35, 55, 64, 81, 104, 113, 92],
                                        [49, 64, 78, 87, 103, 121, 120, 101],
                                        [72, 92, 95, 98, 112, 100, 103, 99]])

        # Reconstruct the DCT coefficients of each block
        dct_blocks = []
        for quantized_block in quantized_blocks:
            dct_block = quantized_block * quantization_matrix
            dct_blocks.append(dct_block)

        # Apply the inverse DCT to each block
        blocks = []
        for dct_block in dct_blocks:
            block = cv2.idct(np.float32(dct_block))
            blocks.append(block)

        # Reconstruct the padded image from the blocks
        padded_img = np.zeros((compressed_height, compressed_width), dtype=np.uint8)
        for i, block in enumerate(blocks):
            y = i // (compressed_width // 8)
            x = i % (compressed_width // 8)
            padded_img[y * 8:(y + 1) * 8, x * 8:(x + 1) * 8] = block

        # Crop the padded image to its original size
        img = padded_img[:height, :width]

        # Show the reconstructed image

        self.figure.clear()
        plt.style.use('seaborn-dark')
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.xlabel("width")
        plt.ylabel("height")
        plt.title("decomp ")
        self.canvas5.draw()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Import image"))
        self.pushButton_2.setText(_translate("MainWindow", "Histogramme"))
        self.pushButton_3.setText(_translate("MainWindow", "Histogramme cumulé"))
        self.pushButton_4.setText(_translate("MainWindow", "Histogramme normalisé"))
        self.pushButton_5.setText(_translate("MainWindow", "L\'inversion d\'histogram"))
        self.pushButton_6.setText(_translate("MainWindow", "Segmentation"))
        self.label.setText(_translate("MainWindow", "MIN"))
        self.label_2.setText(_translate("MainWindow", "MAX"))
        self.pushButton_7.setText(_translate("MainWindow", "Egalisation"))
        self.pushButton_8.setText(_translate("MainWindow", "Expansion dynamique"))
        self.pushButton_9.setText(_translate("MainWindow", "Translation"))
        self.pushButton_10.setText(_translate("MainWindow", "Quantification"))
        self.pushButton_11.setText(_translate("MainWindow", "Median"))
        self.pushButton_12.setText(_translate("MainWindow", "Uniforme"))
        self.pushButton_13.setText(_translate("MainWindow", "Import vedio"))
        self.pushButton_14.setText(_translate("MainWindow", "Capteur"))
        self.pushButton_15.setText(_translate("MainWindow", "Etiquetage"))
        self.pushButton_16.setText(_translate("MainWindow", "comp-decom"))








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
