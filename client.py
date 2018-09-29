#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = '127.0.0.1'
port = 2252

print 'Connect to:', host, port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('\x01\x02\xa1\xb1')
s.close()

