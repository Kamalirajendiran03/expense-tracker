'''
from flask import Flask , request , render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('project.html')'''
from flask import Flask , request , render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_tempate('home.html')

@app.route("/about") 
def about():
	return "about page"




if __name__ == '__main__':
    app.run()
