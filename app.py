import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
def index():
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


@app.route('/siteDetails')
def siteDetails():
    website = {
        'owners': ['IainMcHugh'],
        'title': 'WebApp Store',
        'url': 'https://www.webappstore.com',
        'description': 'This is a description of the purpose of the website and blah blah blah. This is a description of the purpose of the website and blah blah blah. This is a description of the purpose of the website and blah blah blah.',
        'stars': 4,
        'reviews': 100,
        'last_update': 'This is the most recent update description.',
        'comments': [
            {
                'username': 'bob_123',
                'timestamp': '2 days ago',
                'value': 'I really like this website!',
                'stars': 4,
                'comment_type': 'COMMENT',
            },
            {
                'username': 'jane_456',
                'timestamp': '3 days ago',
                'value': 'I found this bug I think should be fixed!',
                'stars': 3,
                'comment_type': 'BUG',
            },
        ]
    }
    return render_template('siteDetails.html', website=website)


@app.route('/user')
def user():
    # user = mongo.db.users.find()
    user = {
        'username': 'Iain_McHugh',
        'email': 'iamchugh@tcd.ie',
        'websites': [
            {
                'id': '123456',
                'name': 'My website',
                'url': 'https://www.google.com',
                'isOwner': True
            },
            {
                'id': '123456',
                'name': 'My second website',
                'url': 'https://www.google.com',
                'isOwner': True
            },
            {
                'id': '123456',
                'name': 'My third website',
                'url': 'https://www.google.com',
                'isOwner': False
            },
        ]
    }
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True) # change to False in production