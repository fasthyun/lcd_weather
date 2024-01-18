from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QPainter, QImage, QPen, QColor
from PyQt5.QtCore import QTimer,QRect , Qt
from PyQt5 import uic
#from PyQt5 import rc
import weather_rc

from socket_server import server


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
        self.config={"title":"title","pos":(0,0)}
        self.move(0,0)        
    
    def changeSize(self,d):
        gw=self.parentWidget().width()
        gh=self.parentWidget().height()
        #print("w=",w," , h=",h)
        #self.setBaseSize(w/3,h/3)
        self.resize(gw/3 -d ,gh/3 -d )    
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
        #self.changeSize()
        _height=self.height()        
        _width=self.width()
        
        #print("w=",w," , h=",h)
        p = QPainter()
        p.begin(self)        
        #qp.drawImage(self.rect(),self.image_bg,self.image_bg.rect())
        #p.draw#Rect(self)
        
        p.setBrush(QColor(255, 255, 255))
        p.setPen(QPen(QColor(60, 60, 60), 3))
        p.drawRect(self.rect())
        
        p.setPen(QPen(QColor(10, 10, 10), 1))
                
        p.setBrush(self.basecolor['title'])
        p.setPen(QPen(QColor(10, 10, 10), 1))
        
        r=QRect(0,0,_width,_height/4)
        p.drawRect(0,0,_width,_height/4)
        
        p.setPen(QPen(QColor(255, 255, 255), 1))
        p.drawText(r,0,self.title1)
        
        y1=_height*1/4
        #y1=_height*1/4
        r=QRect(0,y1,_width,_height*3/4) 
        p.setPen(QPen(QColor(1, 1, 1), 1))
        p.drawText(r, Qt.AlignVCenter | Qt.AlignHCenter ,self.title1)
        p.end()
         
    
class MyWindow(QMainWindow):         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")
        self.setGeometry(830, 100, 700, 700)
        self.setStyleSheet(" ")        
        self.image_bg=QImage(":/image/sky_blue2.jpeg"); 
        
        self.widgets=[]
        
        for i in range(0,9):
            self.widgets.append(AWidget(self))
            
        #self.
    def resizeEvent(self, e):
        print("resizeEvent=",e.size())
        size = e.size()
        _w=size.width()
        _h=size.height() - 40 
        
        d=_w/50;
        xw=(_w/3 - d); 
        xh=(_h/3 -d );
        x=d;
        y=d;
        for w in self.widgets:
            w.move(x,y)
            x= x + xw + d
            if x > _w: 
                x=d;
                y= y+ xh +d 
            w.changeSize(d)
            
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
      
        qp.drawImage(self.rect(),self.image_bg,self.image_bg.rect())
        qp.end()
        
app = QApplication([])
#widget = uic.loadUi('lcd_weather.ui')

def timeout():
    server.timeout=0.01
    server.handle_request()
    print("timeout!")
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
del server

