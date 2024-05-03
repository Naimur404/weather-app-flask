from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = 'be9ceaf2a3264c4da22181334240305'
    
    location = request.args.get('city')  # Get location from query parameter
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if  location != '':
       
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes"
    else:
        
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}&aqi=yes"
    

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        weather_data = response.json()
        return jsonify(weather_data)
    except requests.RequestException as e:
        return jsonify({'error': f"Error fetching weather data: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

