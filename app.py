from flask import Flask, request, render_template, redirect, url_for
from blog_manager import BlogPostManagerJSON

app = Flask(__name__)
blog_manager = BlogPostManagerJSON()


@app.route('/helloworld')
def hello_world():
    return 'Hello, World!'

@app.route("/")
def index():
    search_term = request.args.get('s', '')
    blog_posts = blog_manager.filter_posts(search_term)
    return render_template("index.html", blog_posts=blog_posts, title="Posts")


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
    return render_template('add.html', title="Add Post")


@app.route('/delete/<int:post_id>')
def delete(post_id):
    blog_manager.delete_post(post_id)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = blog_manager.get_post(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        author = request.form["author"]
        title = request.form["title"]
        content = request.form["content"]
        blog_manager.update_post(
            post_id,
            author=author,
            title=title,
            content=content
        )
        return redirect(url_for('index'))

    return render_template('update.html', post=post, title="Update Post")


@app.route('/reset')
def reset():
    blog_manager.reset()
    return redirect(url_for('index'))


@app.route('/reset_confirm')
def reset_confirm():
    return render_template("reset_confirm.html", title="RESET")

@app.route('/like/<int:post_id>')
def like(post_id):
    blog_manager.add_like(post_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)