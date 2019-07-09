from flask import Flask, request, render_template
from jinja2 import Template, Environment, FileSystemLoader, select_autoescape
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

env = Environment(
    loader=FileSystemLoader('./Templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20))
    content = db.Column(db.String(255))
    date = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name



@app.route("/")
def homepage():
    return "hi"

@app.route("/blog")
def blogs():
    return "here we have blogs"

@app.route("/newpost", method="POST")
def newpost():
    return "here we will add a new post to the database"


if __name__ == '__main__':
    app.run()
