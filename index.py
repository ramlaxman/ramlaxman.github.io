from flask import Flask

app = Flask(__name__)

#following line is example of decorator
@app.route('/') 
def index():
    return '<h3><a href="http://localhost:5000/home">Home</a><br/><a href="http://localhost:5000/about">About</a><br/><a href="http://localhost:5000/resume">Resume</a><br/><a href="http://localhost:5000/social">Socialize</a></h3>'

@app.route('/home/<place>') 
def home(place):
    return '<h1> You are on the ' + place + '! </h1>'
#in browser, type http://localhost/home/Youtube. Any name will be printed for place.

@app.route('/about',methods=['GET','POST']) 
def about():
    return '<h1> This is first page by Mayur for Flask. </h1>'

@app.route('/resume') 
def resume():
    return '<h1> Programming, Teaching, Theology </h1>'

@app.route('/social') 
def social():
    return '<a href="https://twitter.com/RamMayur"> Tweet </a><a href="https://www.facebook.com/RamMayur"> Facebook </a><a href="https://plus.google.com/+mayurpatil"> G+ </a>'

if __name__ == '__main__':
    app.run(debug=True)
