print "helo"
import socket

class potok(threading.Thread):
	def ClientTr():
		print "test 1"
		while True:
 			conn, addr = s.accept()
			print ("conn="+ str(conn) )
			print ("addr="+ str(addr) )
			for x in xrange(20):
				data=conn.recv(1024)
				print ("data="+ str(data) )
				if not data:
					print ("data not="+ str(data) )
					break
				else:
					if data == "close":
						print ("data close="+ str(data) )
						conn.close()
					else:
						print ("data else="+ str(data) )
						conn.send(data)
		conn.close()
		
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
#print ("s="+ str(s) )
#conn, addr = s.accept()
#print ("s=2="+ str(s) )
for x in xrange(10):
 potok(target=potok.ClientTr).start()
