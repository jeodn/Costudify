"""
This version of Costudify is the one where users can anonymously post their group chats for certain courses.
"""

from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal, get_posts
from datetime import datetime

app = Flask(__name__)
application = app

posts_list = get_posts('posts.csv')
print([post.title for post in posts_list])


@app.route('/')
def index():
    return render_template('index.html', posts=posts_list, the_title="Index")


@app.route('/detail/<num>')
def detail(num):
    try:
        post = posts_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for post: {num}</h1>"

    return render_template('post.html', post=post, the_title=f"{post.user}: {post.title}")

if __name__ == "__main__":
    app.run(debug=True)