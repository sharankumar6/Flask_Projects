# Build URL dynamically
# Variable Rules and URL building

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to my channel"


# Build URL dynamically
@app.route('/passed/<int:score>')
def Passed(score):
    return "The Person is passed and the marks is: "+ str(score)


@app.route('/failed/<int:score>')
def Failed(score):
    return "The Person is failed and the marks is: "+ str(score)

# Result checker: it will be looped to passed route when the student scores more than 35 marks
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<35:
        result = 'Failed'
    else:
        result = 'Passed'
    return redirect(url_for(result,score=marks))
        

if __name__=="__main__":
    app.run(debug=True)