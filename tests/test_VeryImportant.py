import pytest
from src.secure_class import *

class TestVeryImportant(object):
    very_important = VeryImportant("Nathan")

    def test_hello_static(self):
        print "Static hello()"
        assert VeryImportant.say_hello() == "Hello!"
    
    def test_hello_instance(self):
        print "Instance hello()"
        assert self.very_important.say_hello() == "Hello Nathan!"
        assert self.very_important.say_hello() != "Hello John Doe!" # Default case in constructor

    def test_class_str(self):
        print "Class __str__()"
        assert very_important.__str__() == "<VeryImportant: Nathan>"
