from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time



import datetime

import wikipedia
import webbrowser as wb
import random
import pyautogui
import psutil
import pyjokes

temp=0
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
my_list=["Can I help you in any other way","Do need my any further assistance","I always enjoy helpin you. Any more orders Sir"]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ttime():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("current time is")
    speak(Time)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning Sir")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir")
    elif hour>=16 and hour<=24:
        speak("Good Evening Sir")
    else:
        speak("Good night Sir")

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)

def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\main mini project\screenshot\ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)
def battery():
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    speak("percent")

def jokes():
    speak(pyjokes.get_joke())

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown -l")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()

    def run(self):
        self.JARVIS()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:

            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        engine.setProperty('rate',190)
        speak("Hi, I'm BotN. Nice to meet you! How may I help you")
        engine.setProperty('rate',170)
        while True:
            self.query = self.STT()
            if 'goodbye' in self.query or "offline" in self.query or "get lost" in self.query or 'good bye' in self.query:

                quit()





            elif "time" in self.query:
                ttime()
            elif "date" in self.query:
                date()


            elif "wikipedia" in self.query:
                speak("Great question! I'll find that out for you!")
                self.query=self.query.replace("wikipedia","")
                result=wikipedia.summary(self.query,sentences=2)
                speak(result)

            elif "search" in self.query:
                speak("What should i search?")
                path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                search=self.STT()+".com"
                wb.get(path).open(search)

            elif "log out" in self.query:
                logout()

            elif "shut down" in self.query or "shutdown" in self.query:
                shutdown()

            elif "restart" in self.query:
                restart()

            elif "speak in male voice" in self.query:
                engine.setProperty('voice',voices[0].id)
            elif "speak in female voice" in self.query:
                engine.setProperty('voice',voices[1].id)

            elif "remember that" in self.query:
                speak("What should I remember?")
                data=self.STT()
                speak("I stored your data")
                remember=open("data.txt","w")
                remember.write(data)
                remember.close()

            elif "do you know anything" in self.query or "do you remember anything" in self.query:
                remember=open("data.txt","r")
                speak("I completely understand what do you want. You said that"+remember.read())

            elif "screenshot" in self.query:
                screenshot()
                speak("Screenshot taken")
            elif "cpu" in self.query:
                cpu()
            elif "battery" in self.query:
                battery()
            elif "how was your day" in self.query:
                speak("I had a great day sir. What about you")
                self.query=self.STT()
                if "a good" in self.query or "fine" in self.query or "great" in self.query or "awesome" in self.query:
                    speak("Happy to hear that. What made you remember me")
                elif "not good" in self.query or "sad" in self.query or "tired" in self.query or "bad" in self.query:
                    speak("Sorry to hear that. Want to hear some jokes. LOL")
                    self.query=self.STT()
                    if "yes" in self.query or "sure" in self.query:
                        jokes()
                    elif "no" in self.query or "not in a mood" in self.query:
                        v=random.randint(0,2)
                        speak("OK")




            elif "how are you" in self.query:
                speak("Excellent sir")
            elif "hey" in self.query or "hello" in self.query:
                wish()

            elif "joke" in self.query:
                jokes()
            elif "speed" in self.query:
                speak("At what speed should I speak")
                c=int(self.STT())
                speak("OK")
                engine.setProperty('rate',c)
            v=random.randint(0,2)
            speak(my_list[v])















FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/qw.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()




        self.ts = time.strftime("%A, %d %B")


        Dspeak.start()

        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))

        self.ty = datetime.datetime.now().strftime("%H:%M:%S")
        
        self.label_2.setText("<font size=8 color='white'>"+self.ty+"</font>")
        self.label_2.setFont(QFont(QFont('Acens',8)))



app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
