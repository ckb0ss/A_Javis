
import json
import smtplib
import time
import calendar as ca
from urllib.request import urlopen
import plyer
import pyautogui as pog
from win32 import win32gui
import pyttsx3
import instaloader
from bs4 import BeautifulSoup
import requests
from decouple import config
import pywhatkit as kit
import datetime as dt
import speech_recognition as sr
import senh as se
from random import choice
import os
import AppOpener as ao
import subprocess as sp
import webbrowser as wb
from pygame import mixer

# functions used to convert text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# to change the voice change the value of 0 to 1,2,3
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 200)
engine.setProperty('volume', 2)
# can change the name of user and bot
USER = config('USER', default="CHANDAN")
HOSTNAME = config('BOT', default="BLAZE")


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# If you want that listening start and pause using buttons activate it

'''
listening = False

def start_listening():
    global listening
    listening = True
    print("started listening")

def pause_listening():
    global listening
    listening = False
    print("paused listening")


keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)
'''

# greeting function
def greet_to():

    hour = int(dt.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour <= 12:
        speak(f"GOOD MORNING {USER} sir..")


    elif hour >= 12 and hour <= 16:
        speak(f"GOOD AFTERNOON {USER} sir...")



    elif 16 <= hour <= 19:
        speak(f"GOOD EVENING {USER} sir....")




    h = dt.datetime.now().hour
    t = dt.datetime.now().minute
    speak(f"Its {h}:{t}")
    speak(f"I am {HOSTNAME} HOW MAY I HELP YOU SIR....?")




# take command
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(0) as source:
        print("listening....")
        r.energy_threshold = 8000
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

        if 'stop' not in query:
            speak(choice(se.randomlines))

        if "stop" in query:
            hour = int(dt.datetime.now().hour)
            if 21 <= hour < 6:
                speak("Good night sir , Take care...")
            else:
                speak("Have a good day sir !!!")
                exit()


    except Exception:
        print("Please repeat it sir...")
        query = 'None'
    return query
# function used in setting alarm
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

# the executer of program and container of functions is the next line
if __name__ == "__main__":
    while True:
        query = takecommand().lower()
###########  To activate blaze  ######################33
        if "hey blaze"in query or "hey jarvis" in query or "wake up" in query:
            from intro import play_gif
            play_gif()
            greet_to()
            while True:
                # if listening:
                query = takecommand().lower()
########### SOME COMMOM CONVERSATION LINES YOU CAN ADD MORE############33
                if "go to sleep" in query or "sleep" in query:
                    speak("SIR I am on a sleep if you want to activate me just say wake up")
                    break
                elif "how are you" in query:
                    speak("I am good sir what about you")
                elif "good" in query:
                    speak("Sir I am happy to know that tell me how can I help you")

                elif "what are you doing" in query:
                    speak("I am helping you sir please tell me....")
        # open any app
                elif "open app" in query:
                    speak("Which app do you want to open sir....")
                    name_app= takecommand().lower()
                    ao.open(name_app)
        # close any app
                elif "close app" in query:
                    speak("Which app do you want to close sir....")
                    name_app= takecommand().lower()
                    ao.close(name_app)

        # open command prompt
                elif "open command prompt" in query:
                    speak("Opening command prompt sir..")
                    os.system('start cmd')
        # open camera
                elif "open camera" in query:
                    speak("Opening camera sir..")
                    sp.run('start microsoft.windows.camera:', shell=True)
        # open notepad
                elif "open notepad" in query:
                    speak("Opening notepad sir..")
                    Notepad_p = "C:\\Windows\\system32\\notepad.exe"
                    os.startfile(Notepad_p)
        # search for ip address
                elif "ip address" in query:
                    ip_address = se.find_my_ip()
                    speak(f"Your I.P address is {ip_address}")
        # open youtube and play specified video
                elif "youtube" in query:
                    speak("What do you want to play sir?")
                    video = takecommand().lower()
                    if "play anything" in video:
                        video = choice(se.yt)
                    se.youtube(video)
        # search on youtube
                elif "search on youtube" in query:
                    speak("What do you want to search sir?")
                    query = takecommand().lower()
                    query = query.replace(" ", "+")
                    url = f"https://www.youtube.com/results?search_query={query}"
                    wb.open(url)
        # search on wikipedia
                elif "wikipedia" in query:
                    speak("What do you want to search sir?")
                    query = takecommand().lower()
                    se.search_on_wiki(query)
        # search on google
                elif "google" in query:
                    speak("What do you want to search sir?")
                    query = takecommand().lower()
                    se.search_on_google(query)
        # open stack overflow
                elif "stack overflow" in query:
                    speak("Opening stack over flow sir ....")
                    wb.open("www.stackoverflow.com")
        # open instagram
                elif "open instagram" in query:
                    speak("Opening instagram sir....")
                    wb.open("www.instagram.com")

        # shut down system
                elif "shut down" in query or "shutdown" in query:
                    speak("Shutting down sir..")
                    Shut_p = "C:\\Windows\\system32\\SlideToShutDown.exe"
                    os.startfile(Shut_p)
        # games on chrome
                elif "games" in query:
                    speak("Opening games sir...")
                    wb.open("www.freegames.com")
        # message on whatsapp
                elif "whatsapp" in query:
                    speak("Tell the name of receiver")
                    if "my number" in query:
                        no = '+919198145994'
                    elif "sanju" in query:
                        no = '+917518729265'
                    elif "santosh" in query:
                        no = '+918318002272'
                    elif "usha" in query:
                        no = '+919508654791'
                    speak("Tell the message you want to send")
                    msg = takecommand().lower()
                    hour = int(dt.datetime.now().hour)
                    minu = int(dt.datetime.now().minute) + 1
                    kit.sendwhatmsg(no, msg, hour, minu)

        # convert text to handwritten
                elif "convert text to handwritten" in query:
                    speak("Type the string you want to convert ...")
                    line = input("Type the string you want to convert ...")
                    speak("Sir the name of file, to be saved will be......")
                    name = takecommand().lower()
                    kit.text_to_handwriting(line, f'C:\\USERS\\ADMIN\\Desktop\\{name}.jpg', [0, 0, 138])
                    speak("The file is saved on desktop sir...")
        # open any website
                elif "open website" in query:
                    speak("say the name of the website")
                    website = "www." + takecommand().lower() + ".com"
                    wb.open(website)
        # says where i am
                elif "where i am"in query or "where we are" in query:
                    speak("wait sir, let me check")
                    try:
                        url = "https://ipinfo.io/json"
                        response = urlopen(url)
                        data = json.load(response)
                        city = data['city']
                        region = data['region']
                        country = data['country']
                        # print(data)
                        loc = (f"Sir we are at {city} city of {region} in {country} country")
                        speak(loc)
                    except Exception as e:
                        speak("Sorry sir cannot fetch the location right now...")
                        pass
        # open a particular ig profile & download its D.P
                elif "instagram profile" in query or "profile on instagram" in query:
                    speak("sir please enter the user name correctly...")
                    name = input("Enter the username sir : ")
                    wb.open(f"www.instagram.com/{name}")
                    speak(f"Sir here is the profile of {name}")
                    time.sleep(5)
                    speak(f"Sir would you like to download DP of user")
                    condition = input("Y/N")
                    if "Y" in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name, profile_pic_only= True)
                        speak("I am done sir , picture is savid in main folder . now I am ready to take commands")
                    else:
                        pass
        # take a screenshot
                elif "take screenshot" in query or "take a screenshot" in query:
                    speak("Sir tell the name for your file to be saved ....")
                    naam = takecommand().lower()
                    speak("Sir please hold for a few seconds I am taking screenshot.....")
                    time.sleep(3)
                    img = pog.screenshot()
                    img.save(f"{naam}.png")
                    speak("I am done sir screenshot is saved in main folder")
        # to send email
                elif "email" in query:
                    speak("Enter the email of receiver sir")
                    try:
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        to = input("Please enter the email id here sir...")
                        speak("What do you want to send sir...")
                        login = "legendck60@gmail.com"
                        content = input("Type here")
                        server.sendmail(login ,to_addrs=to,msg=content)
                        speak("Mail has been sent....")
                    except Exception as e:
                        print(e)
                        speak("Sorry sir The email has not been sent")
                        pass
        # to know the temperature of a location
                elif "temperature" in query:
                    speak("Sir you want to get the temerature of which place..")
                    v = takecommand().lower()
                    search = (f"temperature in {v}")
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text , "html.parser")
                    temp = data.find("div" , class_="BNeawe").text
                    speak((f"Sir the {search} is {temp}"))

        # To know today's day and date
                elif "date" in query:
                    date = dt.date.today()
                    day = ca.day_name[date.weekday()]
                    our_date = date.strftime("%d/%m/%y")
                    speak(f"Sir today is {day} and date is {our_date}")

        # to know the battery percent
                elif "battery percent" in query or "percent battery" in query or "battery percentage" in query:
                    import psutil
                    battery = psutil.sensors_battery()
                    per = battery.percent
                    speak(f"Sir battery percentage is {per} %")
                    if per >= 70:
                        speak("Sir we have enough power to continue working....")
                    elif per<70 and per >=50:
                        speak("Sir we have left with nearly half power you may plug in the charger....")
                    elif per <50 and per>= 30:
                        speak("Sir only a little amount of power is left please plug in the charger...")
                    elif per < 30:
                        speak("Sir the system will shot down soon please charge the laptop.....")
        # to know the internet speed
                elif "internet speed" in query:
                    import speedtest
                    st = speedtest.Speedtest()
                    dl = int(st.download() / 1000000)
                    up = int(st.upload() / 1000000)
                    speak(f"Sir your Download speed is {dl} mbps and upload speed is {up} mbps")
        # to volume up
                elif "voume up" in query:
                    pog.press("volumeup")
                    # to volume down
                elif "voume down" in query:
                    pog.press("volumedowm")
        # to volume mute
                elif "voume mute" in query or "mute" in query:
                    pog.press("volumemute")
        # to know the time
                elif "the time" in query:
                    strTime = dt.datetime.now().strftime("%H:%M")
                    speak(f"Sir the time is {strTime}")
        # to make a schedule of my day
                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks(Please speak Yes or No)")
                    query = takecommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt" , "r")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task : "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task : "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
        # to see my made schedule
                elif "show schedule" in query or "so schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("C:\\Users\\Admin\\Downloads\\notifi.mp3")
                    mixer.music.play()
                    plyer.notification.notify(
                        title = "My Schedule : ",
                        message = content,
                        timeout = 15
                        )
        # to check live IPL score
                elif "ipl score" in query or "IPL score" in query:
                    url = "https://www.crickbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text , "html.parser")
                    team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")
                    mixer.init()
                    mixer.music.load("C:\\Users\\Admin\\Downloads\\notifi.mp3")
                    mixer.music.play()

                    plyer.notification.notify(
                        title="IPL SCORE :- ",
                        message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout=15
                        )
        # if something has to be remembered
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("blaze", "")
                    rememberMessage = query.replace("please", "")
                    speak("You told me to " + rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
        # hear what was remembered
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to" + remember.read())
        # pause a video
                elif "pause" in query:
                    pog.press("k")
        # play a video
                elif "play" in query:
                    pog.press("k")
        # to close a tab
                elif "close tab" in query:
                    pog.hotkey("ctrl","w")
        # to open tab
                elif "open tab" in query:
                    pog.hotkey("ctrl","t")
        # to set alarm
                elif "set an alarm" in query:
                    print("input time example:- 10:10")
                    speak("Set the time, sir....")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                elif "play offline game" in query:
                    speak("Opening offline games ,sir......")
                    import brick_breaker
                    brick_breaker.play_offline_game()






            
            

