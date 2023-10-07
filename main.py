import random

username = input("Enter Username: ")
print("WELCOME TO THE PYTHON NUMBER GUESSING GAME")

while True:
    ran = random.randint(1,10000000000000000000000000000000000000000000000000000000000000000000)
    comp_guess = random.randint(1,ran)
    print(F"\nTHE NUM IS IN BETWEEN 1 to {ran}")
    try:
        user_guess = input("Enter a Number: ")
    except Exception as err:
        print(f"Error: {err}")

    if comp_guess == user_guess:
        print("CONGRATULATIONS USER YOU GOT IT RIGHT!")
        with open("hiscore.txt", "a") as f:
            f.write("A new User has created a Hiscore.")
    elif comp_guess > user_guess:
        print("Too Low.")
    elif comp_guess < user_guess:
        print("Too High")
