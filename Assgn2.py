from abc import ABC, abstractmethod

# Define the abstract Animal class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Implement subclasses for different animals
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"

# Create instances of the subclasses and call the sound method
dog = Dog()
cat = Cat()
cow = Cow()

print("Dog says:", dog.sound())
print("Cat says:", cat.sound())
print("Cow says:", cow.sound())
