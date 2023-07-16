from .connection import db


class Post:
    def __init__(self, imageUrl: str, description: str) -> None:
        self.imageUrl = imageUrl
        self.description = description

    def save_to_collection(self) -> None:
        db["posts"].insert_one(
            {'imageUrl': self.imageUrl, 'description': self.description})
