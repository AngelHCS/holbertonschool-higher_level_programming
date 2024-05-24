from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass

class Dog(Animal):
    """
    Subclass of Animal representing a dog.
    """

    def sound(self):
        """
        Returns the sound of a dog, which is 'Bark'.
        """
        return "Bark"

class Cat(Animal):
    """
    Subclass of Animal representing a cat.
    """

    def sound(self):
        """
        Returns the sound of a cat, which is 'Meow'.
        """
        return "Meow"

if __name__ == "__main__":
    # Instantiate a Dog object and a Cat object
    bobby = Dog()
    garfield = Cat()

    # Print the sounds of the dog and the cat
    print(bobby.sound())   # Output: Bark
    print(garfield.sound())  # Output: Meow

    # Attempt to instantiate an Animal object directly
    animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods sound
    print(animal.sound())

