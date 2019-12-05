import json
from hello_app import app

@app.route("/")
def welcome_message():
    return json.dumps({
        "response": "Welcome to the Hello app!"
    })
