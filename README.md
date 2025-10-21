# 🐾 Kenbruz-Fact-API
A basic RESTful API using Flask that serves up my profile details alongside a random cat fact pulled from an external API

## Description

This lightweight Flask REST API that exposes a `/me` endpoint. The endpoint returns user information, a timestamp,
and a random cat fact fetched from an external API. This project is ideal for beginners exploring Flask, environment 
variables, and external API integration.

---

## 🚀 Features

- `/me` endpoint returns:
  - Username and email (loaded from environment variables)
  - Tech stack info
  - UTC timestamp
  - Random cat fact from [catfact.ninja](https://catfact.ninja)
- Graceful error handling for failed API requests
- Clean JSON response using Flask’s `jsonify`

---

## 🧱 Project Structure

Cat-API/
  - app.py 
  - .env 
  - requirements.txt 
  - README.md

---

## ⚙️ Installation

### 1. Clone the Repository
  - git clone https://github.com/kenbruz/kehinde-hng.git

### 2. Create a Virtual Environment
  - python -m venv .venv (for Windows)
  - python3 -m venv .venv (for macOS/Linux)

### 3. Activate the Virtual Environment
  - .venv\Scripts\activate (for Windows)
  - source .venv/bin/activate (for macOS/Linux)

### 3. Install Dependencies
  - pip install -r requirements.txt


🛠️ Usage
1. Run the Flask App
   - python app.py
   - By default, the app runs on http://127.0.0.1:5000

2. Access the Endpoint
Visit http://127.0.0.1:5000/me to see your JSON response.

📦 Key Files
1. app.py: Contains the Flask app and /me route logic

2. .env: Stores user-specific environment variables

3. requirements.txt: Lists required Python packages

🧪 Example Response

---
Docker support for deployment

🧑‍💻 Author
Damilola — Built with ❤️ and Flask.

📄 License
This project is licensed under the MIT License.

