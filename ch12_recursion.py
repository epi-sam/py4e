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

for key, var in enumerate(names):
    print(key, var)