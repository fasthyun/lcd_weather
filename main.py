# work for pyhton3.6 
# because of 
#    1. ordreddict 
#    2. 
 
""" 

design 철학 : 
    화면표시부와 네트워크 데이타 처리부를 따로 분리하고 
    그렇게 분리하는게 낫겠다 싶었는데 
    잘 안되었다.

   * qlayout이나 qlabel을 사용하지 않은 이유는 여러가지 제한 사항이 발생해서 그렇다.
      예를 들어 qt stylesheet는 기능은 많지만 내가 필요로하는 속성의 제한, 직접  애니메이션  넣기 제한 등등 
   * 표시부 widget는 용도에따라 코드재사용을 할수있게 설계하였다.
   
"""

from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QPainter, QImage, QPen, QColor
from PyQt5.QtCore import QTimer,QRect , Qt
from PyQt5 import uic
#from PyQt5 import rc
import weather_rc

import time
from socket_server import startServer


form_ui, widget_class = uic.loadUiType('lcd_weather.ui')


#화면을 띄우는데 사용되는 Class 선언
class MainWindow(widget_class,form_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

class AWidget(QWidget) :
    def __init__(self, parent,_title) :
        super().__init__( parent)
        print("parent= ", parent)
        self.title1=_title
        self.basecolor={"title":QColor(0,100,200) ,"value": None}
        self.config={"title":"title","pos":(0,0)}
        self.move(0,0)      
        self.value=0
    def setValue(self,val):
        self.value=val
        #draw 
        
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
    
    def drawTitle(self, p ): # painter
        _height=self.height()        
        _width=self.width()
        d=_height/10
        p.setPen(QPen(QColor(10, 10, 10), 1))
        p.setBrush(self.basecolor['title'])
        p.setPen(QPen(QColor(10, 10, 10), 1))
        r=QRect(0,0,_width,_height/4)
        p.drawRect(0,0,_width,_height/4 )
        br=QRect(0,0,_width,_height/4 -d )
        p.setPen(QPen(QColor(255, 255, 255), 1))
        p.drawText(r,0,self.title1)
        
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
    
         
        self.drawTitle(p)
        y1=_height*1/4
        #y1=_height*1/4
        r=QRect(0,y1,_width,_height*3/4) 
        p.setPen(QPen(QColor(1, 1, 1), 1))
        p.drawText(r, Qt.AlignVCenter | Qt.AlignHCenter ,str(self.value))
        p.end()
         
    
class MyWindow(QMainWindow):         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")
        self.setGeometry(830, 100, 700, 700)
        self.setStyleSheet(" ")        
        self.image_bg=QImage(":/image/sky_blue2.jpeg"); 
        
        self.widgets=[]
        
        #for i in range(0,9):
        for k in items.keys():
            _it=items[k]
            _obj=AWidget(self,_it['title'])
            _it["object"]=_obj
            self.widgets.append(_obj)
            
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
        
def onAppQuit():
    if server is not None:
        server.server_close()
        print("close server!!")
    #if app is not None:
    #    app.closeAllWindows()
    
    
#orderedDictionary
items = {  
   "wind_direction" : { "name":"", "title" :"풍향", "object": None ,"class":AWidget },
   "wind_speed":{ "name":"", "title" :"풍속", "object": None ,"class": AWidget },
   "humidity": { "name":"", "title" :"습도", "object":  None ,"class":AWidget },
   "temp_now": { "name":"", "title" :"현재기온", "object":  None ,"class": AWidget ,"style": ""},
   "temp_high_aday":{ "name":"", "title" :"일최고기온", "object": None ,"class": AWidget },
   "temp_low_aday": { "name":"", "title" :"일최저기온", "object":  None ,"class": AWidget },
   "rainfall": { "name":"", "title" :"강수량", "object":  None ,"class": AWidget },
   "rainfall_yesterday": { "name":"humidity", "title" :"전일강수량", "object": None ,"class": AWidget },
   "snowfall": { "name":"", "title" :"강설량", "object": None ,"class": AWidget }
 }

server=startServer()
app = QApplication([])
#widget = uic.loadUi('lcd_weather.ui')
app.aboutToQuit.connect(onAppQuit)
def timeout():
    if server is not None:
        server.timeout=0.01
        server.handle_request()
    print("timeout!")
    #time.sleep(3)
    pass

timer = QTimer()
timer.start(1000)
timer.timeout.connect(timeout)


#window = widget #MainWindow()
window = MyWindow()
window.show()

app.exec()


del app 
del server
