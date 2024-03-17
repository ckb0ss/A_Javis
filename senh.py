from win32 import win32gui
import datetime
import requests
import wikipedia
import pywhatkit as kit
import json
import os
import calendar as ca
from urllib.request import urlopen
def h_d():
    os.system("attrib -h /s /d")
    print("done")





def find_my_ip():
    ip_address= requests.get("https://api.ipify.org?format=json").json()
    return ip_address["ip"]

def search_on_wiki(query):
    results= wikipedia.summary(query, sentences = 2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)


def location_my():
    url = "https://ipinfo.io/json"
    response = urlopen(url)
    data=json.load(response)
    city = data['city']
    region = data['region']
    country = data['country']
    # print(data)
    print(f"Sir we are at {city} city of {region} region in {country} country")
def today_dateandtime():
    date =datetime.date.today()
    t = datetime.datetime.now()
    new_time = t.strftime('%H:%M')
    new =date.strftime("%d-%m-%y")
    day = ca.day_name[date.weekday()]
    print(day)
    print(date)
    print(new)
    print(new_time)
def sp_t():
    import speedtest
    st = speedtest.Speedtest()
    dl = st.download() / 1000000
    up = st.upload() / 1000000

# today_dateandtime()


yt = ["gotilo" , "pasoori", "satisfya" , "amplifier","khada hu ajj bhi wahi","mai agar kahu",
      "shark tank india"
      "shorts", "kabhi jo badal barse" , "aaja we mahiya","mujhe nahi pata hai"
      "cheques","one love", "no love", "moti chain moti paisa", "offshore", "mashup-shubh"]

randomlines = ["Cool , sir I am working" , "I am here sir, you don't worry",
               "Your work is processing sir" , "You don\'t worry sir I will do it ",
               "Fetching the work sir", "I am doing sir wait a minute",
               "Blaze is working You just relax"]
# print(response)
# if __name__ == "__main__":
#     get_location()