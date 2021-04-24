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
    """Home page
    * Retreives the websites from the database in 3 different ways:

    1. Sorted by stars in descending order
    2. Sorted by _id in descending order (this sorts by timestamp)
    3. Takes a random sample of 5 websites and returns

    * These arrays populate an object and are returned.
    """
    websites_popular = [
        x for x in mongo.db.websites.find().sort("stars", -1).limit(10)]

    websites_recent = [
        x for x in mongo.db.websites.find().sort("_id", -1).limit(10)]

    websites_random = [x for x in mongo.db.websites.aggregate(
        [{"$sample": {"size": 10}}]
    )]
    websites = {
        'popular': websites_popular,
        'recent': websites_recent,
        'random': websites_random
    }

    return render_template('index.html', websites=websites)


@app.route('/store', methods=["GET"])
def store():
    """ Searching:
    * Retreives the search query the user typed
        and use it to search the database.

    * User can search by website name or URL.

    * Return result as an object, appending boolean True,
        as the page this to reformat the layout.

    """
    query = request.args.get('query')
    if query:
        websites_search = list(mongo.db.websites.find(
            {"$text": {"$search": query}}))
    else:
        websites_search = list(mongo.db.websites.find())

    websites = {
        'search': websites_search,
        'searched': True
    }

    return render_template('store.html', websites=websites)


@app.route('/site_details/<websiteid>', methods=['GET', 'POST'])
def siteDetails(websiteid):
    """ Website page:
    GET: Builds the website page that the user sees when they click on a website.

    POST: Handles a user posting a comment on the website page.

    Args:
    1.  websiteid (str): The objectId associated with the MongoDB document
        for that specific website.

    Returns:
    *   POST: comment object is constructed, and based on the 3 comment variations
        available this is what happens:
        1.  COMMENT: star rating is retrieved from comment and website's rating is updated
            accordingly. Comment object is constructed and appended to comments array for
            that website's MongoDB document.
        2.  UPDATE: Previous update comment is replaced with this. Comment object is constructed
            and appended to comments array for that website's MongoDB document.
        3.  BUG: Comment object is constructed and appended to comments array for
            that website's MongoDB document.

    *   GET: The information contained in the MongoDB website document.
    """
    if request.method == 'POST':
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
    return render_template('site_details.html', website=website)


@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    """ User page:
    *   If there is a user logged in, builds the user page 
        from that User's MongoDB document.

    Args:
    1.  username (str): The user's username.

    Returns:
    *   The username, user's data and any website's the user has added.
    """
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


@app.route("/create_site", methods=["GET", "POST"])
def createSite():
    """ Adding a site page:
    *   GET: Returns the create site page template

    *   POST: Constructs a MongoDB website document, and updates both
        the website collection, as well as the user's document with this
        website.
    *   The added image associated with the website (required) is uploaded
        to cloudinary, and the url and id in the cloudinary response is stored
        against the website's document for later retreival.

    """
    if request.method == 'POST':
        existing_website = mongo.db.websites.find_one(
            {"url": request.form.get('site_url')})

        if existing_website:
            flash("Website with this url already exists.", 'error')
            return render_template('create_site.html')

        file = request.files['site_img']
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
        return redirect(url_for('user', username=session['user']))

    return render_template('create_site.html')


@app.route('/update_site/<websiteid>', methods=['GET', 'POST'])
def updateSite(websiteid):
    """ Update your site page:
    *   GET: Returns the update site page template

    *   POST: Updates the website's MongoDB document with new information

    Args:
    1.  websiteid (str): The associated website id.

    Returns:
    *   When successfully updated, it renders the site details page with
        updated information.
    """
    if request.method == 'POST':
        existing_website = mongo.db.websites.find_one(
            {"$and": [
                {"url": request.form.get('site_url')},
                {"_id": {
                    "$ne": ObjectId(websiteid)
                }}
            ]})
        if existing_website:
            flash("Website with this url already exists.", 'error')
            return render_template('create_site.html')

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
    return render_template('update_site.html', website=website)


@app.route('/deleteSite/<websiteid>')
def deleteSite(websiteid):
    """ Delete site route
    *   Deletes the website from the database

    Args:
    1.  websiteid (str): The website id

    Returns:
    *   Removes the website document as well as reference to website in user's
        array of websites. Also removes the website's image from cloudinary.
    """
    mongo.db.users.find_one_and_update(
        {'username': session["user"]},
        {"$pull": {"websites": ObjectId(websiteid)}},
        upsert=True)

    website = mongo.db.websites.find_one({"_id": ObjectId(websiteid)})
    destroy(website["image_id"])
    mongo.db.websites.remove({"_id": ObjectId(websiteid)})

    flash('Website was successfully removed', 'success')
    return redirect(url_for('user', username=session['user']))


@app.route('/signup', methods=['POST'])
def signup():
    """ Sign up route
    *   The passwords entered are checked to validate they match, and
        it is checked that username and email are not already taken,
        before creating a new user document in the Users collection.

    *   The user's password is hashed for security purposes.

    Return:
    *   Redirected to user page

    """
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
    """ Log in route
    *   If the user's email matches that of a user in the Users collection, it
        is then checked that the hashed passwords match.

    Returns:
    *   If successful login, the user is redirected to their User page
    *   If password does not match or email is not found, we give the same error message
        and redirect to home page.

    Return:
    *   Redirected to user page

    """
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
    """ Log out route
    *   If user clicks logout, we simple pop the user cookie from the session array.

    Returns:
    *   Redirects to the home page
    """
    flash("You have successfully been logged out", "success")
    session.pop("user")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)  # change to False in production
