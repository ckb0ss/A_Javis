import pyttsx3
import datetime
from pygame import mixer

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
from win32 import win32gui,win32ui
extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            mixer.init()
            mixer.music.load("C:\\Users\\Admin\\Downloads\\animal_bgm.mp3")
            mixer.music.play()
            # os.startfile("C:\\Users\\Admin\\Downloads\\animal_bgm.mp3") #You can choose any music or ringtone
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)