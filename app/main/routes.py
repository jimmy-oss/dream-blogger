from flask import Blueprint  
from flask import render_template, request, Blueprint
from app.models import Post
import requests

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/quote")
def quote():
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    data = requests.get(url)
    response = data.json()
    quote = response["quote"]
    author = response["author"]
     
    return render_template("quote.html",quote=quote,author=author)   

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')