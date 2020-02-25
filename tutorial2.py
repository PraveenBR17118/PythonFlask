from flask import Flask,redirect,url_for , render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index2.html",content=["tim", "joe","bill"])


if __name__=="__main__":
    app.run()





"""
from flask import Flask,redirect,url_for , render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index1.html",content=name)


if __name__=="__main__":
    app.run()

"""
