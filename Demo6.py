from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/hello/<user>")
def hello_name(user):
    return render_template('hello.html', name = user)

@app.route('/')
def hello():
    return 'Hello!'

if __name__=="__main__":
    app.run(debug=True)