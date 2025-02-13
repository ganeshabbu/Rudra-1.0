from email import encoders
from email.mime.base import MIMEBase

import requests
from email.mime.multipart import MIMEMultipart

import pyautogui
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import datetime
import os
import cv2
from email.mime.text import MIMEText
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import instaloader
import time
import PyPDF2
from newsapi import NewsApiClient
from PyPDF2.errors import PdfReadError
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from RudraUi import Ui_RudraUi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Rudra 1.0. How may I help you?")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ganeshabbu03@gmail.com', 'elci ckka smrz qhaz')
    server.sendmail('ganeshabbu03@gmail.com', to, content)
    server.close()
def news():
    client = NewsApiClient(api_key='4c82a3e2aeda42f69e9685576a99a2d9')
    top_headlines = client.get_top_headlines()
    articles = top_headlines['articles']
    for article in articles:
        speak(article['title'])
        speak(article['description'])
class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        self.TaskExecution()
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_thrshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said:{query}")
        except Exception as e:
            speak("Say that again please..")
            return "None"
        return query
    def TaskExecution(self):
        wishme()
        while True:
            self.query = self.takecommand().lower()
            if 'open notepad' in self.query:
                path = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(path)
            elif 'close notepad' in self.query:
                speak("closing notepad")
                os.system("taskkill /f /im notepad.exe")
            elif 'open command prompt' in self.query:
                os.system("start cmd")
            elif 'close command prompt' in self.query:
                speak("closing command prompt")
                os.system("taskkill /f /im cmd.exe")
            elif 'open camera' in self.query:
                 cap = cv2.VideoCapture(0)
                 while True:
                     ret, img = cap.read()
                     cv2.imshow('webcam', img)
                     k = cv2.waitKey(50)
                     if k==27:
                         break
                 cap.release()
                 cv2.destroyAllWindows()
            elif 'play music' in self.query:
                music_dir = "C:\\AE\\Adobe After Effects 2022\\Download"
                songs = os.listdir(music_dir)
                #ss = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song ))
                        break
            elif'stop music' in self.query:
                os.system("taskkill /f /im vlc.exe")
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif 'open code' in self.query:
                codePath = "C:\\Users\\ganes\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'open pycharm' in self.query:
                codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1.3\\bin\\pycharm64.exe"
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            elif 'open facebook' in self.query:
                webbrowser.open("www.facebook.com")
            elif 'stackoverflow' in self.query:
                webbrowser.open("www.stackoverflow.com")
            elif 'open google' in self.query:
                speak('sir,what should search on google?')
                cm = self.takecommand().lower()
                webbrowser.open(f"https://www.google.com/search?q={cm}")
            elif 'send message' in self.query:
                current_hour = datetime.datetime.now().hour
                current_minute = datetime.datetime.now().minute
                kit.sendwhatmsg("+919849827740", "this is testing protocol", current_hour, current_minute + 1)
            elif 'play song on youtube' in self.query:
                speak('sir,what should i play  on youtube?')
                cm = self.takecommand().lower()
                kit.playonyt(f"https://www.youtube.com/search?q={cm}")
            elif 'email' in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand()
                    if 'send a file' in self.query:
                        email = 'ganeshabbu03@gmail.com'
                        password = 'elci ckka smrz qhaz'
                        send_to_email = "broganesh93@gmail.com"
                        speak("what the content of this email sir!")
                        message = self.takecommand().lower()
                        speak("enter the file location for this email")
                        file_location = input("please enter the path here: ")
                        speak("please wait,I am sending this email")
                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = send_to_email
                        msg['Subject'] = "This is the subject of this email"
                        msg.attach(MIMEText(message, 'plain'))
                        with open(file_location, 'rb') as attachment:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f"attachment; filename= {file_location}")
                        msg.attach(part)
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        server.sendmail(email, send_to_email, msg.as_string())
                        server.quit()
                        speak("Email has been sent!")
                    else:
                        to = "brogranesh93@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend ganesh. I am not able to send this email")
            elif 'no thanks' in self.query:
                speak("thanks for using me sir,have a good day")
                sys.exit()
            elif 'set alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir = "C:\\AE\\Adobe After Effects 2022\\Download\\song"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
            elif 'tell me a joke' in self.query:
                speak(pyjokes.get_joke())
            elif 'shutdown system' in self.query:
                os.system("shutdown /s /t 1")
            elif 'restart system' in self.query:
                os.system("shutdown /r /t 1")
            elif 'log off system' in self.query:
                os.system("shutdown /l")
            elif 'sleep system' in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")
            elif 'tell me news' in self.query:
                speak("please wait sir, fetching the latest news")
                news()
            elif 'where am i' in self.query:
                try:
                    ip = get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    state = geo_data['region']
                    country = geo_data['country']
                    speak(f"sir,you are currently in {city} city of {state} state of {country} country")
                except Exception as e:
                    speak("sorry sir,Due to network issue i'm unable to find your current location")
                    pass
            elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                speak("enter the username correctly..")
                name = input("username: ")
                webbrowser.open(f"https://www.instagram.com/{name}")
                speak(f"here is the profile of {name}")
                time.sleep(5)
                speak("would you like to download profile pic of this account?")
                condition = self.takecommand().lower()
                if 'download' in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("profile pic has been downloaded successfully into our main folder sir !")
                else:
                    pass
            elif 'weather' in self.query:
                speak("please wait sir !,I'm fetching the weather report")
                report = get('https://wttr.in/?format=3').text
                speak(report)
            elif 'take screenshot' in self.query:
                speak("sir, tell me name of the screenshot file")
                name = self.takecommand().lower()
                speak('please wait sir,I am taking screenshot ')
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("screenshot has been taken sir,check your main folder")
            elif 'read pdf' in self.query:
                file_path = speak(input("enter the path of pdf:"))
                try:
                    with open(file_path, 'rb') as book:
                        pdfReader = PyPDF2.PdfReader(book)
                        # Use len(reader.pages) instead of reader.numPages
                        num_pages = len(pdfReader.pages)
                        speak(f"Total number of pages: {num_pages}")
                        speak("tell me upto which page you want to read:")
                        pg = int(input("page number: "))
                        # Extract text from each page
                        for page in pdfReader.pages[pg-1:pg]:
                            speak(page.extract_text())
                except PdfReadError as e:
                    speak(f"Error reading PDF:{e}")
                except FileNotFoundError:
                    speak("File not found. Please check the file path.")
                except Exception as e:
                    speak("An unexpected error occurred")
            elif 'hide all files' in self.query or 'hide this folder' in self.query or 'disable hiding files' in self.query:
                speak("please tell me whether you want to hide all files or disable hiding files")
                condition = self.takecommand().lower()
                if 'yes hide' in condition:
                    os.system("attrib +h /s /d")
                    speak("all files are hidden sir")
                elif 'disable hiding files' in condition:
                    os.system("attrib -h /s /d")
                    speak("hiding files has been disabled sir")
                elif 'leave it' in condition:
                    speak("ok sir")

            elif 'play song on spotify' in self.query:
                speak('Sir, what should I play on Spotify?')
                cm = self.takecommand().lower()
                kit.playons(f"https://open.spotify.com/search/{cm}")

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.thread = None
        self.ui = Ui_RudraUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

        # Set up the timer and connect it to the showTime method
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)  # Connect the timer to showTime
        self.timer.start(1000)  # Start the timer to trigger every second

    def startTask(self):
        self.thread = MainThread()
        self.thread.start()  # Start the thread

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = now.toString(Qt.ISODate)  # Use 'now' for the date
        self.ui.textBrowser.setText(f"{label_date} {label_time}")  # Display both date and time
class MyClass(QObject):
    my_signal = pyqtSignal()  # Correctly defining a signal

    def __init__(self):
        super().__init__()
        self.my_signal.connect(self.my_slot)  # Connecting the signal to a slot

    def my_slot(self):
        print("Signal received!")
app = QApplication(sys.argv)
Rudra = Main()
Rudra.show()
exit(app.exec_())