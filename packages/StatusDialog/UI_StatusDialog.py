# Form implementation generated from reading ui file '.\StatusDialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StatusDialog(object):
    def setupUi(self, StatusDialog):
        StatusDialog.setObjectName("StatusDialog")
        StatusDialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        StatusDialog.resize(219, 163)
        StatusDialog.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.closeButton = QtWidgets.QPushButton(parent=StatusDialog)
        self.closeButton.setGeometry(QtCore.QRect(70, 110, 75, 23))
        self.closeButton.setObjectName("closeButton")
        self.muteButton = QtWidgets.QPushButton(parent=StatusDialog)
        self.muteButton.setGeometry(QtCore.QRect(20, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.muteButton.sizePolicy().hasHeightForWidth())
        self.muteButton.setSizePolicy(sizePolicy)
        self.muteButton.setText("")
        self.muteButton.setIconSize(QtCore.QSize(32, 32))
        self.muteButton.setObjectName("muteButton")
        self.conversionButton = QtWidgets.QCheckBox(parent=StatusDialog)
        self.conversionButton.setGeometry(QtCore.QRect(90, 50, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conversionButton.setFont(font)
        self.conversionButton.setIconSize(QtCore.QSize(20, 20))
        self.conversionButton.setObjectName("conversionButton")

        self.retranslateUi(StatusDialog)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog)

    def retranslateUi(self, StatusDialog):
        _translate = QtCore.QCoreApplication.translate
        StatusDialog.setWindowTitle(_translate("StatusDialog", "Dialog"))
        self.closeButton.setText(_translate("StatusDialog", "Close"))
        self.conversionButton.setText(_translate("StatusDialog", "PitchConversion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatusDialog = QtWidgets.QDialog()
    ui = Ui_StatusDialog()
    ui.setupUi(StatusDialog)
    StatusDialog.show()
    sys.exit(app.exec())
