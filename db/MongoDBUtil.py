import datetime
import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.pythondb
# post = {"author": "Maxsu",
#          "text": "My first blog post!",
#          "tags": ["mongodb", "python", "pymongo"],
#          "date": datetime.datetime.utcnow()}
#
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print ("post id is ", post_id)

posts = db.posts

pprint.pprint(posts.find_one())
