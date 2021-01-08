from flask import Flask,  render_template, url_for, redirect, request, session

app = Flask(__name__)
app.secret_key = '111'

@app.route('/')
def main_func():
    return render_template('main.html')

def Etaycv():
    return redirect('cv.html')
def hobbies():
    return render_template('ass8.html')


def Send_massage():
    return redirect('Contact.html')


@app.route('/Etaycv')
def Etaycv():
    return render_template('cv.html')


@app.route('/Contract')
def Send_massage():
    return render_template('Contact.html')


@app.route('/Send_massage')
def leave_details_func():
    return render_template('leave_details.html')

@app.route('/hobbies')
def hobbies():
    user = 'etay'
    return render_template('assignament8.html', name=user, sport ={'Football','Handball','Volleyball'},music ={'Coldplay','Chriss cornel','Band of horses'})

@app.route('/block')
def block_func():
    user='etay'
    return render_template('block.html',name=user, sport ={'Football','Handball','Volleyball'},music ={'Coldplay','Chriss cornel','Band of horses'})



@app.route('/ass9', methods=['GET','POST'])
def assignament9():
    username = ''
    users = [
        {'id': 2, 'firstname': "Mark", 'lastname': "Howell", 'age': 25, 'mail': "Mark.Howell@reqres.in"},
        {'id': 3, 'firstname': "Pam", 'lastname': "Fields", 'age': 27, 'mail': "Pam.Fields@reqres.in"},
        {'id': 4, 'firstname': "Michael ", 'lastname': "Lawson", 'age': 30, 'mail': "Michael.lawson@reqres.in"},
        {'id': 5, 'firstname': "Lindsay", 'lastname': "Ferguson", 'age': 30, 'mail': "Lindsay.Ferguson@reqres.in"},
        {'id': 6, 'firstname': "Tobias", 'lastname': "Funke", 'age': 30, 'mail': "Tobias.Funke@reqres.in"},

    ]

    firstname = ''
    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']
    if request.method == 'POST':
        if username == '':
            username = request.form['username']
            session['Logged_in'] = True
            session['username'] = username
        else:
            session['Logged_in'] = False
            session['username'] = ''
            username = ''
    return render_template('assignament9.html',
                           request_method=request.method, username=username,
                           firstname=firstname, users=users)

if __name__ == '__main__':
    app.run(debug=True)