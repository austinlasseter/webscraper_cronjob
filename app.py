from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# display HTML template
@app.route("/")
def display_index():
    return render_template('index.html')


############ Deploy
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
