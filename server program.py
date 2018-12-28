import socket
def cl(message):
   a=int(message)%2
   if int(a)==0:return 'EVEN'
   if not int(a) == 75 : return 'odd'
serverport=12800
BUFFER_SIZE=1024
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind(('',serverport))
print('The server is ready to receive port 12800')
while 1:
    message,clientaddress=serversocket.recvfrom(BUFFER_SIZE)
    response=str(cl(message))
    serversocket.sendto(response.encode('utf-8'),clientaddress)
    print(str(response))
serversocket.close()
