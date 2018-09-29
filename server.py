#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time
import struct

def printHex(title, data):
	if not data or len(data) == 0:
		print '(empty)'
		return

	buf = ''
	if title and len(title) > 0:
		buf += title + ' '
	n = len(data)
	buf += '(len:%d)' % (n)

	for i in range(n):
		buf += ' %d:0x%s' % (i, data[i].encode('hex'))
	print buf

def processClient(cs, addr):
	print 'accept client %s:%s' % addr

	while True:
		try:
			recvBuf = cs.recv(4096)
			if not recvBuf:
				break
			printHex('recv', recvBuf)
			cs.send('\x06')
		except:
			print 'recv error'
			break

	cs.close()
	print 'close client %s:%s' % addr

port = 2252
print 'listening on port:', port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen(10)

while True:
	try:
		client, addr = server.accept()
		t = threading.Thread(target=processClient, args=(client, addr))
		t.start()
	except:
		print 'error, exit'

server.close()
