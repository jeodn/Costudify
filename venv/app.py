"""
This version of Costudify is the one where users can anonymously post their group chats for certain courses.
"""

from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal
from datetime import datetime

app = Flask(__name__)
application = app

class User:
    """
    A user

    === Attributes ===
    username: username as string 
    password: password as string
    posts: list of all posts, posts stored as post ID


    """
    username: str
    password: str
    posts: list[int]
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.posts = []


class Post:
    """
    A group chat posting

    === Attributes ===
    id: The post ID as a number.
    date: date in unix time [OR MAYBE AS A STRING? IDK]
    username: The post's user ID.
    platform: The group chat's platform.
    course: The group chat's course, if any. Can be empty string.
    url: The URL to the group chat.
    title: The title of the post.
    description: The post text. 

    === Representation Invariants ===

    platform, course, url can all be empty string. 
    """
    id: int
    date: str
    user: User
    platform: str
    course: str
    url: str
    title: str
    description: str

    def __init__(self, id, date, user, platform, course, url, title, description):
        self.id = id

        self.date = date
        #self.datestr = self.date.strftime("%Y/%m/%d %H:%M%S")

        self.user = user
        self.platform = platform
        self.course = course
        self.url = url
        self.title = title
        self.description = description


# create a list of dicts from a CSV
posts_list = convert_to_dict("posts.csv")

# create a list of tuples in which the first item is the number
# (Presidency) and the second item is the name (President)
# Constants
KEY_ID = 0
KEY_TITLE = 1
KEY_DESCRIPTION = 2

pairs_list = []
for p in posts_list:
    pairs_list.append( (p['ID'], p['Title'], p['Description']) )


@app.route('/')
def index():
    return render_template('index.html', posts=posts_list, the_title="Main Index")


def id_to_post_title(id: int, post_pairs: list[tuple]):
    """
    Get post title by ID. ID_KEY is position of id in tuple.
    """
    for pair in post_pairs:
        if pair[KEY_ID] == id:
            return pair


@app.route('/detail/<num>')
def detail(num):
    try:
        post_dict = posts_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for post: {num}</h1>"
    post_tuple = id_to_post_title(num, pairs_list)
    desc = post_tuple[KEY_DESCRIPTION]
    title = post_tuple[KEY_TITLE]

    return render_template('post.html', p=post_dict, the_title=f"{post_dict['User']}: {post_dict['Title']}")

if __name__ == "__main__":
    app.run(debug=True)