"""
Note to future self: using venv means you have to be in the venv directory...
use flask --app hello run  
"""
from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

# create a list of dicts from a CSV
presidents_list = convert_to_dict("presidents.csv")
student_list = convert_to_dict("students.csv")
test_list = [{'Name': 'Josh', 'Year': 1}, {'Name': 'Nate', 'Year': 2}]

# create a list of tuples in which the first item is the number
# (Presidency) and the second item is the name (President)
pairs_list = []
for p in presidents_list:
    pairs_list.append( (p['Presidency'], p['President']) )

# first route

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Presidents Index")

@app.route("/user/<name>")
def user(name):
    return render_template('home.html', name=name)

@app.route('/president/<num>')
def detail(num):
    try:
        pres_dict = presidents_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Presidency: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = make_ordinal( int(num) )
    return render_template('president.html', pres=pres_dict, ord=ord, 
                           the_title=pres_dict['President'])

@app.route('/student/<num>')
def student_bio(num):
    try:
        student_dict = test_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Presidency: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = make_ordinal( int(num) )
    return render_template('student.html', stu=student_dict, ord=ord, 
                           the_title=student_dict['Name'])


if __name__ == '__main__':
    app.run(debug=True)
