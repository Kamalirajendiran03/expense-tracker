from flask import Flask , render_template

app = Flask (__name__)

@app.route ('/')

def home():
    return '''<html>
    <head></head>
    <body>
    <h2> welcome </h2>
    <p>
        hai kamalaa<br>
        epdi iruka ...
        </p>
    </body>
    </html>
    '''
@app.route('/j')
def template():
    return render_template('bigof3.html.j2')

if __name__ == '__main__':
    app.run()
        
    
