import json
from abc import ABC, abstractmethod
from pathlib import Path
from config import PATH
from json_storage import BLOG_POSTS


class BlogPostManager(ABC):
    def __init__(self):
        self.blog_posts = self.load_posts()

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def load_posts(self):
        pass

    @abstractmethod
    def save_posts(self):
        pass

    def get_next_id(self):
        if not self.blog_posts:
            return 1

        return max(post["id"] for post in self.blog_posts) + 1

    def add_post(self, author, title, content):
        new_post = {
            "id": self.get_next_id(),
            "author": author,
            "title": title,
            "content": content
        }

        self.blog_posts.append(new_post)
        self.save_posts()
        return new_post

    def read_post(self, post_id):
        for post in self.blog_posts:
            if post["id"] == post_id:
                return post

        return None

    def read_all_posts(self):
        return self.blog_posts

    def update_post(self, post_id, author=None, title=None, content=None):
        post = self.read_post(post_id)

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
        post = self.read_post(post_id)

        if post is None:
            return False

        self.blog_posts.remove(post)
        self.save_posts()
        return True


class BlogPostManagerJSON(BlogPostManager):
    def __init__(self, file_path=PATH):
        self.file_path = Path(file_path)
        super().__init__()

    def reset(self):
        self.blog_posts = [post for post in BLOG_POSTS]
        self.save_posts()

    def load_posts(self):
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_posts(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                self.blog_posts,
                file,
                indent=4,
                ensure_ascii=False
            )

    def show_posts(self):
        for post in self.blog_posts:
            print(post)


def main():
    blog = BlogPostManagerJSON()
    blog.show_posts()
    print()
    blog.add_post("John Doe", "First Post", "This is my first post.")
    blog.show_posts()
    print()
    blog.update_post(1, title="Updated First Post")
    blog.show_posts()
    print()
    blog.delete_post(1)
    blog.show_posts()
    print()
    blog.reset()
    blog.show_posts()


if __name__ == '__main__':
    main()