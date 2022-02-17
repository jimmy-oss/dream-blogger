from flask import Flask,render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    data = requests.get(url)
    response = data.json()
    quote = response["quote"]
    author = response["author"]
     
    return render_template("index.html",quote=quote,author=author)   


if __name__ == '__main__':
    app.run(debug=True)