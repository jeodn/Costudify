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


def id_to_post_title(id: int, post_pairs: list[tuple]):
    """
    Get post title by ID. ID_KEY is position of id in tuple.
    """
    for pair in post_pairs:
        if pair[KEY_ID] == id:
            return pair


# create a list of dicts from a CSV. Or, create a list of Posts.
#posts_list = convert_to_dict("posts.csv")
def get_posts(post_file: str):
    """
    Return a list of Post objects with information from posts.csv.
    """
    post_dicts = convert_to_dict("posts.csv") # list of dictionaries
    out_list = []

    for p in post_dicts:
        out_list.append( Post(p['ID'], p['Date'], p['User'], p['Platform'], 
                        p['Course'], p['URL'], p['Title'], p['Description']) )

    return out_list

posts_list = get_posts('posts.csv')


@app.route('/')
def index():
    return render_template('index.html', posts=posts_list, the_title="Main Index")


@app.route('/detail/<num>')
def detail(num):
    try:
        post = posts_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for post: {num}</h1>"

    return render_template('post.html', post=post, the_title=f"{post.user}: {post.title}")

if __name__ == "__main__":
    app.run(debug=True)