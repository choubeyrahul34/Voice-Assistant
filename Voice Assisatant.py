from ntpath import join
from platform import system
import sys
from time import time
from typing import ContextManager, Text
import pyttsx3
import datetime
import requests
from requests.api import head
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
from requests import get
import pywhatkit
import pyjokes
import pyautogui
import instaloader
import PyPDF2
from wikipedia import exceptions


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishme():
    hour = datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    speak("I am Your Voice Assistant 'Robert' . Please tell me How Can I help You")

def takeCommand():
    # it takes microphone input from the user and returns string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
      #  r.energy_threshold = 4000
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please..")
        return "none"
    return query


# making send email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'password')
    server.sendmail('choubeyrahul34@gmail.com', to, content)
    server.close()

def news():
    news_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a9fe95a9dea447feb1cdc45902a04a89'
    main_page = requests.get(news_url).json
    articles = main_page["articles"]
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")



 # function to read the pdf   
def pdf_reader():
    speak("Enter the path and file name with .pdf extension")
    path_pdf = input("Enter the path and file name with .pdf extension")
    book = open(path_pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this pdf is {pages}")
    speak("Sir, Please enter the page I have to read")
    pg = int(input("Enter the page number"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    print(text)
    speak(text)


if __name__=="__main__":
    wishme()
    

    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'notepad' in query:
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f"Your IP address is {ip}")
            speak(f"Your IP address is {ip}")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Done sir,  please tell me next task")
        
        elif 'open google' in query:
            speak("sir, what should I search on google")
            gooq = takeCommand().lower()
            webbrowser.open(f"{gooq}")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'instagram profile' in query:
            speak("Sir, please enter the username correctly")
            insta_user = input("Enter username correctly : ")
            webbrowser.open(f"www.instagram.com/{insta_user}")
            speak(f"Sir, here is the instagram profile of {insta_user}")
            speak("Sir, would you like to download the profile Picture of this account")
            profile_pic = takeCommand().lower()
            if 'yes' in profile_pic:
                mod = instaloader.Instaloader()
                mod.download_profile(insta_user, profile_pic_only=True)
                speak("I am done sir")
            else:
                pass

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'play music' in query:
            music_dir = "E:\\Songs"
            song = os.listdir(music_dir)
            print(song)
            rd = random.choice(song)
            os.startfile(os.path.join(music_dir, rd))

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')

        elif 'send whatsapp message' in query:
            speak("To which You have to send the message, Please type the mobile number : ")
            mobile_no = '+91' + input("Enter mobile No.")
            speak("Enter a message which you want to send : ")
            #message_snd = input("Enter a message : ")
            message_snd = takeCommand().lower()
            speak("On which time you have to send the message : ")
            msg_time_hour = int(input("Enter hour : "))
            msg_time_min = int(input("Enter minutes : "))
            pywhatkit.sendwhatmsg(mobile_no, message_snd, msg_time_hour, msg_time_min)

        elif 'play song on youtube' in query:
            speak("Which song do you want to play  : ")
            song_name = takeCommand().lower()
            print(song_name)
            pywhatkit.playonyt(song_name)

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Now the time is {strtime}")
        
        # to open vs code
        elif 'open vs code' in query:
            codepath = 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)

        elif 'name' in query:
            speak("I am Your voice assistant and My name is Robert")

        elif 'how are' in query:
            speak("I am fine, please tell me how can I help you")
            
        
        # elif 'close notepad' in query:
        #     speak("ok sir, closing notepad")
        #     os.system("taskkill /f /im notepad.exe")

        # elif 'set alarm' in query:
        #     alarm_time = str(datetime.datetime.now().hour)
        #     if alarm_time == str(15:03:00):
        #         music_direc = "E:\\Songs"
        #         songssss = os.listdir(music_direc)
        #         rd = random.choice(songssss)
        #         os.startfile(os.path.join(music_direc, rd))

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'sleep' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            exit()
        
        elif 'shut down' in query:
            os.system("shutdown /s /t 5")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 5")

        elif 'window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
           # time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak("Sir, please tell me the name for the screenshot file")
            ss_name = takeCommand().lower()
            img = pyautogui.screenshot()
            img.save(f"{ss_name}.png")
            speak("I am done sir, The screenshot is save in our main folder, Please tell me my next task")


        elif 'where i am' in query or 'tell me my location' in query:
            speak("wait sir, let me check")
            try:
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
              #  state = geo_data['state']
                country = geo_data['country']
                print(f"sir i am not sure, but i think we are in {city} city of {country} country")
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                print(e)
                speak("Sorry sir, due to network problem I am not able to find where we are")
                pass

        elif 'read pdf' in query:
            pdf_reader()


        elif 'news' in query:
            news()
        
        
        # to send email using sendemail function
        elif 'send email' in query:
            try:
                speak("What should I speak ?")
                Content = takeCommand()
                send_add = input("Enter Email on which you want to send mail : ")
                to = send_add
                sendEmail(to, Content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry I am not able to send the email at this moment")

        elif 'exit' in query or 'leave me' in query:
            speak("Okay, I will go, Thank you for using me ")
            exit()