import sys
#from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
#from filedialog import fileDialog
from RFgui import Ui_Dialog

class initGUI(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.btn_Browserdata.clicked.connect(self.browserdata)
        self.btn_browsercamera.clicked.connect(self.browsercamera)
        
                
    def browserdata(self):
        fname, _ = QFileDialog.getOpenFileName()  # Eu não sei pq o _ mas sem ele, ele retorna 2 valores, seria o _ uma variavel?
        self.txt_Data.setPlainText(str(fname))

        #dire = self.sourceDir
        #filters = "Text files (*.txt);;Images (*.png *.xpm *.jpg)"
        #selected_filter = "Images (*.png *.xpm *.jpg)"
        #files = QFileDialog.getOpenFileName(self, " File dialog ","", filters, selected_filter)


        #options = QFileDialog.Options()
        #fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        #fileDialog.initUI()
        #print("oi")

    def browsercamera(self):
        fname, _ = QFileDialog.getOpenFileName()  # Eu não sei pq o _ mas sem ele, ele retorna 2 valores, seria o _ uma variavel?
        self.txt_Camera.setPlainText(str(fname))

        # objFilediago = QFileDialog
        # fname,_= objFilediago.getOpenFileName()

        # options = QFileDialog.Options()
        #fname = QFileDialog.getOpenFileName()
        #print(fname)

        # options = QFileDialog.Options()
        # fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        # fileDialog.initUI()
        # print("oi")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = initGUI(dialog)

    dialog.show()
    sys.exit(app.exec_())
