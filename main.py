from tkinter import *
import requests
import json
from datetime import datetime

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Weather Phyton")


city_value = StringVar()

def showWeather():
    api_key = "51018b60257b50207fc63de7c53af5e1"
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(weather_url)
    weather_info = response.json()

    tfield.delete("1.0", "end")

    if weather_info['cod'] == 200:

        temp = int(weather_info['main']['temp'] - 273)
        feels_like_temp = int(weather_info['main']['feels_like'] - 273)
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"\n Şehir : {city_name}\n Sıcaklık (Celsius): {temp}°\n Hissedilen (Celsius): {feels_like_temp}°\n Güneşin Doğuşu {sunrise_time} \n Güneşin Batışı {sunset_time}\n Cloud: {cloudy}%\n Bilgi: {description}"

    else:
        weather = f"\n\tHava Durumu '{city_name}' Başarısız !\n\tGeçerli Şehir Adı Giriniz !!"
    tfield.insert(INSERT, weather)
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


city_head = Label(root, text='Şehir Adı', font='Arial 12 bold').pack(pady=10)
inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()
Button(root, command = showWeather, text = "Hava Durumu", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
weather_now = Label(root, text="Sonuç : ", font='arial 12 bold').pack(pady=10)

tfield = Text(root, width=46, height=10)
tfield.pack()


root.mainloop()