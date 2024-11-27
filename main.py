from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# ThingSpeak API details
# THINGSPEAK_CHANNEL_ID = "YOUR_CHANNEL_ID"  # Replace with your channel ID
# THINGSPEAK_READ_API_KEY = "YOUR_READ_API_KEY"  # Replace with your read API key
THINGSPEAK_URL = "https://api.thingspeak.com/channels/2760070/feeds.json?api_key=MPUBH5OMQX30DZQW&results=2"

@app.route('/')
def index():
    """
    Fetch data from ThingSpeak and display it on an HTML page.
    """
    try:
        response = requests.get(THINGSPEAK_URL)
        data = response.json()
        feeds = data.get("feeds", [])
        return render_template("index.html", feeds=feeds)
    except Exception as e:
        return f"Error fetching data from ThingSpeak: {e}"

@app.route('/api/data', methods=['GET'])
def api_data():
    """
    API endpoint to return ThingSpeak data as JSON.
    """
    try:
        response = requests.get(THINGSPEAK_URL)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()
