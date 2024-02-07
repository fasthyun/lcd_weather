# for python3
# test sample 
_b1=b'\x020001,01MN,20231223170800,-3.8,-3.7,-3.8,52.1,52.7,51.7,1024.8,1024.8,1024.8,0.0,0.0,0.2,0.0,0.0,92.9,84.6,15.0\x03'
_b2=b'\x02-0.5,-15.6,0.0\x03\r\n'
"""
b'\x020001,01MN,20231223170800,-3.8,-3.7,-3.8,52.1,52.7,51.7,1024.8,1024.8,1024.8,0.0,0.0,0.2,0.0,0.0,92.9,84.6,15.0\x03'
b'\x02-0.5,-15.6,0.0\x03\r\n'
b'\x020001,01MN,20231223170900,-3.8,-3.8,-3.8,53.6,53.9,53.3,1024.8,1024.8,1024.8,0.0,0.0,0.2,0.0,0.0,76.7,70.5,15.0\x03'
b'\x02-0.5,-15.6,0.0\x03\r\n'
b'\x020001,01MN,20231223171000,-3.9,-3.8,-3.9,53.6,54.0,53.3,1024.8,1024.9,1024.8,0.0,0.0,0.2,0.0,0.0,90.6,98.7,15.0\x03'
b'\x02-0.5,-15.6,0.0\x03\r\n'
b'\x020001,01MN,20231223171200,-4.0,-3.9,-4.0,52.4,52.5,52.4,1024.9,1024.9,1024.9,0.0,0.0,0.2,0.0,0.0,105.3,107.2,15.0\x03'
b'\x02-0.5,-15.6,0.0\x03\r\n'
b'\x020001,01MN,20231223171300,-4.0,-4.0,-4.0,52.3,52.4,52.3,1024.9,1025.0,1024.9,0.0,0.0,0.2,0.0,0.0,108.6,135.4,15.0\x03'
b'\x02-0.5,-15.6,0.0\x03\r\n'
"""

from socketserver import TCPServer,BaseRequestHandler
from datetime import datetime

from queue import Queue
""" 
 전부 문자열 ㄸㄸㄸㄸ
['0001', # 0  데이터로거 ID
 '01MN', # 1  자료 타입 
 '20231223170800',  # 2  날짜
 '-3.8', # 3  기온
 '-3.7', # 4
 '-3.8', # 5
 '52.1', # 6  습도?
 '52.7', # 7
 '51.7', # 8
 '1024.8', #9   기압
 '1024.8', #10
 '1024.8', #11
 '0.0', 
 '0.0',
 '0.2',   # 풍속인듯 !
 '0.0',
 '0.0',
 '92.9',  # ? 
 '84.6',  #18 풍향 360
 '15.0'] #19 로거 전압 
"""

def parse_KWEATHER(_bytes):    
    if _bytes[0] == 0x02 :
        if _bytes[-1] == 0x03:            
            _list=_bytes[1:-1].decode().split(',')
            if len(_list) == 20:
                print("DEBUG: 20 field found", _list[1])
                _dict={
                '_id' :_list[0],
                '_type' :_list[1],
                '_datetime':datetime.strptime(_list[2],"%Y%m%d%H%M%S"),
                'temp_now' : _list[3],
                'temp2' : _list[4],
                'temp3' : _list[5],
                'humidity':_list[6],
                'hum2' : _list[7],
                'hum3' : _list[8],
                'press1' :_list[9],
                'press2' : _list[10],
                'press3' : _list[11],
                '_none1' : _list[12],
                '_none2' : _list[13],
                'wind_speed_x' : _list[14],
                'wind_speed' : _list[15],
                '_none4' : _list[16],
                'wind_direction_x' : _list[17],
                'wind_direction' :_list[18],
                '_voltage': _list[19]}
                return _dict
            elif len(_list) == 11 :
                print("DEBUG: 11 field found", _list[1])
                _dict={
                '_id' :_list[0],
                '_type' :_list[1],
                '_datetime':datetime.strptime(_list[2],"%Y%m%d%H%M%S"),
                'temp_now' : _list[3],
                'humidity':_list[4],
                'pressure' :_list[5],
                'unknown1' : _list[6],
                'unknown2' : _list[7],   
                'wind_speed' : _list[8],  
                'wind_direction' :_list[9],
                '_voltage': _list[10]}
                return _dict        
            if len(_list) == 3:
                _dict={}
                print("DEBUG: 3 field found ",_bytes) 
                _dict={
                'temp_high_day' :_list[0],
                'temp_low_day' :_list[1],               
                'rainfall_yesterday' : _list[2]}
                return _dict
            else:
                print("DEBUG: unknown length frame =",len(_list),_bytes)
        
    print("unknown data =",_bytes)
    return {}

class HandleClass(BaseRequestHandler):    
    def setup(self):
        pass
    def handle(self):
        sock=self.request 
        _data=sock.recv(1024)
        self.put(_data)    
        print("DEBUG: transfered from : ", self.client_address,type(self.request),len(_data))        
        while True:
            _frame = self.getFrame()
            if _frame is not None:
                self.server.que.put(_frame)
            else:
                break 
        
    def finish(self):
        print("finished!")

class Server(TCPServer):
    def __init__(self):
        TCPServer.__init__(self,("0.0.0.0",2000),HandleClass)
        self.timeout=0.1
        self.que=Queue() # temporaly!!!
        self.buffer=bytes(0)
    
    def put(self,new_bytes):
        #self.buffer = self.buffer + new_bytes
        self.buffer += new_bytes
        
    def getFrame(self):
        _bytes=self.buffer        
        s=_bytes.find(0x02);
        if s == -1 :            
            return None 
        e=_bytes.find(0x03);
        if e == -1 :             
            return None        
        if s < e:
            self.buffer= _bytes[e:]
            return _bytes[s:e] # safer        
        # something wrong !  end < start  so , 
        self.buffer = _bytes[s:] # delete until start
        return None 
                
        
#server.serve_forever(0.1)
#server.handle_request()
#server.server_close()


if __name__ =="__main__" :    
    c=parse_KWEATHER(_b1)
    print(c)
    c=parse_KWEATHER(_b2)
    print(c)
    pass
print("__pacakge__",__package__)
