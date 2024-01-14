from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QPainter, QImage, QPen, QColor
from PyQt5.QtCore import QTimer,QRect
from PyQt5 import uic
#from PyQt5 import rc
import weather_rc

form_ui, widget_class = uic.loadUiType('lcd_weather.ui')


#화면을 띄우는데 사용되는 Class 선언
class MainWindow(widget_class,form_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

class AWidget(QWidget) :
    def __init__(self, parent) :
        super().__init__( parent)
        print("parent= ", parent)
        self.title1="awidget"
        self.basecolor={"title":QColor(0,100,200) ,"value": None}
        pass
    def changeSize(self):
        gw=self.parentWidget().width()
        gh=self.parentWidget().height()
        #print("w=",w," , h=",h)
        #self.setBaseSize(w/3,h/3)
        self.resize(gw/3,gh/3)
        self.move(0,0)
        _height=self.height()        
        _width=self.width()
        _d=_height/10
        _f=self.font()
        _f.setPixelSize(_height/3 - _d)
        self.setFont(_f)
        
    def showEvent(self,event):
        print("show parent = " ,self.parentWidget())
        #w=self.parentWidget().width()
        #h=self.parentWidget().height()
        #self.setBaseSize(w/3,h/3)
        pass
    def paintEvent(self, event):
        self.changeSize()
        _height=self.height()        
        _width=self.width()
        
        #print("w=",w," , h=",h)
        p = QPainter()
        p.begin(self)
        # 그리기 함수의 호출 부
        #qp.drawImage(self.rect(),self.image_bg,self.image_bg.rect())
        #p.draw#Rect(self)
        
        p.setBrush(QColor(255, 255, 255))
        p.setPen(QPen(QColor(60, 60, 60), 3))
        p.drawRect(self.rect())
        
        p.setPen(QPen(QColor(10, 10, 10), 1))
                
        p.setBrush(self.basecolor['title'])
        p.setPen(QPen(QColor(10, 10, 10), 1))
        
        r=QRect(0,0,_width,_height/3)
        p.drawRect(0,0,_width,_height/3)
        
        p.setPen(QPen(QColor(255, 255, 255), 1))
        p.drawText(r,0,self.title1)
        p.end()
         
    
class MyWindow(QMainWindow):         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")
        self.setGeometry(830, 100, 700, 700)
        self.setStyleSheet(" ")        
        self.image_bg=QImage(":/image/sky_blue2.jpeg"); 
        self.aw=AWidget(self)
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # 그리기 함수의 호출 부분      
        qp.drawImage(self.rect(),self.image_bg,self.image_bg.rect())
        qp.end()
        
app = QApplication([])
#widget = uic.loadUi('lcd_weather.ui')

def timeout():
    pass

timer = QTimer()
timer.start(1000)
timer.timeout.connect(timeout)

#window = widget #MainWindow()
window = MyWindow()
"""window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
"""
window.show()
app.exec()
del app 


