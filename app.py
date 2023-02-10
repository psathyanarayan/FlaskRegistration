from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import os

app = Flask(__name__,template_folder='templates')
app.secret_key = os.urandom(24)

# hardcoded data for demonstration purposes
event_start = datetime(2023, 2, 20, 12, 0, 0)
schedule = [
    ('12:00 PM', 'Welcome and Introduction'),
    ('12:30 PM', 'Keynote Speaker'),
    ('1:00 PM', 'Break'),
    ('1:30 PM', 'Panel Discussion'),
    ('3:00 PM', 'Closing remarks')
]

# create a list to store registration data
registration_data = []

# home page
@app.route('/')
def home():
    time_remaining = event_start - datetime.now()
    return render_template('home.html', time_remaining=time_remaining, schedule=schedule)

# registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    return render_template('register.html')
    

# registration success page
@app.route('/register_success',methods=['GET', 'POST'])
def register_success():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        registration_data.append(name)
        registration_data.append(email)
        registration_data.append(event)
        print(registration_data)
    return 'Registration successful. Thank you for registering!'

# admin page
@app.route('/admin',methods=['GET', 'POST'])
def admin():
    return render_template('admin.html', name = registration_data[0], email = registration_data[1],event = registration_data[2])

if __name__ == '__main__':
    app.run(debug=True)
