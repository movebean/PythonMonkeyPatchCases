from socket import *
import sys

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 32201))
sys.stdout = s.makefile('w', 0)
sys.stdin = s.makefile('r', 0)


print 'hello world'
sys.stdout.flush()
a = raw_input('text:')
print '---', a
