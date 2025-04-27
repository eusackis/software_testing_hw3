import unittest
from Comment import Comment, comment_validator  

class TestCommentValidator(unittest.TestCase):

    def test_valid_comment(self):
        comment = Comment(text="This is a safe comment", rating=5)
        result = comment_validator(comment)
        self.assertEqual(result, {'rating': 5, 'comment': "This is a safe comment"})

    def test_text_not_string(self):
        comment = Comment(text=12345, rating=5)
        with self.assertRaises(TypeError) as context:
            comment_validator(comment)
        self.assertIn("Expected comment to be str", str(context.exception))

    def test_text_too_short(self):
        comment = Comment(text="Hi", rating=5)
        with self.assertRaises(ValueError) as context:
            comment_validator(comment)
        self.assertIn("Comment should be 3 - 300 characters long", str(context.exception))

    def test_text_too_long(self):
        comment = Comment(text="A" * 301, rating=5)
        with self.assertRaises(ValueError) as context:
            comment_validator(comment)
        self.assertIn("Comment should be 3 - 300 characters long", str(context.exception))

    def test_text_with_prohibited_characters(self):
        bad_texts = ['Bad, comment', 'Wrong(comment)', 'Dangerous; text', 'Dot.', 'Quote"here', "Single'quote", "Percent%"]
        for bad_text in bad_texts:
            with self.subTest(bad_text=bad_text):
                comment = Comment(text=bad_text, rating=5)
                with self.assertRaises(ValueError) as context:
                    comment_validator(comment)
                self.assertIn("Comment contains prohibited characters", str(context.exception))

    def test_rating_not_integer(self):
        comment = Comment(text="Valid text", rating="five")
        with self.assertRaises(TypeError) as context:
            comment_validator(comment)
        self.assertIn("Expected rating to be int", str(context.exception))

    def test_rating_too_low(self):
        comment = Comment(text="Valid text", rating=0)
        with self.assertRaises(ValueError) as context:
            comment_validator(comment)
        self.assertIn("Comment rating must range from 1 to 10", str(context.exception))

    def test_rating_too_high(self):
        comment = Comment(text="Valid text", rating=11)
        with self.assertRaises(ValueError) as context:
            comment_validator(comment)
        self.assertIn("Comment rating must range from 1 to 10", str(context.exception))

if __name__ == '__main__':
    unittest.main()