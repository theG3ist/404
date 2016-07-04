#!/usr/bin/python
from socket import *
from codecs import decode
from threading import Thread
from time import ctime

BUFSIZE = 1024
CODE = 'ascii'
class ClientHandler(Thread):
	def __init__(self, client, record):
		Thread.__init__(self)
		self._client = client
		self._record = record

	def run(self):
		self._name = decode(self._client.recv(BUFSIZE), CODE)
		self._client.close()

#ip = socket.gethostbyname('172.16.176.156')
ip = '172.16.176.156'
port = 31337
ADDR = (ip, port)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(10)

while True:
	print('Waiting for connection . . .')
	client, address = server.accept()
	print('... connected from:', address)
	handler = ClientHandler(client, record)
	handler.start()