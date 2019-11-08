from flask import Flask, render_template
import datetime
cities = ["Edmonton", "Winnipeg", "Toronto"]

app = Flask(__name__)
year = datetime.datetime.now().year
name = "Holly Meade"

@app.route('/')
def index():
    return render_template("index.html",year=year, name=name)

@app.route('/about-me')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=4000)