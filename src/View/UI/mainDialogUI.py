# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\View\UI\mainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1000, 500)
        self.gridLayout_3 = QtWidgets.QGridLayout(mainWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.space_SpecialSummon = QtWidgets.QGridLayout()
        self.space_SpecialSummon.setObjectName("space_SpecialSummon")
        self.horizontalLayout.addLayout(self.space_SpecialSummon)
        self.space_CommonSummon = QtWidgets.QGridLayout()
        self.space_CommonSummon.setObjectName("space_CommonSummon")
        self.horizontalLayout.addLayout(self.space_CommonSummon)
        self.space_SSRSummon = QtWidgets.QGridLayout()
        self.space_SSRSummon.setObjectName("space_SSRSummon")
        self.horizontalLayout.addLayout(self.space_SSRSummon)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 1, 1, 6)
        self.btn_UpdateData = QtWidgets.QPushButton(mainWindow)
        self.btn_UpdateData.setObjectName("btn_UpdateData")
        self.gridLayout_3.addWidget(self.btn_UpdateData, 1, 1, 1, 1)
        self.btn_ExportExcel = QtWidgets.QPushButton(mainWindow)
        self.btn_ExportExcel.setCheckable(False)
        self.btn_ExportExcel.setChecked(False)
        self.btn_ExportExcel.setObjectName("btn_ExportExcel")
        self.gridLayout_3.addWidget(self.btn_ExportExcel, 1, 6, 1, 1)
        self.btn_GetToken = QtWidgets.QPushButton(mainWindow)
        self.btn_GetToken.setObjectName("btn_GetToken")
        self.gridLayout_3.addWidget(self.btn_GetToken, 0, 1, 1, 1)
        self.txt_UpdateTime = QtWidgets.QLabel(mainWindow)
        self.txt_UpdateTime.setObjectName("txt_UpdateTime")
        self.gridLayout_3.addWidget(self.txt_UpdateTime, 1, 2, 1, 1)
        self.btn_Hint = QtWidgets.QPushButton(mainWindow)
        self.btn_Hint.setObjectName("btn_Hint")
        self.gridLayout_3.addWidget(self.btn_Hint, 1, 3, 1, 1)
        self.btn_EnterToken = QtWidgets.QPushButton(mainWindow)
        self.btn_EnterToken.setObjectName("btn_EnterToken")
        self.gridLayout_3.addWidget(self.btn_EnterToken, 0, 2, 1, 1)
        self.txt_logger = QtWidgets.QLabel(mainWindow)
        self.txt_logger.setText("")
        self.txt_logger.setObjectName("txt_logger")
        self.gridLayout_3.addWidget(self.txt_logger, 0, 3, 1, 4)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Dialog"))
        self.btn_UpdateData.setText(_translate("mainWindow", "更新資料"))
        self.btn_ExportExcel.setText(_translate("mainWindow", "匯出Excel"))
        self.btn_GetToken.setText(_translate("mainWindow", "抓取token"))
        self.txt_UpdateTime.setText(_translate("mainWindow", "上次更新時間: 無"))
        self.btn_Hint.setText(_translate("mainWindow", "操作說明"))
        self.btn_EnterToken.setText(_translate("mainWindow", "手動輸入"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QDialog()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

