# for python3


from socketserver import TCPServer,BaseRequestHandler

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
    if _bytes[0] == 0x02 and _bytes[-1] == 0x03:
        print("ok")
        _list=_bytes[1:-1].decode().split(',')
        if len(_list) == 20:
            _id=_list[0]
            _type=_list[1]
            _datetime=_list[2]
            _temp1 = _list[3]
            _temp2 = _list[4]
            _temp3 = _list[5]
            _hum1 = _list[6]
            _hum2 = _list[7]
            _hum3 = _list[8]
            _press1 = _list[9]
            _press2 = _list[10]
            _press3 = _list[11]
            _none = _list[12]
            _none = _list[13]
            _windspeed = _list[14]
            _none = _list[15]
            _none = _list[16]
            _none = _list[17]
            _winddirection = _list[18]
            _voltage= _list[19]
        return _list
    return ""
    

class HandleClass(BaseRequestHandler):
    #def __init__(
    def setup(self):
        pass
    def handle(self):
        sock=self.request 
        _data=sock.recv(1024)
        print("happend?", self.client_address,type(self.request))
        #print(" ===>", data)
        parse_KWEATHER(_data)
        
    def finish(self):
        print("finished!")

def startServer():
    #server= TCPServer(("192.168.1.5",2000),HandleClass)
    server= TCPServer(("0.0.0.0",2000),HandleClass)
    server.timeout=0.1
    return server
#server.serve_forever(0.1)
#server.handle_request()
#server.server_close()


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


if __name__ =="main" :    
    c=parse_KWEATHER(_b1)
    pass
print("__pacakge__",__package__)