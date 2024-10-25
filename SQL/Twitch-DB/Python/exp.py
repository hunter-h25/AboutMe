import socket               # Import socket module
import time

listOfFiles = ['April 2021.csv','peakviewers.csv','twitchjan.csv','twitchfeb.csv','twitchmar.csv','twitchapr.csv','twitchmay.csv','twitchjun.csv','twitchjul.csv','twitchaug.csv','twitchsep.csv','twitchoct.csv','twitchnov.csv','twitchdec.csv']

file = listOfFiles[1]

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.


s.connect(('172.16.1.212', port))
f = open(file,'rb')
print('Sending...')
l = f.read(1024)
while (l):
    print('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print("Done Sending")
s.shutdown(socket.SHUT_WR)
print(s.recv(1024))
s.close()
