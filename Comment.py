import re

class Comment:
    def __init__(self, text: str = None, rating: int = None):
        self.text = text
        self.rating = rating

def comment_validator(comment: Comment):
    if type(comment.text) is not str:
        raise TypeError(f"Comment is not accepted. Expected comment to be str, got {type(comment.text)} instead.")

    if not (3 <= len(comment.text) <= 300):
        raise ValueError("Comment should be 3 - 300 characters long.")

    if re.search(r'[\"\'\;\.\(\)\%,]', comment.text):
        raise ValueError("Comment contains prohibited characters.")

    if type(comment.rating) is not int:
        raise TypeError(f"Rating is not accepted. Expected rating to be int, got {type(comment.rating)} instead.")

    if not (1 <= comment.rating <= 10):
        raise ValueError(f"Comment rating must range from 1 to 10, got {comment.rating} instead.")

    return {'rating': comment.rating, 'comment': comment.text}

