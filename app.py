from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():    
     return render_template('home.html',
        title = 'Hello World',
        msg = 'Hello World')

if __name__ == '__main__':
    app.run()
