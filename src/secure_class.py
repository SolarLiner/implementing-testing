"""A very secure and important class to implement, and later, to test"""

class VeryImportant(object):
    """This class is very secure and must be tested thouroughly."""
    def __init__(self, user_name):
        if not user_name:
            user_name = "John Doe"
        self.name = user_name

    def __str__(self):
        return "<VeryImportant: {}>".format(self.name)

    def say_hello():
        """Static function saying hello."""
        return "Hello!"

    def say_hello_instance(self):
        """Instance method calling for name."""
        return "Hello {}!".format(self.name)