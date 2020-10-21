
import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia 
import webbrowser
import time
import urllib.request
import urllib.parse
import re
import webbrowser as wb
import subprocess, sys
import random
import  os
import wave
from playsound import playsound
import multiprocessing
import pywhatkit
import mydictionary
import os,random,sys,time
import giveNews as n
from selenium import webdriver
import fromMyServer as fs
from bs4 import BeautifulSoup

# import mytodo


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate', 150)
engine.runAndWait() 
myList=['xyx','Girishwani','abc','Bot']


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else: 
        speak("Good Evening!")
    
    speak("Hello sir,How may I help you?")

     
def takeCommand():
    '''It takes micro-phone  input and returns the string output'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # speak("I am Listening  : ")
        print('\nListening for the command....\n')  
        r.pause_threshold =1
        audio = r.listen(source)
        time.sleep(2)

        try:
            print('\nRecognising the command....\n')
            query=r.recognize_google(audio)
            #print('qqqqq :   ',query)
        except Exception as e:
            print(e)
            print("Please say again")
    return query   

def searchWiki(query):
    speak('searching wikipedia')
    query=query.replace("wikipedia","")
    # print('sdsfdsgdsgfd    ',query)
    result=wikipedia.summary(query,sentences=2)
    speak("According to wikipedia")
    print(result)
    speak(result)

def youTube(query):
        '''
        if 'search' in query:
            query=query.replace('youtube',"").replace('search','').replace('on',"")
            words=query.split()            
            if len(words)!=0:
                print(words)
               link = "http://www.youtube.com/results?search_query="
                for i in words:
                    link += i + "+"
                time.sleep(1)
                    # =================
                    # x=""
                    # i=0
                    # for i in words:
                    #     x+=i
                    # print(x)
                    # html_content = urllib.request.urlopen("http://www.youtube.com/results?"+x)
                    # search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                    # print(search_results)
                    # print("http://www.youtube.com/watch?v=" + search_results[0])
                    # webbrowser.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))
                webbrowser.open(link[:-1])
            else:
                webbrowser.open("https://youtube.com")
        elif 'open' in query:
            webbrowser.open("https://youtube.com")
        '''
        speak('opening youtube')
        link = "http://www.youtube.com/results?search_query=iiec+rise"
        webbrowser.open(link[:])
        

def playMusic():
    # musicloc='home/sanket/Desktop//0.mp3'
        path='/home/sanket/Desktop/music/'
        files=os.listdir(path)
        print(files)
        d=random.choice(files)
            # print(d)
            # os.system(path+d)
            # playsound()
        print(d)
        p = multiprocessing.Process(target=playsound, args=(f'/home/sanket/Desktop/music/{d}',))
        p.start()
        input("press ENTER to stop playback")
        p.terminate()
        
def sendWhatsapp():
    import whatsapp 
    speak("To whome:")
    toWhome=takeCommand().title()
    print(f'To Whome : {toWhome} ')
    speak("What message to send ")
    message=takeCommand().lower()
    print(f'Messsage : {message}')
    if (toWhome in myList):
        res=whatsapp.Mywhatsapp(toWhome,message).SendMessage()
        if res:
            speak(f"Message Send successfully to {toWhome}")
        else: 
            speak("No user found, Message not send")
    else: 
        speak("No user found, Message not send")     

def giveTime():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is  {strTime}")


def giveMeaning(query):
    query=query.replace('meaning','').replace('of','').replace('word','').replace('the','')
    meaning=mydictionary.Mydictionary(query).giveMeaning()
    speak(f"Meaning is {meaning}")
    time.sleep(2)
  
def todo():
    f = open("t1.txt", "r")
    f1=open("temp.txt","r")
    x=str(f.read())
    print(str(f1.read()))   
    speak(x)  
     
     
def linkedIn():
    
    browser=webdriver.Chrome()
    browser.get("https://www.linkedin.com/login")
    speak("Linked In is Opening")
    time.sleep(3)
    speak("Required   Credentials")
    time.sleep(2)
    x=takeCommand().lower()
    time.sleep(2)
    
    elementID=browser.find_element_by_id('username')
    elementID.send_keys('')

    elementID=browser.find_element_by_id('password')
    elementID.send_keys('')
    elementID.submit()
    
    speak("okay , Authentication successfull")
    time.sleep(2)
    speak("Do you have any task for me to do on linked in ")
    time.sleep(2)
    search=takeCommand().lower()
    time.sleep(2)
    speak('searching and opening  iiec rise page ')
    searchElement=browser.find_element_by_xpath('//*[@id="ember16"]/input')
    searchElement.send_keys('iiec rise')
    searchElement=browser.find_element_by_xpath('//*[@id="ember14"]/div[2]').click()
    browser.get('https://www.linkedin.com/company/iiec-rise/')
    time.sleep(2)
    speak("Done with searching and opening the linked in page")
    time.sleep(1)
    speak("Any thing else for me")
    time.sleep(2)
    xx=takeCommand().lower()
    speak('okay  closing linked in')
    time.sleep(1)    
    browser.close()
    
       
def Controller():
    print('-----------------------------Welcome-----------------------------')
    
    wishMe()
    while True :
        time.sleep(5)
        speak("Do you have any new task for me ")
        time.sleep(1)
        newtask=takeCommand().lower()
        if 'yes' in newtask:
            speak("okay, please tell me the task")
            time.sleep(3)
            
            query=takeCommand().lower()
            
            if 'iiec' in query:
                print('open youtube and search iiec rise ')
            else:
                print(query)
            
            if 'wikipedia' in query:
                searchWiki(query)
            
            elif 'open terminal' in query:
                speak("opening terminal ") 
                os.system("gnome-terminal")
                
                
            elif 'create' in query and ('folder' in query or 'directory' in query):
                speak("Name of the directory")
                
                dirname=takeCommand().lower()
                print(f'Directory Name: {dirname}')
                
                speak("In which location") 
                loc=takeCommand().title()
                print(f'location: {loc}')
                try:
                    os.mkdir(f'/home/sanket/{loc}/{dirname}')
                    speak("Directory created")

                except Exception as e:
                    speak("Directory not Created")
                    
            elif 'youtube' in query and ('open' in query or 'search' in query)  : 
                # webbrowser.open("https://youtube.com")
                youTube(query)

            elif 'play music' in query:
                playMusic()
            
                
            elif 'whatsapp' in query and  ('send' in query or 'message' in query):
                sendWhatsapp()
            
            elif 'the time' in query:
                giveTime()
        
            elif 'meaning' in query:
                giveMeaning(query)
        
            elif 'exit' in query:
                speak("Thank you sir. Have a nice day")
                break
            elif 'list' in query: 
                todo()

            elif 'linked' in query: 
                linkedIn()
            
            elif 'command' in query:
                
                while True:
                    fs.FromServer()
                    time.sleep(1)
                    speak('Do you want to run any other command on server ')
                    time.sleep(3)
                    temp=takeCommand().lower()
                    if 'yes' in temp:
                        continue
                    else: 
                        break
          
            elif 'news' in query: 
                n.GiveNews()
        else: 
            speak("Thank you sir ,have a nice day!")
            break
        
