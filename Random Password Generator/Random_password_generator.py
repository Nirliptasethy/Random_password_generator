import random
import string
import time
print("==== Random Password Generator ===")
generation_count = 0
MAX_GENERATIONS = 10
WAIT_TIME = 600  # 10 minutes = 600 seconds
while(True):
    # Check generation limit
    if generation_count >= MAX_GENERATIONS:
        print("\nYou have reached the maximum limit of 10 passwords.")
        print("Please wait 10 minutes before generating again.")

        for remaining in range(WAIT_TIME, 0, -1):
            minutes = remaining // 60
            seconds = remaining % 60
            print(f"\rWait time: {minutes:02d}:{seconds:02d}", end="")
            time.sleep(1)

        print("\nYou can generate passwords again!")
        generation_count = 0
    # Get password lenght
    try:
        length=int(input("\n Enter password length (maximum 8):"))
        if length>8:
            print("\nsorry...your input lenght can't be more than 8....try again")
            continue
    except ValueError:
        print("Error....please enter a valid number")
        continue
    # Character type section
    print("\n Choose character type :")
    print("1.Uppercase letter")
    print("2.Lowercase letter")
    print("3.Number")
    print("4.symbols")
    choice=input("enter choice (example :1234):")
    # validation chracter choice
    valid_choices = set("1234")

    if not set(choice).issubset(valid_choices):
        print("Error: Please select only 1, 2, 3, or 4.")
        continue

    if len(set(choice)) < 2:
        print("Error: Select at least 2 character types.")
        continue
    character=" "
    if "1" in choice:
        character +=string.ascii_uppercase
    if "2" in choice:
        character +=string.ascii_lowercase
    if "3" in choice:
        character +=string.digits
    if "4" in choice:
        character +=string.punctuation
    # Generate password
    password=" "
    for i in range(length):
        password += random.choice(character)

    generation_count += 1

    print("\nGenerated Password:", password)
    print(f"Passwords generated: {generation_count}/10")

    # Generate another
    again = input("\nGenerate another password? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the Password Generator!")
        break
    