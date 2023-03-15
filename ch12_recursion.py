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