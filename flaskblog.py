from flask import Flask, render_template
app = Flask(__name__)

#simple blok post
posts = [
    {
        'author': 'Corey',
        'title': 'Blog post 1',
        'content': 'First post content, Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                   'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                   'ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                   'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non '
                   'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'data_postsed': 'April 20, 2019'
    },
    {
        'author': 'Dominik',
        'title': 'Blog post 2',
        'content': 'Second post content, Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do tempor '
                   'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                   'ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                   'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non '
                   'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'data_postsed': 'April 20, 2019'
    }
]

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html',  title='Home', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')
