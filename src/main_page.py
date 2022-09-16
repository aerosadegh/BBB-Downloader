# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 142)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, -1, 5, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.target_lbl = QtWidgets.QLabel(self.centralwidget)
        self.target_lbl.setObjectName("target_lbl")
        self.gridLayout.addWidget(self.target_lbl, 1, 0, 1, 1)
        self.sessionid_lbl = QtWidgets.QLabel(self.centralwidget)
        self.sessionid_lbl.setObjectName("sessionid_lbl")
        self.gridLayout.addWidget(self.sessionid_lbl, 0, 0, 1, 1)
        self.sessionid_led = QtWidgets.QLineEdit(self.centralwidget)
        self.sessionid_led.setObjectName("sessionid_led")
        self.gridLayout.addWidget(self.sessionid_led, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbar = QtWidgets.QProgressBar(self.centralwidget)
        self.pbar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pbar.setProperty("value", 0)
        self.pbar.setAlignment(QtCore.Qt.AlignCenter)
        self.pbar.setOrientation(QtCore.Qt.Horizontal)
        self.pbar.setObjectName("pbar")
        self.horizontalLayout.addWidget(self.pbar)
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setObjectName("download_btn")
        self.horizontalLayout.addWidget(self.download_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)
        self.sessionno_lbl = QtWidgets.QLabel(self.centralwidget)
        self.sessionno_lbl.setObjectName("sessionno_lbl")
        self.gridLayout.addWidget(self.sessionno_lbl, 0, 2, 1, 1)
        self.sessionno_sp = QtWidgets.QSpinBox(self.centralwidget)
        self.sessionno_sp.setMinimumSize(QtCore.QSize(53, 0))
        self.sessionno_sp.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sessionno_sp.setMinimum(1)
        self.sessionno_sp.setMaximum(1000)
        self.sessionno_sp.setObjectName("sessionno_sp")
        self.gridLayout.addWidget(self.sessionno_sp, 0, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.target_led = QtWidgets.QComboBox(self.centralwidget)
        self.target_led.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.target_led.setEditable(True)
        self.target_led.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.target_led.setObjectName("target_led")
        self.horizontalLayout_2.addWidget(self.target_led)
        self.browse_btn = QtWidgets.QToolButton(self.centralwidget)
        self.browse_btn.setMinimumSize(QtCore.QSize(32, 0))
        self.browse_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.browse_btn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.browse_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.browse_btn.setArrowType(QtCore.Qt.NoArrow)
        self.browse_btn.setObjectName("browse_btn")
        self.horizontalLayout_2.addWidget(self.browse_btn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout_BBB_Downloader = QtWidgets.QAction(MainWindow)
        self.actionAbout_BBB_Downloader.setObjectName("actionAbout_BBB_Downloader")
        self.actionLoad_Setting_from_Target = QtWidgets.QAction(MainWindow)
        self.actionLoad_Setting_from_Target.setCheckable(True)
        self.actionLoad_Setting_from_Target.setChecked(True)
        self.actionLoad_Setting_from_Target.setEnabled(True)
        self.actionLoad_Setting_from_Target.setObjectName("actionLoad_Setting_from_Target")
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionLoad_Setting_from_Target)
        self.menuAbout.addAction(self.actionAbout_BBB_Downloader)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BBB Downloader"))
        self.target_lbl.setText(_translate("MainWindow", "Target"))
        self.sessionid_lbl.setText(_translate("MainWindow", "Session ID"))
        self.download_btn.setText(_translate("MainWindow", "Download"))
        self.sessionno_lbl.setText(_translate("MainWindow", "# Session"))
        self.browse_btn.setText(_translate("MainWindow", "..."))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAbout_BBB_Downloader.setText(_translate("MainWindow", "About BBB Downloader"))
        self.actionLoad_Setting_from_Target.setText(_translate("MainWindow", "Load Setting from Target"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
