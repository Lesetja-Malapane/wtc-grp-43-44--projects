a = 0
b = 0

def fruit_basket_guessing_game(guess, secret):
    for x in range(len(guess)):
            if guess[x] == secret[x]:
                a += 1
            elif guess[x] in secret:
                b += 1
    return (a, b)
            
fruit_basket_guessing_game(['apple', 'banana', 'orange', 'grape'], ['apple', 'orange', 'banana', 'pear'])

