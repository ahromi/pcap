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
betul = "Well done, muggle! You are free now"
salah = "Ha ha! You're stuck in my loop!"
ask = int(input("Input your number: "))
while ask:
    if ask != secret_number:
        print(salah)
        ask = int(input("Input your number: "))
    else:
        print("Your number is: ", ask)
        print(betul)
        exit()
exit()