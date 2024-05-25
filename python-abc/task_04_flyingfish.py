#!/usr/bin/python3

class Fish:
    # Define a class Fish.

    def swim(self):
        # Method to make the fish swim.
        print("The fish is swimming")

    def habitat(self):
        # Method to specify the habitat of the fish.
        print("The fish lives in water")


class Bird:
    # Define a class Bird.

    def fly(self):
        # Method to make the bird fly.
        print("The bird is flying")

    def habitat(self):
        # Method to specify the habitat of the bird.
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    # Define a class FlyingFish that inherits from both Fish and Bird.

    def fly(self):
        # Override the fly method to provide specific behavior for flying fish.
        print("The flying fish is soaring!")

    def swim(self):
        # Override the swim method to provide specific behavior for flying fish.
        print("The flying fish is swimming!")

    def habitat(self):
        # Override the habitat method to specify the habitat of flying fish.
        print("The flying fish lives both in water and the sky!")


flying_fish = FlyingFish()  # Create an instance of the FlyingFish class.
flying_fish.fly()  # Call the fly method of the FlyingFish instance.
flying_fish.swim()  # Call the swim method of the FlyingFish instance.
flying_fish.habitat()  # Call the habitat method of the FlyingFish instance.

print(FlyingFish.mro())  # Print the method resolution order (MRO) of the FlyingFish class.

