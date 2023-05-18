from flask import Flask, render_template
from post import Post
import requests

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
all_blogs = response.json()
posts = []
for b in all_blogs:
    posts.append(Post(b['id'], b['title'], b['subtitle'], b['body']))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=posts)


@app.route('/post/<int:post_id>')
def blog_post(post_id):
    for post in posts:
        if post.id == post_id:
            return render_template("post.html", post=post)
    return None


if __name__ == "__main__":
    app.run(debug=True)
