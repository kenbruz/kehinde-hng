from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from datetime import datetime, timezone
import requests
from flask_cors import CORS
import logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()

name = os.getenv("FULL_NAME")
email = os.getenv("EMAIL")
rate_limit = os.getenv("RATE_LIMIT")

# initiating flask
app = Flask(__name__)

# setting Cross-Origin Resource sharing
CORS(app)

# limit request rates
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"],
    storage_uri=rate_limit
)

# basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)


@app.route("/me", methods=["GET"])
def home():
    logger.info("Received request at /me")

    try:
        response = requests.get("https://catfact.ninja/fact", timeout=10)
        response.raise_for_status()
        fact = response.json()["fact"]
        status_code = 200
    except requests.exceptions.RequestException:
        fact = "Could not fetch cat fact due to error. Check the URL or your network and try again"
        status_code = 503

    web_response = {
        "status": "success" if status_code == 200 else "error",
        "user": {
            "name": "Kehinde Okeowo",
            "email": "kenbruz46@gmail.com",
            "stack": "Python/Flask"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact
    }

    return jsonify(web_response), status_code


if __name__ == "__main__":
    app.run(debug=True)
