import os
from datetime import datetime
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
import cloudinary as Cloud
from cloudinary.uploader import upload, destroy
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

Cloud.config.update = ({
    'cloud_name': os.environ.get('CLOUD_NAME'),
    'api_key': os.environ.get('CLOUD_KEY'),
    'api_secret': os.environ.get('CLOUD_SECRET')
})


@app.route('/')
def index():
    # get popular websites
    websites_popular = [
        x for x in mongo.db.websites.find().sort("stars", -1).limit(5)]
    # get recently added websites
    websites_recent = [
        x for x in mongo.db.websites.find().sort("_id", -1).limit(5)]
    # get random websites
    websites_random = [x for x in mongo.db.websites.aggregate(
        [{"$sample": {"size": 5}}]
    )]
    websites = {
        'popular': websites_popular,
        'recent': websites_recent,
        'random': websites_random
    }
    return render_template('index.html', websites=websites)


@app.route('/siteDetails/<websiteid>', methods=['GET', 'POST'])
def siteDetails(websiteid):

    if request.method == 'POST':
        # its a comment post
        if "user" in session:
            if request.form.get('type') == 'comment':
                comment = {
                    'username': session['user'],
                    'timestamp': datetime.now(),
                    'stars': int(request.form.get('site-stars')),
                    'value': request.form.get('site-description'),
                    'comment_type': request.form.get('type')
                }
                website = mongo.db.websites.find_one(
                    {"_id": ObjectId(websiteid)})

                reviews = website["reviews"]
                stars_total = website["stars_total"]

                new_reviews = reviews + 1
                new_stars_total = stars_total + \
                    int(request.form.get('site-stars'))
                new_stars = int(new_stars_total/new_reviews)

                mongo.db.websites.find_one_and_update(
                    {"_id": ObjectId(websiteid)},
                    {"$push": {"comments": comment},
                     "$set": {"reviews": new_reviews, "stars": new_stars, "stars_total": new_stars_total}},
                    upsert=True)
            elif request.form.get('type') == 'update':
                comment = {
                    'username': session['user'],
                    'timestamp': datetime.now(),
                    'value': request.form.get('site-description'),
                    'comment_type': request.form.get('type')
                }
                mongo.db.websites.find_one_and_update(
                    {"_id": ObjectId(websiteid)},
                    {"$push": {"comments": comment},
                     "$set": {"last_update": request.form.get('site-description')}},
                    upsert=True)
            else:
                comment = {
                    'username': session['user'],
                    'timestamp': datetime.now(),
                    'value': request.form.get('site-description'),
                    'comment_type': request.form.get('type')
                }
                mongo.db.websites.find_one_and_update(
                    {"_id": ObjectId(websiteid)},
                    {"$push": {"comments": comment}},
                    upsert=True)
            flash('Commented successfully', 'success')
        else:
            flash('You need to be logged in to add a comment', 'info')
        return redirect(url_for('siteDetails', websiteid=websiteid))
    website = mongo.db.websites.find_one({"_id": ObjectId(websiteid)})
    return render_template('siteDetails.html', website=website)


@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    if session["user"]:
        user_data = mongo.db.users.find_one({"username": session["user"]})
        user_websites = []
        if "websites" in user_data:
            for website in user_data["websites"]:
                user_websites.append(mongo.db.websites.find_one(
                    {"_id": ObjectId(website)}))

        if not user_websites:
            flash(
                'Click the "ADD" button to publish your first website!', 'info')
        return render_template(
            'user.html', username=user_data["username"],
            user_data=user_data,
            user_websites=user_websites)
    return redirect(url_for("index"))


@app.route("/createSite", methods=["GET", "POST"])
def createSite():
    if request.method == 'POST':
        # Get image and post to cloudinary
        file = request.files['site_img']
        # upload to cloudinary
        cloudinary_response = upload(
            file,
            folder="webapp_store/site_images/",
            public_id=request.form.get('site_name'),
            overwrite=True,
            resource_type='image',
            transformation=[{'width': 640}]
        )
        site = {
            "title": request.form.get('site_name'),
            "url": request.form.get('site_url'),
            "owner": session["user"],
            "description": request.form.get('site_description'),
            "stars": 0,
            "reviews": 0,
            "stars_total": 0,
            "last_update": "",
            "image": cloudinary_response["url"],
            "image_id": cloudinary_response["public_id"],
            "comments": [],
        }
        website = mongo.db.websites.insert_one(site)
        mongo.db.users.find_one_and_update(
            {'username': session["user"]},
            {"$push": {"websites": website.inserted_id}},
            upsert=True)
        flash("Your website was published successfully", 'success')
        # redirect to siteDetails with inserted_id
        return redirect(url_for('user', username=session['user']))

    return render_template('createSite.html')


@app.route('/updateSite/<websiteid>', methods=['GET', 'POST'])
def updateSite(websiteid):
    if request.method == 'POST':
        website = mongo.db.websites.find_one_and_update(
            {"_id": ObjectId(websiteid)},
            {"$set": {
                "title": request.form.get('site_name'),
                "url": request.form.get('site_url'),
                "owner": session["user"],
                "description": request.form.get('site_description'),
            }})
        updated_website = mongo.db.websites.find_one(
            {"_id": ObjectId(websiteid)})
        flash("Your website was updated successfully", "success")
        return render_template('siteDetails.html', website=updated_website)

    website = mongo.db.websites.find_one({"_id": ObjectId(websiteid)})
    return render_template('updateSite.html', website=website)


@app.route('/deleteSite/<websiteid>')
def deleteSite(websiteid):
    # need to delete from websites and user website list
    mongo.db.users.find_one_and_update(
        {'username': session["user"]},
        {"$pull": {"websites": ObjectId(websiteid)}},
        upsert=True)
    website = mongo.db.websites.find_one({"_id": ObjectId(websiteid)})
    destroy(website["image_id"])
    mongo.db.websites.remove({"_id": ObjectId(websiteid)})
    # delete associated cloudinary image
    flash('Website was successfully removed', 'success')
    return redirect(url_for('user', username=session['user']))


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
                flash(
                    'Welcome ' + existing_user["username"] + ', you are now logged in', 'success')
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
            debug=True)  # change to False in production
