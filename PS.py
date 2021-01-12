import os
print("In Memories Of All Rained Flower ----<----***")
print("Hi This is PSexec utility Written by Aryan")
#os.system('cmd /k "psexec \\\\10.10.11.8 systeminfo"')
# print("hi "+name+"\`")
host = input("Enter the host address or IP :")#catch host address from User
try:
  response = os.system("ping -n 3 " + host)#try to ping host
except:
   print("Some Things Wrong")
if response == 0:
  print("Enter 1 To Run CMD remotely in client with your privilage")
  print("Enter 2 To Get System IP information")
  print("Enter 3 To Check system information remotely")
  print("Enter 4 To Disable Firewall Remotely")
  print("Enter 5 Enable Remote Desktop Remotly")
  cmd="psexec \\\\"+host+" -i -d -s cmd.exe"
  systeminfo="psexec \\\\"+host+" systeminfo"
  ipconfig="psexec \\\\"+host+" ipconfig /all"
  firewall="psexec \\\\"+host+" netsh advfirewall set allprofiles state off"
  remotedesktop='psexec \\\\'+host+' reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f'
  choise=input("Please Enter your Choise in Integer ")
  try:
   choise=int(choise) 
   def choose(choise):
        switcher={
                '1':os.system('cmd /k ' +cmd+"\""),
                '2':os.system('cmd /k ' +ipconfig+"\""),
                '3':os.system('cmd /k ' +systeminfo+"\""),
                '4':os.system('cmd /k ' +firewall+"\""),
                '5':os.system('cmd /k ' +remotedesktop+"\""),                
                    
                  }
        return switcher.get(choise,"Invalid Selection")
   
   choose(choise)   
  except:
   print("not an integer")

            
