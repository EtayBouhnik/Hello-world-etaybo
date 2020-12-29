from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
