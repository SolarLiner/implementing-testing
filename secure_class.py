"""A very secure and important class to implement, and later, to test"""

class VeryImportant(object):
    """This class is very secure and must be tested thouroughly."""
    def __init__(name="John Doe"):
        self.name = name

    def __str__(self):
        return self.name

    def say_hello():
        """Static function saying hello."""
        return "Hello!"

    def say_hello(self):
        """Instance method calling for name."""
        return "hello {}!".format(self.name)