import socket
import threading
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

portBroj = 40101
print("Port broj je ", portBroj)
s.bind(("localhost", portBroj))


if (portBroj == 40101):
	c = socket.socket()
	portBrojToConnectTo = int(input("Na koji port da se spojim? "))
	stringZaPoslati = str(input("Upišite string za poslati: "))
	time.sleep(5)
	c.connect(('localhost', portBrojToConnectTo))
	c.send(bytes(stringZaPoslati, "utf-8"))
	print("Poruka poslana")
	s.listen(2)
	print("waiting for connections...")
	while True:
		c2, addr = s.accept()
		name = c2.recv(1024).decode()
		print("Connected with ", addr, name)
		c2.close()
else:
	s.listen(2)
	zaPoslati = "prazno zasad"
	print("waiting for connections...")
	while True:
		c, addr = s.accept()
		name = c.recv(1024).decode()
		print("Connected with ", addr, name)
		zaPoslati = name
		c.close()
		break
		
	c = socket.socket()
	'''
	portBrojToConnectTo = int(input("Na koji port da se spojim? "))
	'''
	portBrojToConnectTo = 40103
	time.sleep(5)
	c.connect(('localhost', portBrojToConnectTo))
	c.send(bytes(zaPoslati, "utf-8"))






	