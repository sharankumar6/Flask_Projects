
# Understanding a sample Flask web application

from flask import Flask

# It is a WSGI application communicating with the server
app = Flask(__name__) # Initialising flask app object


# Decorator is very much important, This decorator comes with the binding along with the function
# It takes 2 params: 
# 1. Rule  ('/' root) 
# 2. Options (methods: POST or GET)

@app.route('/') #'/' --> Route homepage: http://127.0.0.1:5000
def welcome():
    return "Welcome to my Channel, please subscribe"

@app.route('/members') #'/' --> members homepage: http://127.0.0.1:5000/members
def welcome_members():
    return "Welcome to my yotube Channel guys........subscribe"


# For execution
if __name__=="__main__":
    app.run(debug=True)