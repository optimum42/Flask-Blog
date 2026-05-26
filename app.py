from flask import Flask, request, render_template, redirect, url_for
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


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form["author"]
        title = request.form["title"]
        content = request.form["content"]
        blog_manager.add_post(
            author=author,
            title=title,
            content=content
        )
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)