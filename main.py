## Integrate HTML with Flask
## HTTP verb GET and POST

## Jinja2
'''
In result.html you can use,
{%...%} for any kind of statements like for loops
{{    }} expression to print output
{#...#} this is for comments
'''


from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')# call index.html file


# Build URL dynamically
@app.route('/passed/<int:score>')
def Passed(score):
    res = ''
    if score>=35:
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('result.html', result = res)# call result.html file


@app.route('/failed/<int:score>')
def Failed(score):
    return "The Person has failed and the marks is "+ str(score)

# Result checker: it will be looped to passed route when the student scores more than 35 marks
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<35:
        result = 'Failed'
    else:
        result = 'Passed'
    return redirect(url_for(result,score=marks))


# Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4

    res = ''
    return redirect(url_for('Passed',score=total_score))
        

if __name__=="__main__":
    app.run(debug=True)