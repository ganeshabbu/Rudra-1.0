# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RudraUi(object):
    def setupUi(self, RudraUi):
        RudraUi.setObjectName("RudraUi")
        RudraUi.resize(1326, 936)
        self.centralwidget = QtWidgets.QWidget(RudraUi)
        self.centralwidget.setObjectName("centralwidget")

        # Label for background image
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 130, 1091, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/6448d91b06900e80a8730b07e9a2a329.jpg"))
        self.label.setObjectName("label")

        # Label for GIF
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 200, 501, 431))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.movie = QtGui.QMovie("../../../Downloads/1.gif")  # Path to your GIF
        self.label_2.setMovie(self.movie)
        self.movie.start()  # Start the GIF animation
        self.label_2.setObjectName("label_2")

        # Run button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(940, 620, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(16, 255, 12);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run_action)  # Connect to run_action

        # Exit button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1060, 620, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 17, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(RudraUi.close)  # Connect to close the application

        # Text browsers
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(830, 190, 131, 31))
        self.textBrowser.setStyleSheet("background:transparent;\n"
                                        "border-radius:none")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(980, 190, 141, 31))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
                                          "border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        RudraUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RudraUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1326, 26))
        self.menubar.setObjectName("menubar")
        RudraUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RudraUi)
        self.statusbar.setObjectName("statusbar")
        RudraUi.setStatusBar(self.statusbar)

        self.retranslateUi(RudraUi)
        QtCore.QMetaObject.connectSlotsByName(RudraUi)

    def retranslateUi(self, RudraUi):
        _translate = QtCore.QCoreApplication.translate
        RudraUi.setWindowTitle(_translate("RudraUi", "MainWindow"))
        self.pushButton.setText(_translate("RudraUi", "Run"))
        self.pushButton_2.setText(_translate("RudraUi", "Exit"))

    def run_action(self):
        # Define what happens when the Run button is clicked
        print("Run button clicked!")
        self.textBrowser.setText("Run action executed!")  # Example action
        self.textBrowser_2.setText("This is the second text browser.")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RudraUi = QtWidgets.QMainWindow()
    ui = Ui_RudraUi()
    ui.setupUi(RudraUi)
    RudraUi.show()
    sys.exit(app.exec_())