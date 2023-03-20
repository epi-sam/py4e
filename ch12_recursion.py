# started: 2023-03-14
# what: sidestep to learn recursion basics to solve ch12_following_links.py

# factorial function

## recursive 
def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n-1)
    print(f" -> factorial({n}) returns {return_value}")
    return return_value

factorial(5)

## iterative equivalent
def factorial(n):
     return_value = 1
     for i in range(2, n + 1):
         return_value *= i
     return return_value

factorial(5)

# traversing a nested list

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

len(names)

for idx, var in enumerate(names):
    print(idx, var)

# determine if nested items are of type 'list'
isinstance(names[0], list)
isinstance(names[1], list)
isinstance(names[1][1], list)
isinstance(names[1][1][0], list)

# define a recursive function to count list items

def count_leaf_items(item_list):
    """Recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += count_leaf_items(item)
        else:
            print(f"Counted leaf item \"{item}\"")
            count += 1
    return count

count_leaf_items(names)

# iterative equivalent

def count_leaf_items_loop(item_list):
    """Non-recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """

    count = 0
    stack = []
    current_list = item_list
    i = 0

    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue

        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1

count_leaf_items_loop(names)

# simple version
def is_palindrome(word):
    """Return True if word is a palindrome, False if not."""
    return word == word[::-1]

# recursive version, just for fun
# works from the outside in, until the last string is length 1 (or 0)
def is_palindrome(word):
	"""Return True if word is a palindrome, False otherwise"""
	if len(word) <= 1:
		return True
	else:
		return word[0] == word[-1] and is_palindrome(word[1:-1])


# Quicksort algorithm

# first get us some random numbers to sort
import random

def get_random_numbers(length, minimum = 1, maximum = 100):
    numbers = []
    for i in range(length):
          numbers.append(random.randint(minimum, maximum))
    
    return numbers

num_rand = get_random_numbers(20)
num_rand

# define quicksort algorithm

import statistics as stat

def quicksort(numbers):
     
     if len(numbers) <= 1:
          return numbers
     else:
          print("numbers = ", numbers)
          pivot = stat.median(
               [
               numbers[0],
               numbers[len(numbers) // 2],
               numbers[-1]
               ]
          )
          print("pivot = ", pivot)

          items_less, pivot_items, items_greater = (
               [n for n in numbers if n < pivot],
               [n for n in numbers if n == pivot],
               [n for n in numbers if n > pivot]
          )
          print("less = ", items_less)
          print("pivot_items = ", pivot_items)
          print("greater = ", items_greater)

          return(
               quicksort(items_less) +
               pivot_items +
               quicksort(items_greater)
          )


quicksort(num_rand)