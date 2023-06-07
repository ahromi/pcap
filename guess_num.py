secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess = int(input("Input your guess number: "))

while guess:
    if guess != secret_number:
        print("Ha ha! You're stuck in my loop! You input the wrong number:", guess)
        guess = int(input("Input your guess number: "))
    else:
        print("Well done, muggle! You are free now.")
        exit()
exit()
