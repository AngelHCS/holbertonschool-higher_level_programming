#!/usr/bin/python3

class VerboseList(list):
    # Define a custom list class named VerboseList that inherits from the built-in list class.

    def append(self, item):
        # Override the append method of the list class.
        super().append(item)  # Call the append method of the parent class.
        print(f"Added {item} to the list.")  # Print a message indicating the item added to the list.

    def extend(self, items):
        # Override the extend method of the list class.
        super().extend(items)  # Call the extend method of the parent class.
        print(f"Extended the list with {len(items)} items.")  # Print a message indicating the number of items extended.

    def remove(self, item):
        # Override the remove method of the list class.
        if item in self:
            # Check if the item exists in the list.
            print(f"Removed {item} from the list.")  # Print a message indicating the item removed from the list.
        else:
            print(f"{item} not found in the list.")  # Print a message if the item is not found.
        super().remove(item)  # Call the remove method of the parent class to remove the item.

    def pop(self, index=None):
        # Override the pop method of the list class.
        if index is not None:
            # Check if an index is specified.
            item = super().pop(index)  # Call the pop method of the parent class with the specified index.
            print(f"Popped {item} from the list.")  # Print a message indicating the item popped from the list.
            return item  # Return the popped item.
        else:
            item = super().pop()  # Call the pop method of the parent class without an index (pops the last item).
            print(f"Popped {item} from the list.")  # Print a message indicating the item popped from the list.
            return item  # Return the popped item.

