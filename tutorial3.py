from flask import Flask,redirect,url_for , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("indextt3.html")

@app.route("/test")
def home1():
    return render_template("new.html",content="Testing")


if __name__=="__main__":
    app.run(debug=True)