'''
author: Jesse Greenlee
Main Program
'''

from Golfer import Golfer
from GolferDatabase import Golfer_Database
from flask import Flask, request, render_template
import urllib.request
import urllib.parse



app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form['submit'] == 'Add':
            add_data(request)
        if request.form['submit'] == 'Update':
            update_data(request)
        if request.form['submit'] == 'Login':
            userName = request.form['userName']
            pwd = request.form['password']
            print(userName, pwd)
            if userName == 'admin' and pwd == 'password':
                return redirect()
            else:
                print('Incorrect username or password')
                data4 = nope()
                return render_template('index.html', data4=data4)
        if request.form['submit'] == 'Search':
            data = search_data(request)
            return render_template('index.html', data=data)
        if request.form['submit'] == 'Display All':
            data = get_all()
            return render_template('index.html', data=data)
        if request.form['submit'] == 'Caddie':
            data2 = yardage_data(request)
            return render_template('index.html', data2=data2)
        if request.form['submit'] == 'Remove':
            remove_data()
    data = None
    return render_template('index.html', data=data)

def redirect():
    url = 'http://127.0.0.1:5000/remove' #  I don't think that this url "truly" brings up this what I typed in there('http://127.0.0.1:5000/remove'). It just brings up 'http://127.0.0.1:5000/'. Slightly confused.
    req = urllib.request.urlopen(url)
    return req

def nope():
   text = 'Wrong username or password'
   return text


# Route for remove a record
@app.route('/remove', methods=['POST', 'GET'])
def remove():
    if request.method == 'POST':
        if request.form['submit'] == 'Remove':
            remove_data()
    data4 = None
    return render_template('remove.html', data=data4)


# function to remove a record (golfer)
def remove_data():
    userInput = request.form['uInput']
    print(userInput)
    db = Golfer_Database()
    db.remove(userInput)
    db.close_database()


# function to adjust yardage
def yardage_data(request):
    caddie_rec = []
    yardage = request.form['yardage']
    wind = request.form['wind']
    yardage = int(yardage)
    wind = int(wind)
    print('Golfer entered yardage', yardage, 'and wind', wind)
    if wind > 0:
        data2 = wind + yardage
    else:
        data2 = yardage + (wind / 2)
    caddie_rec.append(data2)
    print(caddie_rec)
    return caddie_rec

# method to look for a golfer
def search_data(request):
    userInput = request.form['search']
    print('The user entered:', userInput)
    #player = Golfer(None, None, None, None, userInput)
    db = Golfer_Database()
    data = db.search(userInput)
    db.close_database()
    return data

# update a golfers information
def update_data(request):
    id = request.form['id']
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    driver = request.form['driver']
    three_wood = request.form['three_wood']
    hybrid = request.form['hybrid']
    five_iron = request.form['five']
    six_iron = request.form['six']
    seven_iron = request.form['seven']
    eight_iron = request.form['eight']
    nine_iron = request.form['nine']
    p_wedge = request.form['p_wedge']
    s_wedge = request.form['s_wedge']
    l_wedge = request.form['l_wedge']
    print('This is what the golfer entered:', id, f_name, l_name, driver, three_wood, hybrid, five_iron, six_iron, seven_iron, eight_iron, nine_iron, p_wedge, s_wedge, l_wedge)
    player1 = Golfer( f_name, l_name, driver, three_wood, hybrid, five_iron, six_iron, seven_iron, eight_iron, nine_iron, p_wedge, s_wedge, l_wedge, id)
    print(player1)
    db = Golfer_Database()
    db.update(player1)
    db.close_database()

# add a new golfer
def add_data(request):
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    driver = request.form['driver']
    three_wood = request.form['three_wood']
    hybrid = request.form['hybrid']
    five_iron = request.form['five']
    six_iron = request.form['six']
    seven_iron = request.form['seven']
    eight_iron = request.form['eight']
    nine_iron = request.form['nine']
    p_wedge = request.form['p_wedge']
    s_wedge = request.form['s_wedge']
    l_wedge = request.form['l_wedge']
    print('This is what the golfer entered:', f_name, l_name, driver, three_wood, hybrid, five_iron, six_iron, seven_iron, eight_iron, nine_iron, p_wedge, s_wedge, l_wedge)
    player1 = Golfer(f_name, l_name, driver, three_wood, hybrid, five_iron, six_iron, seven_iron, eight_iron, nine_iron, p_wedge, s_wedge, l_wedge)
    print(player1)
    db = Golfer_Database()
    db.insert(player1)
    db.close_database()

# get all the golfers in the database
def get_all():
    db = Golfer_Database()
    data = db.get_all_data()
    db.close_database()
    return data






if __name__ == '__main__':
    #app.run(debug=True)
    #you can use this method for testing
    pass