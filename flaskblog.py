from flask import Flask
# flask package to render template in routes..to render static pages essentially
from flask import render_template, url_for

posts = [
    {
        'author': 'Sid Harsha',
        'title': 'Blog post 1',
        'content': 'This is the first post',
        'date': 'Aug 3, 2022'
    },
    {
        'author': 'Harsha',
        'title': 'Blog post 2',
        'content': 'This is the Second post',
        'date': 'Sep 12, 2022'
    },
    {
        'author': 'Negan',
        'title': 'Blog post 3',
        'content': 'This is the Third post',
        'date': 'Aug 11, 2022'
    }
]

# __name__ is name of the module..tells flask where to look for templates and stuff
app = Flask(__name__)


@app.route("/")
@app.route("/home")  # decorators
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)
