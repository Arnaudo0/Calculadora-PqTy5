from typing import Text
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from math import sqrt
import math
import locale
locale.setlocale(locale.LC_ALL, 'es_AR')
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        #Seteamos los operadores
        self.operador1 = 0
        self.operador2 = 0
        self.Rapt = 0
        #Seteamos el tipo de operación a realizar
        self.operacion = ""
        #Listeners de Eventos de los botones de los números
        self.boton1.clicked.connect(self.click_1)
        self.boton2.clicked.connect(self.click_2)
        self.boton3.clicked.connect(self.click_3)
        self.boton4.clicked.connect(self.click_4)
        self.boton5.clicked.connect(self.click_5)
        self.boton6.clicked.connect(self.click_6)
        self.boton7.clicked.connect(self.click_7)
        self.boton8.clicked.connect(self.click_8)
        self.boton9.clicked.connect(self.click_9)
        self.boton0.clicked.connect(self.click_0)
        self.Borrartodo.clicked.connect(self.DeletAll)
        self.Borrar.clicked.connect(self.Delet)
        self.Coma.clicked.connect(self.coma)
        #Listeners de Eventos de los botones de las operaciones
        self.suma.clicked.connect(self.sumar)
        self.igual.clicked.connect(self.resultado)
        self.resta.clicked.connect(self.restar)
        self.Potencia.clicked.connect(self.potenciar)
        self.Dividir.clicked.connect(self.dividir)
        self.Raiz.clicked.connect(self.raiz)
        self.multiplica.clicked.connect(self.multiplicar)
        self.backup.returnPressed.connect(self.teclado)

    def resultado(self):
            operador1 = self.Calculo.text()
            if (self.Rapt == 0):
                try:
                        ans = eval(operador1)
                        self.Calculo.setText(str(ans))
                except:
                        self.Calculo.setText("Error")
            elif (self.Rapt == 1) :
                global num
                num = pow(num,float(self.Calculo.text()))
                self.Calculo.setText(str(num))
                    

    #Eventos de asignación de valores al label
    def sumar(self):
        self.Rapt = 0
        text = self.Calculo.text()
        self.Calculo.setText(text + "+")
    
    def restar(self):
        self.Rapt = 0
        text = self.Calculo.text()
        self.Calculo.setText(text + "-")

    def dividir(self):
        self.Rapt = 0
        text = self.Calculo.text()
        self.Calculo.setText(text + "/")

    def multiplicar(self):
        self.Rapt = 0
        text = self.Calculo.text()
        self.Calculo.setText(text + "*")

    def potenciar(self):
        self.Rapt = 1
        global num
        num = float(self.Calculo.text())
        self.Calculo.setText("")
    
    def coma(self):
        text = self.Calculo.text()
        self.Calculo.setText(text + ".")
            
    def raiz(self):
        global num
        num = float(self.Calculo.text())
        num = sqrt(num)
        self.Calculo.setText(str(num))

    def teclado(self):
        operador1 = self.backup.text()
        try:
            ans = eval(operador1)
            ans = format(ans,',d').replace(",",".")
            self.Calculo.setText(str(ans))
        except:
            self.Calculo.setText("Error")

    def click_1(self):
        self.Calculo.setText(self.Calculo.text() + "1")

    def click_2(self): 
        self.Calculo.setText(self.Calculo.text() + "2")
    
    def click_3(self): 
        self.Calculo.setText(self.Calculo.text() + "3")
    
    def click_4(self): 
        self.Calculo.setText(self.Calculo.text() + "4")
    
    def click_5(self): 
        self.Calculo.setText(self.Calculo.text() + "5")
    
    def click_6(self): 
        self.Calculo.setText(self.Calculo.text() + "6")
    
    def click_7(self): 
        self.Calculo.setText(self.Calculo.text() + "7")
    
    def click_8(self): 
        self.Calculo.setText(self.Calculo.text() + "8")
    
    def click_9(self): 
        self.Calculo.setText(self.Calculo.text() + "9")
    
    def click_0(self): 
        self.Calculo.setText(self.Calculo.text() + "0")

    def Delet(self): 
        text = self.Calculo.text() 
        self.Calculo.setText(text[:len(text)-1])

    def DeletAll(self):
        self.Calculo.clear()
        self.expr = ''
        self.resultfinished = False
        self.operador1= 0
        self.operador2= 0

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()