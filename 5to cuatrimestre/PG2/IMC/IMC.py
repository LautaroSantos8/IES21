# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IMC.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgIMC(object):
    def setupUi(self, dlgIMC):
        dlgIMC.setObjectName("dlgIMC")
        dlgIMC.resize(538, 216)
        dlgIMC.setSizeGripEnabled(False)
        dlgIMC.setModal(False)
        self.label = QtWidgets.QLabel(dlgIMC)
        self.label.setGeometry(QtCore.QRect(29, 14, 52, 16))
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(dlgIMC)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 26, 16))
        self.label_3.setObjectName("label_3")
        self.txtPeso = QtWidgets.QLineEdit(dlgIMC)
        self.txtPeso.setGeometry(QtCore.QRect(90, 15, 133, 20))
        self.txtPeso.setObjectName("txtPeso")
        self.txtAltura = QtWidgets.QLineEdit(dlgIMC)
        self.txtAltura.setGeometry(QtCore.QRect(90, 50, 133, 20))
        self.txtAltura.setObjectName("txtAltura")
        self.label_2 = QtWidgets.QLabel(dlgIMC)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 55, 16))
        self.label_2.setObjectName("label_2")
        self.btnCalcular = QtWidgets.QPushButton(dlgIMC)
        self.btnCalcular.setGeometry(QtCore.QRect(370, 40, 75, 23))
        self.btnCalcular.setAutoFillBackground(False)
        self.btnCalcular.setObjectName("btnCalcular")
        self.txtIMC = QtWidgets.QLineEdit(dlgIMC)
        self.txtIMC.setEnabled(True)
        self.txtIMC.setGeometry(QtCore.QRect(90, 90, 133, 20))
        self.txtIMC.setObjectName("txtIMC")
        self.txtCat = QtWidgets.QLineEdit(dlgIMC)
        self.txtCat.setEnabled(True)
        self.txtCat.setGeometry(QtCore.QRect(90, 130, 171, 20))
        self.txtCat.setObjectName("txtCat")
        self.label_4 = QtWidgets.QLabel(dlgIMC)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 47, 16))
        self.label_4.setObjectName("label_4")
        self.btnLimpiar = QtWidgets.QPushButton(dlgIMC)
        self.btnLimpiar.setGeometry(QtCore.QRect(370, 70, 75, 23))
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnSalir = QtWidgets.QPushButton(dlgIMC)
        self.btnSalir.setGeometry(QtCore.QRect(370, 110, 75, 23))
        self.btnSalir.setObjectName("btnSalir")

        self.retranslateUi(dlgIMC)
        QtCore.QMetaObject.connectSlotsByName(dlgIMC)

    def retranslateUi(self, dlgIMC):
        _translate = QtCore.QCoreApplication.translate
        dlgIMC.setWindowTitle(_translate("dlgIMC", "CALCULO DE IMC"))
        self.label.setText(_translate("dlgIMC", "Peso (kg): "))
        self.label_3.setText(_translate("dlgIMC", "IMC: "))
        self.label_2.setText(_translate("dlgIMC", "Altura (m): "))
        self.btnCalcular.setText(_translate("dlgIMC", "Calcular"))
        self.label_4.setText(_translate("dlgIMC", "Categoria"))
        self.btnLimpiar.setText(_translate("dlgIMC", "Limpiar"))
        self.btnSalir.setText(_translate("dlgIMC", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgIMC = QtWidgets.QDialog()
    ui = Ui_dlgIMC()
    ui.setupUi(dlgIMC)
    dlgIMC.show()
    sys.exit(app.exec_())
