from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username = username)
    
if __name__ == '__main__':
    app.run(port=5000)

