from flask import Flask,render_template
import requests

app = Flask(__name__)

 

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/quote")
def quote():
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    data = requests.get(url)
    response = data.json()
    quote = response["quote"]
    author = response["author"]
     
    return render_template("quote.html",quote=quote,author=author)   


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__':
    app.run(debug=True)