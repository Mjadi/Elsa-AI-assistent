# Importing Frameworks
import json, requests
from sys import exit
import sys
import time
import pyttsx3
import speech_recognition as sr
import datetime as dt
import webbrowser
import os
import random
import wikipedia
import pywhatkit as pwt
import cv2
import wolframalpha
import pyjokes
# from Dony import tati, main1
import pyautogui
from playsound import playsound
import PyPDF2
from time import sleep
import keyboard
import pygame
import smtplib
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI import Ui_Elsa

# Specifying owner and assistent

OWNER = "Mjadi"
ASSISTENT = "Elsa"

# Function @for_Bot


def sound():
    pygame.mixer.init()
    pygame.mixer.music.load('notification.mp3')
    pygame.mixer.music.play()
def say(x):

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.setProperty('voice', voices[1].id)
    engine.say(x)
    engine.runAndWait()


def take_order1():
    # print("Listening...")
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 4)
        clear()
        print("Listening...")
        audio = r.listen(source)
        

        try:
            # print("Recognizing...")
            text = r.recognize_google(audio, language = 'en-in')
            # text = text.lower()
            
            return str(text)

        except:
            pass

def r_seq(n):

    r_lines = random.choice(n)
    return r_lines

clear = lambda: os.system("cls")

def timer(t):
    t = int(t)
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

    said("countdown is over sir.")
    say("countdown is over sir.")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email', 'password')
    server.sendmail('your email', to, content)
    server.close()

def o_file():
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    os.startfile(FILEBROWSER_PATH)

def wishMe():
    hour = dt.datetime.now().hour
    if hour >= 0 and hour < 12:
        say("Good Morning sir.")
        print("Good Morning sir.")
    elif hour >= 12 and hour < 18:
        say("Good Afternoon sir.")
        print("Good Afternoon sir.")
    else:
        say("Good Evening sir.")
        print("Good Evening sir.")


def tati():
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   CITY = "Jamshedpur"
   API_KEY = "3293fe8d766fd6e130bff0cb37360399"
   # upadting the URL
   URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
   # HTTP request
   response = requests.get(URL)
   # checking the status code of the request
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      # getting temperature
      temperature = main['temp']
      # getting the humidity
      humidity = main['humidity']
      # getting the pressure
      pressure = main['pressure']
      # weather report
      report = data['weather']
      # print(f"{CITY:-^30}")
      said(f"""Sir the current Temperature is {int(temperature - 273.15)} degree celcius, Humidity in air is {humidity}%
and the Weather_Status at your place is {report[0]['description']}.""")
      say(f"""Sir the current Temperature is {int(temperature - 273.15)} degree celcius, Humidity in air is {humidity}%
and the Weather Status at your place is {report[0]['description']}.""")
      
   else:
      # showing the error message
      print("Could not fetch the weather details of the specified location.")



def sleep1():
    while(True):
        try:
                        
                            sleep_command = take_order1()
                            if 'wake up' in sleep_command:
                                print(f"{OWNER} said: {sleep_command}")
                                jb4 = ["Back to work.", "Ready for your next command."]
                                jb5 = r_seq(jb4)
                                say(jb5)
                                print(jb5)
                                break

                            else:
                                print("")
        except Exception as f:
                        print(" ")
                        pass

def rem():
    with open('C:\\Users\\DELL\\Desktop\\Reminders\\Reminder-1.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        # print(last_line)
        return last_line
def said(c):
    print(f"{ASSISTENT} said: {c}")
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.main34()

    def take_order(self):

        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration = 4)
            sound()
            # playsound('elsaS.wav', True)
            print("Listening...")
            
            audio = r.listen(source)

            try:
                print("Recognizing...")
                text = r.recognize_google(audio, language = 'en-in')
                text = text.lower()
                if 'elsa' in text:
                        text1 = text.replace('elsa', '')
                        return text1
                else:
                        return text

            except:
                text = None
    def main34(self):
        wishMe()
        while(True):
            try:
                self.text = self.take_order()
                
                def r_Request():
                    print(f'{OWNER} said: {self.text}')

                def main1():
                    try:
                            said('Advance elsa activated, You can now ask any computational questions.')
                            say('Advance elsa activated, You can now ask any computational questions.')
                            while(True):
                                question = self.take_order()
                                print(f"{OWNER} said: {question}.")
                                if 'exit' in question or 'quit' in question:
                                    said("Changing back to default mode.")
                                    say("Changing back to default mode.")
                                    break

                                else:
                                    app_id = 'YJ8V6K-Y3TVKJP7TL'
                                    client = wolframalpha.Client('R2K75H-7ELALHR35X')
                                    res = client.query(question)
                                    answer = next(res.results).text
                                    say(f"The answer to your question is {answer}.")
                                    said(f"The answer to your question is {answer}.")
                    except Exception as e2:
                                k2 = "Say that again please."
                                say(k2)
                                said(k2)
                    
                # avoid()
                if 'about' in self.text or 'who are you' in self.text or 'who created you' in self.text:
                    # avoid
                    details = f"Hi i am {ASSISTENT} an artificial intelligence assistence created by mister {OWNER} who is the most genius person on earth!"
                    r_Request()
                    say(details)
                    # print(details)
                    said(details)

                elif 'open whatsapp' in self.text:
                    # avoid
                    r_Request()
                    say("Opening whatsapp for you sir!")
                    # print("Opening whatsapp for you sir!")
                    said("Opening whatsapp for you sir!")
                    url = 'web.whatsapp.com'
                    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)

                elif 'open youtube' in self.text:
                    # avoid
                    r_Request()
                    say("Opening youtube for you sir!")
                    # print("Opening youtube for you sir!")
                    said("Opening youtube for you sir!")
                    url = 'youtube.com'
                    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)

                elif 'news' in self.text:
                    # avoid
                    r_Request()
                    # # avoid
                    h7 = "Getting you the top headlines from the times of india."
                    # print(h7)
                    said(h7)
                    say(h7)
                    url = 'timesofindia.indiatimes.com/home/headlines'
                    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)

                elif 'open github' in self.text:
                    # avoid
                    r_Request()
                    
                    say("As you say sir!")
                    # print("As you say sir!")
                    said("As you say sir!")
                    url = 'github.com'
                    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)

                elif 'screenshot' in self.text:
                    # avoid
                    r_Request()
                    
                    fr = random.randint(1, 100)
                    fr1 = str(fr)
                    myScreenshot = pyautogui.screenshot()
                    lr = "Taking a screenshot.."
                    # print(lr)
                    said(lr)
                    say(lr)
                    myScreenshot.save(f'C:\\Users\\DELL\\Videos\\Captures\\NewScreenshot_{fr1}.png')

                elif 'open spotify' in self.text or 'play music' in self.text:
                    # avoid
                    r_Request()
                    # print("Enjoy your music sir.")
                    said("Enjoy your music sir.")
                    say("Enjoy your music sir.")
                    s_Path = 'C:\\Users\\DELL\\AppData\\Roaming\\Spotify\\Spotify.exe'
                    os.startfile(s_Path)
                    time.sleep(4)
                    keyboard.press_and_release('space')
                    
                elif 'search for' in self.text:
                    # avoid
                    r_Request()
                    self.text2 = self.text.replace("search for", "")
                    url = self.text2
                    l9 = f"Here are some results of{url}.."
                    said(l9)
                    say(l9)
                    pwt.search(url)

                elif 'hold' in self.text or 'sleep' in self.text:
                    # avoid
                    r_Request()
                    fg = ["As you say sir.", "You can call me any time."]
                    fg2 = r_seq(fg)
                    say(fg2)
                    said(fg2)
                    sleep1()

                elif 'date' in self.text:
                    #    now = dt.datetime.now()
                    # avoid
                    r_Request()
                    now = dt.date.today()
                    now = f'Todays date is {now}'
                    said(now)
                    say(now)

                elif 'time' in self.text:
                    # avoid
                    r_Request()
                    xav = dt.datetime.now()
                    current_time = xav.strftime("%H:%M:%S")
                    said(f"Current Time = {current_time}")
                    say(f'{current_time} is the time right now.')

                elif 'reminder' in self.text:
                    # avoid
                    r_Request()
                    vc = "What you want me to remember."
                    say(vc)
                    said(vc)
                    kw = self.take_order()
                    # fm = dt.datetime.now()
                    with open(f"C:\\Users\\DELL\\Desktop\\Reminders\\Reminder-1.txt", "a")as v:
                        # v.write(f"{dt.datetime.today()}\n")
                        v.write(f"\n{dt.datetime.now()}:-\n{kw}.")
                    say('Done!')
                    said('Done!')

                elif 'remember' in self.text:
                    # avoid
                    r_Request()
                    say("Getting the reminders..")
                    said("Here are some things you told me to remember with respective to its time.\n")
                    with open(f"C:\\Users\\DELL\\Desktop\\Reminders\\Reminder-1.txt", "r")as v1:
                        v2 = v1.read()
                    print(v2)
                    x69 = rem()
                    say(f"The last thing you told me to remember was {x69}")
                    said(f"The last thing you told me to remember was {x69}")
                
                elif 'open code' in self.text:
                    # avoid
                    r_Request()
                    x5 = "Opening visual studio code.."
                    said(x5)
                    say(x5)
                    c_path = 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                    os.startfile(c_path)

                elif 'take a photo' in self.text or 'click a photo' in self.text:
                    # avoid
                    r_Request()
                    o4 = random.randint(1, 100)
                    c7 = "Say cheese!"
                    said(c7)
                    say(c7)
                    videoCaptureObject = cv2.VideoCapture(0)
                    result = True
                    while(result):
                        ret,frame = videoCaptureObject.read()
                        cv2.imwrite(f"C:\\Users\\DELL\\Pictures\\Camera Roll\\NewPicture{str(o4)}.jpg", frame)
                        result = False
                    videoCaptureObject.release()
                    cv2.destroyAllWindows()

                elif 'calculations' in self.text or 'maths' in self.text:
                    # avoid
                    r_Request()
                    main1()

                elif 'wikipedia' in self.text:
                    # avoid
                    r_Request()
                    # ignore(text)
                    text0 = self.text.replace('wikipedia', '')
                    d = f"Searching {text0} on wikipedia.."
                    said(d)
                    say(d)
                    r = wikipedia.summary(text0, sentences = 2)
                    print(r)
                    say(r)

                elif 'joke' in self.text:
                    # avoid
                    r_Request()
                    g1 = pyjokes.get_joke()
                    said(g1)
                    say(g1)

                elif 'weather' in self.text or 'temperature' in self.text:
                    # avoid
                    r_Request()
                    tati()

                elif 'open chrome' in self.text or 'open google' in self.text:
                    # avoid
                    r_Request()
                    f = "Opening google chrome."
                    said(f)
                    say(f)
                    os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")

                elif 'open reddit' in self.text:
                    # avoid
                    r_Request()
                    m3 = "Opening reddit."
                    said(m3)
                    say(m3)
                    url = 'reddit.com'
                    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)

                elif 'on youtube' in self.text:
                    # avoid
                    r_Request()
                    # ignore(text)
                    self.text1 = self.text.replace('on youtube', '')
                    f2 = f"Opening {self.text1} on youtube.."
                    said(f2)
                    say(f2)
                    pwt.playonyt(self.text)

                elif 'open zoom' in self.text:
                    # avoid
                    r_Request()
                    r5 = "Opening zoom meetings as per request."
                    said(r5)
                    say(r5)
                    os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

                elif 'open file manager' in self.text or 'open file explorer' in self.text:
                    # avoid
                    r_Request()
                    s9 = "Opening file manager."
                    said(s9)
                    say(s9)
                    o_file()

                elif 'open gmail' in self.text or 'open email' in self.text or 'open mail' in self.text:
                    # avoid
                    r_Request()
                    m3 = "Opening gmail."
                    said(m3)
                    say(m3)
                    url = 'mail.google.com'
                    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)

                elif 'repeat after me' in self.text or 'say what i say' in self.text:
                    # avoid
                    jkw = "Speak what you want me to repeat."
                    said(jkw)
                    say(jkw)
                    hk1 = self.take_order()
                    said(hk1)
                    say(hk1)

                elif 'read pdf' in self.text:
                    # avoid
                    r_Request()
                    # creating a pdf file object
                    pdfFileObj = open('sample.pdf', 'rb')
                    
                    # creating a pdf reader object
                    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                    
                    # printing number of pages in pdf file
                    said(f"The number of pages are {pdfReader.numPages}.")
                    say(f"The number of pages are {pdfReader.numPages}.")
                    say("Which page you want me to read.")
                    pageask = int(input("Enter the page number: "))
                    pageask2 = pageask - 1
                    
                    # creating a page object
                    pageObj = pdfReader.getPage(pageask2)
                    
                    # extracting text from page
                    print(pageObj.extractText())
                    say(pageObj.extractText())
                    
                    # closing the pdf file object
                    pdfFileObj.close()

                elif 'countdown' in self.text:
                    # avoid
                    r_Request()
                    dj = "For how much time sir."
                    say(dj)
                    said(dj)
                    dj1 = int(input("Enter the time in seconds: "))
                    timer(dj1)

                elif 'exit' in self.text or 'quit' in self.text:
                    # avoid
                    sxd = f"{OWNER} said: {self.text}"
                    print(sxd)
                    fj = ["I hope you had a great time.", "It was a pleasure working with you.", "Thank you for using me sir."]
                    fj1 = r_seq(fj)
                    say(fj1)
                    print(fj1)
                    break

                elif 'send a mail' in self.text:
                    # avoid
                    r_Request()
                    with open('mail.json')as p:
                        emails = json.load(p)
                    try:
                        say("What should I say?")
                        content = self.take_order()
                        said(f"{OWNER} said: {content}")
                        say("whome should i send")      
                        to = self.take_order()
                        to1 = emails.get(to)
                        said(f"Sent a mail to {to1}")
                        sendEmail(to1, content)
                        say("Email has been sent !")
                    except Exception as e:
                        print(e)
                        say("I am not able to send this email")
                else:
                    # error = "sorry can not react i am in development phase!"
                    # r_Request()
                    # say(error)
                    # said(error)
                    r_Request()
                    text5 = self.text.strip()
                    with open('talk.json')as g:
                        g1 = json.load(g)
                    try:
                        g2 = g1[text5]
                        # g3 = g2.strip(g2)
                        say(g2)
                        said(g2)
                    except:
                        said("Sorry,cannot help with that one.")

            except AttributeError as e:
                # said("Sorry didn't get that, I apologise for that.")
                # say("Sorry didn't get that, I apologise for that.")
                # pass
                print(e)

            except Exception as d:
                # pass
                print(d)

startexecution =MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Elsa()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Pictures/Saved Pictures/8871.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Pictures/Saved Pictures/oFTHu7E.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Pictures/Saved Pictures/f889323d87ae92dbd5da3b1193708dc3.gif")
        # self.ui.movie = QtGui.QMovie()
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Pictures/Saved Pictures/279b2e_194dd051fb5741e5b557654410e04d22_mv2.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Pictures/Saved Pictures/932fd00d9b43753061c47739f0cc777b.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Pictures/Saved Pictures/5da311e193e3d828e956ed010f95891b.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Pictures/Saved Pictures/1d735ad8eee8350adc96d50e1421ee6d.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        startexecution.start()



app = QApplication(sys.argv)
elsa = Main()
elsa.show()
exit(app.exec_())


