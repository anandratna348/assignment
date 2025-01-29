from flask import Flask, jsonify
import logging
from analytics_ideas import analytics_ideas

app = Flask(__name__)

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route('/')
def home():
    return "Welcome to the Telegram Analytics API!"

@app.route('/analytics', methods=['GET'])
def get_analytics():
    try:
        analytics = analytics_ideas()
        return jsonify(analytics), 200
    except Exception as e:
        logging.error(f"Error fetching analytics: {str(e)}")
        return jsonify({"error": "Failed to fetch analytics."}), 500

if __name__ == '__main__':
    app.run(debug=True)