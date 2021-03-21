import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    # websites = list(mongo.db.websites.find())
    websites = {'popular': [
        {'url': 'test1', 'image': ''},
        {'url': 'test2', 'image': ''},
        {'url': 'test2', 'image': ''},
        {'url': 'test2', 'image': ''},
        {'url': 'test2', 'image': ''},
        ],
        'recent': [
        {'url': 'recent_test1', 'image': ''},
        {'url': 'recent_test2', 'image': ''},
        {'url': 'recent_test1', 'image': ''},
        {'url': 'recent_test2', 'image': ''},
        {'url': 'recent_test1', 'image': ''}
        ],
        'random': [
        {'url': 'random_test1', 'image': ''},
        {'url': 'random_test2', 'image': ''},
        {'url': 'random_test1', 'image': ''},
        {'url': 'random_test2', 'image': ''},
        {'url': 'random_test1', 'image': ''}
        ],
        }
    return render_template('index.html', websites=websites)


@app.route('/siteDetails/<websiteid>', methods=['GET'])
def siteDetails(websiteid):
    print(websiteid)
    website = mongo.db.websites.find_one({"_id": ObjectId(websiteid)})
    return render_template('siteDetails.html', website=website)
    # websitet = {
    #     'comments': [
    #         {
    #             'username': 'bob_123',
    #             'timestamp': '2 days ago',
    #             'value': 'I really like this website!',
    #             'stars': 4,
    #             'comment_type': 'COMMENT',
    #         },
    #         {
    #             'username': 'jane_456',
    #             'timestamp': '3 days ago',
    #             'value': 'I found this bug I think should be fixed!',
    #             'stars': 3,
    #             'comment_type': 'BUG',
    #         },
    #     ]


@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    if session["user"]:
        user_data = mongo.db.users.find_one({"username": session["user"]})
        user_websites = []
        for website in user_data["websites"]:
            user_websites.append(mongo.db.websites.find_one({"_id": ObjectId(website)}))
        return render_template(
                'user.html', username=user_data["username"],
                user_data=user_data,
                user_websites=user_websites)
    return redirect(url_for("index"))
    # user = {
    #     'username': 'Iain_McHugh',
    #     'email': 'iamchugh@tcd.ie',
    #     'websites': [
    #         {
    #             'id': '123456',
    #             'name': 'My website',
    #             'url': 'https://www.google.com',
    #             'isOwner': True
    #         },
    #         {
    #             'id': '123456',
    #             'name': 'My second website',
    #             'url': 'https://www.google.com',
    #             'isOwner': True
    #         },
    #         {
    #             'id': '123456',
    #             'name': 'My third website',
    #             'url': 'https://www.google.com',
    #             'isOwner': False
    #         },
    #     ]
    # }
    

@app.route("/createSite", methods=["GET", "POST"])
def createSite():
    if request.method == 'POST':
        site = {
            "title": request.form.get('site_name'),
            "url": request.form.get('site_url'),
            "owner": session["user"],
            "description": request.form.get('site_description'),
            "stars": 0,
            "reviews": 0,
            "last_update": "",
            "comments": [],
        }
        website = mongo.db.websites.insert_one(site)
        mongo.db.users.find_one_and_update(
            {'username': session["user"]},
            { "$push": {"websites": website.inserted_id}},
            upsert=True)
        flash("Your website was published successfully", 'success')
        # redirect to siteDetails with inserted_id
        return redirect(url_for('index'))

    return render_template('createSite.html')


@app.route('/updateSite/<websiteid>', methods=['GET', 'POST'])
def updateSite(websiteid):
    if request.method == 'POST':
        website = mongo.db.websites.find_one_and_update(
            {"_id": ObjectId(websiteid)},
            { "$set": {
            "title": request.form.get('site_name'),
            "url": request.form.get('site_url'),
            "owner": session["user"],
            "description": request.form.get('site_description'),
            }})
        updated_website = mongo.db.websites.find_one({"_id": ObjectId(websiteid)})
        flash("Your website was updated successfully", "success")
        return render_template('siteDetails.html', website=updated_website)
    
    website = mongo.db.websites.find_one({"_id": ObjectId(websiteid)})
    return render_template('updateSite.html', website=website)


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        pwd = request.form.get('password')
        re_pwd = request.form.get('repassword')

        if pwd != re_pwd:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('index'))
        
        existing_username = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        existing_email = mongo.db.users.find_one(
            {'email': request.form.get('email').lower()})
        
        if existing_username or existing_email:
            flash("Username or email already exists.", 'error')
            return redirect(url_for('index'))
        
        register = {
            "username": request.form.get('username').lower(),
            "email": request.form.get('email').lower(),
            "password": generate_password_hash(
                request.form.get('password').lower()),
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get('username').lower()
        flash('Welcome ' + request.form.get('username') + 
        ', you are now logged in', 'success')
        return redirect(url_for('user', username=session["user"]))


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one(
            {'email': request.form.get('email').lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get('password')):
                    session["user"] = existing_user["username"].lower()
                    flash('Welcome ' + existing_user["username"] + ', you are now logged in', 'success')
                    return redirect(url_for('user', username=session["user"]))
            else:
                flash('Invalid email or password', 'error')
                return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('index'))


@app.route("/logout")
def logout():
    flash("You have successfully been logged out", "success")
    session.pop("user")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True) # change to False in production