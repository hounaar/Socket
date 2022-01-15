import socket            
s = socket.socket()        
print ("socket created")
port = 1111
s.bind(('', port))        
print ("socket binded to %s" %(port))
s.listen(5)    
print ("Waiting for connection")           
while True:
  c, addr = s.accept()    
  print ('Got connection from', addr )
  c.send('Connected'.encode())
  c.close()
  break
