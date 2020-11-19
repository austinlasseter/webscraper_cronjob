# # from flask import Flask, render_template
# # app = Flask(__name__)
# #
# # @app.route('/')
# # def home():
# #    return render_template('index.html')
# #
# # if __name__ == '__main__':
# #    app.run()
# from flask import Flask, request
# # set the project root directory as the static folder, you can set others.
# app = Flask(__name__, static_url_path='')
#
# @app.route('/')
# def root():
#     return app.send_static_file('index.html')
#
# if __name__ == "__main__":
#     app.run()

# serve.py

from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Hello, World"
    return render_template('index.html', message=message)

# run the application
if __name__ == "__main__":
    app.run(debug=True)
