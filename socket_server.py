# for python3


from socketserver import TCPServer,BaseRequestHandler

def parse_KWEATHER(_bytes):
    
    pass

class HandleClass(BaseRequestHandler):
    #def __init__(
    def setup(self):
        pass
    def handle(self):
        sock=self.request 
        data=sock.recv(1024)
        print("happend?", self.client_address,type(self.request))
        #print(" ===>", data)
        
    def finish(self):
        print("finished!")


#server= TCPServer(("192.168.1.5",2000),HandleClass)
#server= TCPServer(("0.0.0.0",2000),HandleClass)
#server.serve_forever()

"""
2
happend? ('192.168.1.111', 56125) <class 'socket.socket'>
 ===> b'\x020001,01MN,20231223170800,-3.8,-3.7,-3.8,52.1,52.7,51.7,1024.8,1024.8,1024.8,0.0,0.0,0.2,0.0,0.0,92.9,84.6,15.0\x03'
finished!
happend? ('192.168.1.111', 56142) <class 'socket.socket'>
 ===> b'\x02-0.5,-15.6,0.0\x03\r\n'
finished!
happend? ('192.168.1.111', 56148) <class 'socket.socket'>
 ===> b'\x020001,01MN,20231223170900,-3.8,-3.8,-3.8,53.6,53.9,53.3,1024.8,1024.8,1024.8,0.0,0.0,0.2,0.0,0.0,76.7,70.5,15.0\x03'
finished!
happend? ('192.168.1.111', 56160) <class 'socket.socket'>
 ===> b'\x02-0.5,-15.6,0.0\x03\r\n'
finished!
happend? ('192.168.1.111', 56167) <class 'socket.socket'>
 ===> b'\x020001,01MN,20231223171000,-3.9,-3.8,-3.9,53.6,54.0,53.3,1024.8,1024.9,1024.8,0.0,0.0,0.2,0.0,0.0,90.6,98.7,15.0\x03'
finished!
happend? ('192.168.1.111', 56178) <class 'socket.socket'>
 ===> b'\x02-0.5,-15.6,0.0\x03\r\n'
finished!
happend? ('192.168.1.111', 56199) <class 'socket.socket'>
 ===> b'\x020001,01MN,20231223171200,-4.0,-3.9,-4.0,52.4,52.5,52.4,1024.9,1024.9,1024.9,0.0,0.0,0.2,0.0,0.0,105.3,107.2,15.0\x03'
finished!
happend? ('192.168.1.111', 56214) <class 'socket.socket'>
 ===> b'\x02-0.5,-15.6,0.0\x03\r\n'
finished!
happend? ('192.168.1.111', 56220) <class 'socket.socket'>
 ===> b'\x020001,01MN,20231223171300,-4.0,-4.0,-4.0,52.3,52.4,52.3,1024.9,1025.0,1024.9,0.0,0.0,0.2,0.0,0.0,108.6,135.4,15.0\x03'
finished!
happend? ('192.168.1.111', 56232) <class 'socket.socket'>
 ===> b'\x02-0.5,-15.6,0.0\x03\r\n'
finished!

"""
