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
import whatsapp 
import mydictionary
class Controller:
    myList=['xyx','Girishwani','abc']
    def __init__(self):
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voices',self.voices[1].id)
        self.engine.setProperty('rate', 150)
        self.engine.runAndWait() 
        print('hereeeeeeeeee')

    def speak(self,audio):
        self.engine.say(self.audio)
        self.engine.runAndWait() 

    def wishMe(self):
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning!")
        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")
        else: 
            self.speak("Good Evening!")
        
        self.speak("Hello sir, I am your personal   assistant.How may I help you?")
        
    def takeCommand(self):
        '''It takes micro-phone  input and returns the string output'''
    
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold =1
            audio = r.listen(source)
            try:
                print('Recognizing...')
                query=r.recognize_google(audio)
                print(query)
            except Exception as e:
                print(e)
                print("Please say again")
        return query   
        
Controller().wishMe()