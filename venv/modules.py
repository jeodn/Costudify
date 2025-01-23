"""
functions to be imported into the presidents Flask app
"""

import csv

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

    def get_app_icon(self):
        """
        Return filepath to icon of Post's platform.
        """
        app_icons = {"WeChat": "/static/wechat.png",
                     "Instagram": "/static/instagram.png"
                     }
        
        return app_icons[self.platform]


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


def convert_to_dict(filename):
    """
    Convert a CSV file to a list of Python dictionaries
    """
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create DictReader object
    my_reader = csv.DictReader(datafile)

    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # close original csv file
    datafile.close()

    # return the list
    return list_of_dicts


def make_ordinal(num):
    """
    Create an ordinal (1st, 2nd, etc.) from a number.
    """
    base = num % 10
    if base in [0,4,5,6,7,8,9] or num in [11,12,13]:
        ext = "th"
    elif base == 1:
        ext = "st"
    elif base == 2:
        ext = "nd"
    else:
        ext = "rd"
    return str(num) + ext

# tryouts
def test_make_ordinal():
    for i in range(1,46):
        print(make_ordinal(i))

def search_the_list(list):
    for item in list:
        if "Whig" in item['Party']:
            print(item['President'] + " was a Whig.")
    for k in list[0].keys():
        print(k)

# run tryouts
if __name__ == '__main__':
    test_make_ordinal()
    presidents_list = convert_to_dict("presidents.csv")
    search_the_list(presidents_list)
    print(make_ordinal(12))
    print(make_ordinal(32))