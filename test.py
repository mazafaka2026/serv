print "helo"
import socket, threading
i=1
class potok(threading.Thread):
	def ClientTr():
		print "test 1"
		global i
		while True:
			data = conn.recv(1024)

			if not data:
				break
			else:
				print ("data")
				print(data)
			print ("s")
			print (s)
			if data == "close":
					conn.close()
			else:
					conn.send(data)
					break
		conn.close()
		print("schetchik")
		i=i+1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
for x in xrange (10):
    conn, addr = s.accept()
    while True:
        potok(target=potok.ClientTr).start()
        # threading.Thread(target=ClientTr).start()
        # threading.Thread(target=ClientTr).start()
        # threading.Thread(target=ClientTr).start()
        ##threading.Thread(target=ClientTr).start()
        # threading.Thread(target=ClientTr).start()
        # threading.Thread(target=ClientTr).start()
        # threading.Thread(target=ClientTr).start()
        # threading.Thread(target=ClientTr).start()
        # threading.Thread(target=ClientTr).start()
        # while True:
        # conn, addr = s.accept()
        # while True:
        # data=conn.recv(1024)
        # if not data:
        # break
        # else:
        # if data == "close":
        # conn.close()
        # else:
        # conn.send(data)
        # conn.close()
