print(3+4)

def fruit_basket_guessing_game(guess: list, secret: list) -> tuple:
    """
    This function compares two lists of fruits: guess and secret.
    
    - The guess list contains the fruits the player guessed.
    - The secret list contains the correct sequence of fruits.
    
    The function should compare these lists and return a tuple of two values:
    1. The number of fruits that are correct and in the correct position.
    2. The number of fruits that are correct but in the wrong position.
    
    Steps to solve:
    1. Loop through both lists and compare each fruit at the same index to count correct matches.
    2. Then check for correct fruits in the wrong position.
    
    Example:
    fruit_basket_guessing_game(['apple', 'banana', 'orange', 'grape'], ['apple', 'orange', 'banana', 'pear']) 
    should return (1, 2) because 'apple' is correct in the right position, and 'banana' and 'orange' are correct but in the wrong position.
    """
    a = 0
    b = 0

    for x in range(len(guess)):
        if guess[x] == secret[x]:
            a += 1
        elif guess[x] in secret:
            b += 1
    return (a, b)
            


print(fruit_basket_guessing_game(['apple', 'banana', 'orange', 'grape'], ['apple', 'orange', 'banana', 'pear']))
