#plantilla para trabajar con una aplicación basada en QDialog

#importar el archivo python generado desde QtDesigner, reemplazar <clase_ui> por el nombre correcto
from IMC import * 

#clase nueva para construir el dialogo 
# reemplazar <nombreAppClase> por un nombre adecuado a la funcionalidad de la aplicación
class IMC (QtWidgets.QDialog, Ui_dlgIMC):  # reempazar <Ui_Dialog> por el nombre de la clase creada en la ui
    #constructor de la clase
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        #completar el constructor con las inicializaciones necesarias
        self.txtPeso.setText("")  #setText establece un valor 
        self.txtAltura.setText("")
        self.txtCat.setText("")
        self.txtIMC.setText("")
        self.btnCalcular.clicked.connect(self.calcular) # Evento click del botom
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)

    def calcular(self):
        peso= float(self.txtPeso.text()) #Text lee el valor en la caja de texto
        altura= float(self.txtAltura.text())
        imc= peso/ (altura*altura)
        self.txtIMC.setText("{0:.2f}".format(imc))

        if imc < 18.5:
            self.txtCat.setText("Bajo peso")
            self.txtCat.setStyleSheet("txtCat {background-color: red;}")
        elif imc <= 24.9:
            self.txtCat.setText("Normal")
            self.setStyleSheet("txtCat {background-color: yellow;}")
        elif imc <= 29.9:
            self.txtCat.setText("Sobrepeso")
            self.setStyleSheet("txtCat {background-color: yellow;}")
        else:
            self.txtCat.setText("Obesidad")
            self.setStyleSheet("txtCat {background-color: yellow;}")

    def limpiar(self):
        self.txtPeso.setText("")  #setText establece un valor 
        self.txtAltura.setText("")
        self.txtCat.setText("")
        self.txtIMC.setText("")
    
    def salir(self):
        app.closeAllWindows()




# punto de inicio del programa
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dlg = IMC() # reemplazar <nombreAppClase> por el mismo nombre de clase anteriormente establecido
    dlg.show()
    app.exec_()