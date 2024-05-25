#!/usr/bin/python3

class CountedIterator:
    # Define a custom iterator class named CountedIterator.

    def __init__(self, iterable):
        # Constructor method to initialize the CountedIterator object with an iterable.
        self.iterator = iter(iterable)  # Get an iterator from the iterable.
        self.count = 0  # Initialize a counter to keep track of the number of iterations.

    def __iter__(self):
        # Define the __iter__ method to make the object an iterable.
        return self  # Return the iterator itself.

    def __next__(self):
        # Define the __next__ method to iterate over the elements of the iterable.
        try:
            item = next(self.iterator)  # Get the next item from the iterator.
            self.count += 1  # Increment the counter for each iteration.
            return item  # Return the item.
        except StopIteration:
            # If there are no more items to iterate, raise StopIteration with a message.
            raise StopIteration("No items to iterate")

    def get_count(self):
        # Method to get the count of iterations.
        return self.count  # Return the count.

iterable = [1, 2, 3, 4, 5]  # Define an iterable (list in this case).
counted_iter = CountedIterator(iterable)  # Create an instance of the CountedIterator with the iterable.

for item in counted_iter:
    print(item)  # Iterate over the items and print each item.

print("Number of items iterated:", counted_iter.get_count())  # Print the count of iterations.

