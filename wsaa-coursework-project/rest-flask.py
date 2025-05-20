from flask import Flask, jsonify, request, render_template
import requests
from flask_cors import CORS
from config import API_KEY


app = Flask(__name__)
CORS(app)

counties_data = {}

def fetch_weather(county):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={county}&appid={API_KEY}&units=metric"

    response = requests.get(url)
   
    if response.status_code == 200:
        data = response.json()
        return {
            "county": data.get("name", county),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }   
    else:
        return None

@app.route('/counties', methods=['GET'])
def get_counties():
    return jsonify(list(counties_data.values()))

@app.route('/counties', methods=['POST'])
def add_county():
    data = request.get_json()
    county = data.get("county")
    if not county:
        return jsonify({"error": "county is required"})

    weather = fetch_weather(county)
    if not weather:
        return jsonify({"error": "weather data not found"})

    counties_data[county.lower()] = weather
    return jsonify(weather)

@app.route('/counties/<county>', methods=['PUT'])
def update_county(county):
    county_key = county.lower()
    if county_key not in counties_data:
        return jsonify({"error": "county not found"})

    weather = fetch_weather(county)
    if not weather:
        return jsonify({"error": "Weather data not found"})
    
    counties_data[county_key] = weather
    return jsonify(weather)

@app.route('/counties/<county>', methods=['DELETE'])
def delete_county(county):
    county_key = county.lower().replace("county ", "")
    for key in list(counties_data.keys()):
        if key.lower().replace("county ", "") == county_key:
            del counties_data[county_key]
            return jsonify({"message": f"{county} deleted"})
    return jsonify({"error": "county no found"})

@app.route('/')
def index():
    return render_template('weather-openweathermap.html')  

if __name__ == "__main__":
    app.run(debug=True)
