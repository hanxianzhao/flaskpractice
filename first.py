
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/user/<name>/<haha>")
def user(name,haha):
    return "<h1>Hello,%s,%s</h1>" % (name,haha)

if __name__ == "__main__":
    app.run(debug=True)

