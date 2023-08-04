# test_module_package.py
import unittest
import oop_concepts as oc
import my_module
from my_package import math_operations

class TestModulePackage(unittest.TestCase):

    def test_oop_concepts(self):
        dog = oc.Dog("Buddy")
        cat = oc.Cat("Whiskers")
        self.assertEqual(dog.speak(), "Buddy says Woof!")
        self.assertEqual(cat.speak(), "Whiskers says Meow!")

    def test_my_module(self):
        self.assertEqual(my_module.greet("Alice"), "Hello, Alice!")

    def test_my_package_math_operations(self):
        self.assertEqual(math_operations.add(2, 3), 5)
        self.assertEqual(math_operations.subtract(5, 2), 3)

if __name__ == "__main__":
    unittest.main()

