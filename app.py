from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Secure Employee Portal</h1><p>Application is running.</p>"


if __name__ == "__main__":
    app.run(debug=True)
