import requests 
import myAssistant as a
import time
 
def FromServer():   
    time.sleep(2)
    a.speak('which command to run on the server')
    time.sleep(2)
    command=a.takeCommand().lower()
    time.sleep(2)
    
    r = requests.get(f'http://192.168.43.18/cgi-bin/main.py?cmd={command}') 
   
    a.speak("command running")
    
    temp=str(r.content)
    count=0
    if 'ubuntu' in temp:
        count=count+1

    if 'centos' in temp: 
        count=count+1
    
    if 'images' in command:
        print("------------Output from Web server--------------\n")
        print(f'Image Count : {count}')
        print(r.content) 
        a.speak(f"there are {count}    docker  images   at present      they  are  ubuntu         cent os  ") 
        
        time.sleep(3)

    else: 
       print("------------Output from Web server--------------\n")
       print(f'command : {command}')
       print(r.content) 
       a.speak(temp) 
       

        
