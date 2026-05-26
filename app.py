from flask import Flask, render_template
from blog_manager import BlogPostManagerJSON

app = Flask(__name__)
blog_manager = BlogPostManagerJSON()


@app.route('/helloworld')
def hello_world():
    return 'Hello, World!'

@app.route("/")
def index():
    blog_posts = blog_manager.read_all_posts()
    return render_template("index.html", blog_posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)