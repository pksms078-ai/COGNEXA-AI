Python
from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():

    return {
        "platform":"COGNEXA",
        "status":"running"
    }

if __name__ == "__main__":
    app.run()
