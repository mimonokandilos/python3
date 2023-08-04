# oop_concepts.py

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Child class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Child class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Test cases for OOP concepts
if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    animals = [dog, cat]
    for animal in animals:
        print(animal.speak())

