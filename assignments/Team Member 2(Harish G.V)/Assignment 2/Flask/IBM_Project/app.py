from flask import Flask,render_template, request, url_for, redirect, session,jsonify
 
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')
    
@app.route("/signup",methods=['POST'])
def signup():
    return render_template('signup.html')

@app.route("/login",methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route("/home",methods=['POST'])
def dashboard():
    return render_template('home.html')

@app.route("/about",methods=['POST'])
def about():
    return render_template('about.html')

if __name__=="_main_":
    app.run(debug=True)