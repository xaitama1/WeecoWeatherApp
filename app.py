from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = 'd9500df09dfa22269c5633b3765bb077'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    if not city:
        return "<h3>Please enter a city name!</h3><a href='/'>Go Back</a>"

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"<h3>City not found: {city}</h3><a href='/'>Go Back</a>"

        weather = data['weather'][0]['main']
        temp = round(data['main']['temp'])
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        return render_template('result.html', city=city, weather=weather, temp=temp, humidity=humidity, wind_speed=wind_speed)

    except Exception as e:
        return f"<h3>An error occurred: {e}</h3><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
