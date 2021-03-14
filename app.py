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
    # user = mongo.db.users.find()
    # return render_template('user.html', user=user)
    websites = {'popular': [
        {'url': 'test1', 'image': 'test_image1'},
        {'url': 'test2', 'image': 'test_image2'},
        {'url': 'test2', 'image': 'test_image2'},
        {'url': 'test2', 'image': 'test_image2'},
        {'url': 'test2', 'image': 'test_image2'},
        ],
        'recent': [
        {'url': 'recent_test1', 'image': 'recent_test_image1'},
        {'url': 'recent_test2', 'image': 'recent_test_image2'}
        ],
        'random': [
        {'url': 'random_test1', 'image': 'random_test_image1'},
        {'url': 'random_test2', 'image': 'random_test_image2'}
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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True) # change to False in production