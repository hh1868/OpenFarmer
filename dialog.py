# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 412)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(15, 25, 41, 16))
        self.label.setObjectName("label")
        self.edit_account = QtWidgets.QLineEdit(Dialog)
        self.edit_account.setGeometry(QtCore.QRect(60, 25, 116, 20))
        self.edit_account.setObjectName("edit_account")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 56, 16))
        self.label_2.setObjectName("label_2")
        self.spinbox_energy = QtWidgets.QSpinBox(Dialog)
        self.spinbox_energy.setGeometry(QtCore.QRect(250, 25, 57, 21))
        self.spinbox_energy.setMaximum(700)
        self.spinbox_energy.setProperty("value", 500)
        self.spinbox_energy.setObjectName("spinbox_energy")
        self.plain_text_edit = QtWidgets.QPlainTextEdit(Dialog)
        self.plain_text_edit.setGeometry(QtCore.QRect(0, 101, 701, 311))
        self.plain_text_edit.setReadOnly(True)
        self.plain_text_edit.setMaximumBlockCount(100)
        self.plain_text_edit.setObjectName("plain_text_edit")
        self.button_start = QtWidgets.QPushButton(Dialog)
        self.button_start.setGeometry(QtCore.QRect(555, 20, 131, 61))
        self.button_start.setObjectName("button_start")
        self.edit_proxy = QtWidgets.QLineEdit(Dialog)
        self.edit_proxy.setGeometry(QtCore.QRect(410, 25, 126, 20))
        self.edit_proxy.setObjectName("edit_proxy")
        self.checkbox_proxy = QtWidgets.QCheckBox(Dialog)
        self.checkbox_proxy.setGeometry(QtCore.QRect(330, 25, 71, 20))
        self.checkbox_proxy.setChecked(False)
        self.checkbox_proxy.setObjectName("checkbox_proxy")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(35, 65, 501, 20))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.checkbox_build = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_build.setChecked(True)
        self.checkbox_build.setObjectName("checkbox_build")
        self.checkbox_mining = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_mining.setChecked(True)
        self.checkbox_mining.setObjectName("checkbox_mining")
        self.checkbox_chicken = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_chicken.setChecked(True)
        self.checkbox_chicken.setObjectName("checkbox_chicken")
        self.checkbox_plant = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_plant.setChecked(True)
        self.checkbox_plant.setObjectName("checkbox_plant")
        self.checkbox_cow = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_cow.setChecked(True)
        self.checkbox_cow.setObjectName("checkbox_cow")
        self.checkbox_mbs = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_mbs.setChecked(True)
        self.checkbox_mbs.setObjectName("checkbox_mbs")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "农民世界助手"))
        self.label.setText(_translate("Dialog", "账号:"))
        self.edit_account.setText(_translate("Dialog", "uszym.wam"))
        self.label_2.setText(_translate("Dialog", "能量恢复:"))
        self.button_start.setText(_translate("Dialog", "启动"))
        self.edit_proxy.setText(_translate("Dialog", "127.0.0.1:10809"))
        self.checkbox_proxy.setText(_translate("Dialog", "启用代理"))
        self.checkbox_build.setText(_translate("Dialog", "建造"))
        self.checkbox_mining.setText(_translate("Dialog", "采集"))
        self.checkbox_chicken.setText(_translate("Dialog", "养鸡"))
        self.checkbox_plant.setText(_translate("Dialog", "种地"))
        self.checkbox_cow.setText(_translate("Dialog", "养牛"))
        self.checkbox_mbs.setText(_translate("Dialog", "会员"))
