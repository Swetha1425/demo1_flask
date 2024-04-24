#this is python configuration file
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
     return render_template ("home.html")

@app.route ('/s2s/api/signup')
def user_signup():
     return "this is the user signup page"

@app.route('/s2s/api/contect')
def user_contect():
     return "contect us"

@app.route('/s2s/api/login')
def user_login():
     return "this is my login page"

@app.route('/s2s/api/about')
def user_about():
     return "about us"

@app.route('/s2s/api/blog')
def user_blog():
     return "blob storage"

if __name__=="__main__":
     app.run(debug=True)