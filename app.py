import uuid
import pymongo
import datetime
from flask import Flask,  render_template, jsonify, request, redirect, session, url_for, flash


# Local Imports
import config

# Configurations
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.permanent_session_lifetime = datetime.timedelta(minutes=15)
app.logger.setLevel(10)

try:
    conn = pymongo.MongoClient()
    app.logger.debug('MongoDB Collection Established')
except Exception as err:
    app.logger.err(f"Error at establishing connection - {err}")
else:
    db = conn['ThougthsManager']
    col = db['Collection']


@app.route('/')
def nothing():
    return jsonify(
        {
            "Message": 'Nothing to see here dude'
        }, 200
    )


@app.errorhandler(404)
def user_not_authenticated(error):
    return render_template('error.html'), error


@app.route('/index')
def index():
    if session.get('token') != None:
        app.logger.info(session.get('token'))
        return render_template('index.html')
    else:
        return user_not_authenticated(404)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup_check')
def signup_check():
    email = request.args.get('email')
    password = request.args.get('password')
    app.logger.info(f'Email and Password Recieved {email}, {password}')
    data = {
        'email': email,
        'password': password,
        'inserted_time': datetime.datetime.now()
    }
    if col.count_documents({'email': email}, limit=1) == 0:
        inserted_id = col.insert_one(data).inserted_id
        app.logger.info(f"Data Inserted for {email} with Id - {inserted_id}")
        if inserted_id:
            return redirect('/login')
    else:
        app.logger.info('Already Signed Up. Need to login')
        return redirect('/login')


@app.route('/login_check')
def login_check():
    email = request.args.get('email')
    password = request.args.get('password')
    app.logger.info(f'Email and Password Recieved {email}, {password}')
    if col.count_documents({'email': email, 'password': password}, limit=1) != 0:
        app.logger.info(f"Record of email and password found.")
        session['token'] = str(uuid.uuid4())
        app.logger.info(f"Session Token Set - {session.get('token')}")
        return redirect(url_for('index', var=email))
    else:
        app.logger.info('User Not Registered')
        flash('Need to Signup first')
        return redirect(url_for('signup'))


@app.route('/data')
def showData():
    dataList = list()
    for data in col.find():
        data.pop('_id')
        dataList.append(data)
    app.logger.info(f'Recieved Datalist - {dataList}')
    if not len(dataList) == 0:
        return jsonify(dataList)
    else:
        return jsonify(
            {
                'message': "No Data to show"
            }
        )


if __name__ == '__main__':
    app.run()
