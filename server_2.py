
# first of all import the socket library 
import socket                
import os

# next create a socket object 
s = socket.socket()          
print "Socket successfully created"
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print "socket binded to %s" %(port) 
  
# put the socket into listening mode 
s.listen(5)      
print "socket is listening"            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print 'Got connection from', addr 

   recieved = c.recv(BUFFER_SIZE).decode()

   filename, filesize = recieved.split(SEPARATOR)

   filename = os.path.basename(filename)

   filesize = int(filesize)

#   print(s.recv(1024).decode("ascii"))
   with open('recieved_file','wb') as f:
       while True:
           print('receiving data')
           data = c.recv(BUFFER_SIZE)
           print('data=%s',(data))
           if not data:
               break
           f.write(data)
   f.close()
   # Close the connection with the client 
   c.close()
   s.close()
   break
