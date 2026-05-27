import json
from abc import ABC, abstractmethod
from pathlib import Path
from config import PATH
from json_storage import BLOG_POSTS


class BlogPostManager(ABC):
    """
    This class is responsible for managing blog posts.
    The abstract methods load_posts and save_posts are implemented by subclasses.
    """
    def __init__(self):
        self.blog_posts = self.load_posts()
        for post in self.blog_posts:
            if post.get("likes") is None:
                post["likes"] = 0

    @abstractmethod
    def load_posts(self):
        pass

    @abstractmethod
    def save_posts(self):
        pass

    def get_next_id(self):
        """ Gets the next available ID for a new post. """
        if not self.blog_posts:
            return 1
        return max(post["id"] for post in self.blog_posts) + 1

    def add_post(self, author, title, content):
        """ Adds a new post to the blog. """
        new_post = {
            "id": self.get_next_id(),
            "author": author,
            "title": title,
            "content": content,
            "likes": 0,
        }

        self.blog_posts.append(new_post)
        self.save_posts()
        return new_post

    def get_post(self, post_id):
        """ Gets a post by its ID. """
        for post in self.blog_posts:
            if post["id"] == post_id:
                return post
        return None

    def update_post(self, post_id, author=None, title=None, content=None):
        """ Updates an existing post. """
        post = self.get_post(post_id)
        if post is None:
            return None
        if author is not None:
            post["author"] = author
        if title is not None:
            post["title"] = title
        if content is not None:
            post["content"] = content
        self.save_posts()
        return post

    def delete_post(self, post_id):
        """ Deletes a post by its ID. """
        post = self.get_post(post_id)
        if post is None:
            return False

        self.blog_posts.remove(post)
        self.save_posts()
        return True

    def show_all_posts(self):
        """ Prints all blog posts. """
        for post in self.blog_posts:
            print(post)

    def reset(self):
        """
        Resets the blog by deleting all posts loads them from the BLOG_POSTS Variable
        It adds resets the likes for all posts
        """
        self.blog_posts = [post for post in BLOG_POSTS]
        for post in self.blog_posts:
            post["likes"] = 0
        self.save_posts()

    def filter_posts(self, search_term):
        """ Filters blog posts based on the search term. """
        if search_term == None or search_term.strip() == "":
            return self.blog_posts
        search_term = search_term.lower()
        return [post for post in self.blog_posts if search_term in post["title"].lower()
                or search_term in post["content"].lower()]

    def add_like(self, post_id):
        """ Adds a like to a post. """
        post = self.get_post(post_id)
        if post is None:
            return False
        post["likes"] += 1
        self.save_posts()
        return True


class BlogPostManagerJSON(BlogPostManager):
    """
    This class is responsible for managing blog posts in a JSON file.
    It is derived from the BlogPostManager class and overrides the load_posts and save_posts methods.
    It loads and saves blog posts from a JSON file.
    """
    def __init__(self, file_path=PATH):
        self.file_path = Path(file_path)
        super().__init__()

    def load_posts(self):
        """ Loads blog posts from a JSON file. """
        if not self.file_path.exists():
            return []
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_posts(self):
        """ Saves blog posts to a JSON file. """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                self.blog_posts,
                file,
                indent=4,
                ensure_ascii=False
            )


def main():
    blog = BlogPostManagerJSON()
    blog.show_all_posts()
    print()
    blog.add_post("John Doe", "First Post", "This is my first post.")
    blog.show_all_posts()
    print()
    blog.update_post(1, title="Updated First Post")
    blog.show_all_posts()
    print()
    blog.delete_post(1)
    blog.show_all_posts()
    print()
    blog.reset()
    blog.show_all_posts()
    print()
    search_term = input("Enter Search term: ")
    filtered_posts = blog.filter_posts(search_term)
    for post in filtered_posts:
        post["likes"] += 1
        print(post)

if __name__ == '__main__':
    main()