#!/usr/bin/python3

class SwimMixin:
    # Define a mixin class SwimMixin.

    def swim(self):
        # Method to make the dragon swim.
        print("The creature swims!")


class FlyMixin:
    # Define a mixin class FlyMixin.

    def fly(self):
        # Method to make the dragon fly.
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    # Define a class Dragon that inherits from SwimMixin and FlyMixin.

    def roar(self):
        # Method to make the dragon roar.
        print("The dragon roars!")


draco = Dragon()  # Create an instance of the Dragon class.

draco.swim()  # Call the swim method inherited from SwimMixin.
draco.fly()
draco.roar()

