#!/usr/bin/env python3

# Global list defined here before functions
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Look at last item, add 1, append it
    last_item = ordered_list[-1]
    ordered_list.append(last_item + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    # Remove all occurrences of items_to_remove from ordered_list
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)

# Main block for testing
if __name__ == '__main__':
    print(my_list)  # Original list
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)  # After adding 3 items
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)  # After removing items
