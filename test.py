print "helo"
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
print ("s="+ str(s) )
conn, addr = s.accept()
print ("s=2="+ str(s) )
while True:
  conn, addr = s.accept()
  print ("conn="+ str(conn) )
  print ("addr="+ str(addr) )
  for x in xrange(20):
	 	data=conn.recv(1024)
	 	print ("data="+ str(data) )
#	 	if not data:
#			break
#		else:
#			if data == "close":
#				conn.close()
#			else:
#				conn.send(data)
conn.close()
