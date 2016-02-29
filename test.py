print "helo"
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
conn, addr = s.accept()
print ("s")
print (conn+addr)
