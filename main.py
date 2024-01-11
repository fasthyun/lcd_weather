from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5 import uic
#from PyQt5 import rc
import weather_rc

form_ui, widget_class = uic.loadUiType('lcd_weather.ui')
#화면을 띄우는데 사용되는 Class 선언
class MainWindow(widget_class,form_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)



app = QApplication([])
widget = uic.loadUi('lcd_weather.ui')

def timeout():
    pass


timer = QTimer()
timer.start(1000)
timer.timeout.connect(timeout)

window = widget #MainWindow()
#window = MainWindow()
"""window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
"""
window.show()
app.exec()
del app 


