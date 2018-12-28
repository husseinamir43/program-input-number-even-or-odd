import socket
serverip='127.0.0.1'
serverport=12800
BUFFER_SIZE=1024
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
    message= input('input number call EVEN or odd :')

    client.sendto(message.encode('utf-8'),(serverip,serverport))
    response,address=client.recvfrom(BUFFER_SIZE)
    print (response.decode('utf-8'))

client.close()