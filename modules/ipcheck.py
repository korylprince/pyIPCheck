#tester function
def runscan(db):
    import asyncore
    import socket
    import time

    class Socket(asyncore.dispatcher):
        description = ""
        ip_address = ""
        port = ""
        status = False 
    
        def __init__(self, description,ip_address,port):
            asyncore.dispatcher.__init__(self)
            self.description = description
            self.ip_address = ip_address
            self.port = port
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connect( (ip_address, int(port)) )
    
        def handle_connect(self):
            self.status = True
            self.close()
    
    serversockets = []
    switchsockets = []
    
    for s in db(db.services.type == "server").select():
        sock = Socket(s.description,s.ip_address,s.port)
        serversockets.append(sock)
    for s in db(db.services.type == "switch").select():
        sock = Socket(s.description,s.ip_address,s.port)
        switchsockets.append(sock)
    
    time.sleep(.1)
    asyncore.loop(1,count=2)
    
    serversockets.sort(key=lambda x:x.description)
    switchsockets.sort(key=lambda x:x.description)
    return serversockets,switchsockets

#alternating classes
import itertools
alternate = itertools.cycle(('odd','even'))
