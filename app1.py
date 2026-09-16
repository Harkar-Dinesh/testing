from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

@app.route("/healthy")
def health():
    return "Application is healthy"

if __name__ == "__main__":



    app.run(host="0.0.0.0", port=1000)

