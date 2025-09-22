import customtkinter as ctk
import requests

API_KEY = "3977392206a4dc6e38face258507e7c9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.configure(text="❌ Please enter a city name")
        return

    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result_label.configure(
            text=f"🌡 {temp}°C\n☁ {desc}\n💧 {humidity}% humidity\n💨 {wind} m/s wind"
        )
    else:
        result_label.configure(text="⚠️ City not found")

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Weather App")
app.geometry("400x300")


title_label = ctk.CTkLabel(app, text="🌤️ Modern Weather App", font=("Arial", 20, "bold"))
title_label.pack(pady=15)

city_entry = ctk.CTkEntry(app, placeholder_text="Enter city name")
city_entry.pack(pady=10, padx=20, fill="x")


search_btn = ctk.CTkButton(app, text="Get Weather", command=get_weather)
search_btn.pack(pady=10)


result_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
result_label.pack(pady=20)

app.mainloop()



