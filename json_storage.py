import json
from config import PATH


BLOG_POSTS = [
    {
        "id": 1,
        "author": "Alice Smith",
        "title": "Getting Started with Python",
        "content": "Python is a beginner-friendly programming language used worldwide."
    },
    {
        "id": 2,
        "author": "Bob Johnson",
        "title": "Why Learn Django?",
        "content": "Django helps developers build secure and scalable web applications quickly."
    },
    {
        "id": 3,
        "author": "Charlie Brown",
        "title": "Top 5 VS Code Extensions",
        "content": "These extensions can greatly improve your productivity while coding."
    },
    {
        "id": 4,
        "author": "Diana Miller",
        "title": "Understanding APIs",
        "content": "APIs allow different software systems to communicate with each other."
    },
    {
        "id": 5,
        "author": "Ethan Wilson",
        "title": "Introduction to Git",
        "content": "Git is a version control system that tracks changes in your code."
    },
    {
        "id": 6,
        "author": "Fiona Davis",
        "title": "CSS Tips for Beginners",
        "content": "Learning Flexbox and Grid makes modern layouts much easier."
    },
    {
        "id": 7,
        "author": "George Taylor",
        "title": "Debugging Made Simple",
        "content": "Effective debugging saves time and improves software quality."
    },
    {
        "id": 8,
        "author": "Hannah Moore",
        "title": "SQLite with Python",
        "content": "SQLite is a lightweight database perfect for small applications."
    },
    {
        "id": 9,
        "author": "Ian Thomas",
        "title": "Working with JSON Data",
        "content": "JSON is commonly used for storing and exchanging structured data."
    },
    {
        "id": 10,
        "author": "Julia Anderson",
        "title": "Deploying Your First Website",
        "content": "Deploying a website is easier today thanks to cloud platforms and automation."
    }
]


def load_json(path):
    """
    The function loads a JSON file from the specified path.
    """
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    """
    This function saves a JSON file to the specified path.
    """
    with open(path, 'w') as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def main():
    save_json(PATH, BLOG_POSTS)
    blog_posts = load_json(PATH)
    for block_post in blog_posts:
        print(block_post)


if __name__ == '__main__':
    main()