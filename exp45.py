from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)