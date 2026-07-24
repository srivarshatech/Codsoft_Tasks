import random
import string


def display_header():
    print("=" * 45)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 45)

def build_character_pool():
    characters = ""

    lowercase = input("Include lowercase letters? (y/n): ").lower()
    if lowercase == "y":
        characters += string.ascii_lowercase

    uppercase = input("Include uppercase letters? (y/n): ").lower()
    if uppercase == "y":
        characters += string.ascii_uppercase

    digits = input("Include numbers? (y/n): ").lower()
    if digits == "y":
        characters += string.digits

    special = input("Include special characters? (y/n): ").lower()
    if special == "y":
        characters += string.punctuation

    if characters == "":
        print("You must select at least one character type.")
        return build_character_pool()

    return characters


def get_password_length():
    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length <= 0:
                print("Password length must be greater than 0.")
                continue

            return length

        except ValueError:
            print("Please enter a valid integer.")


def generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))


def main():
    display_header()

    while True:
        length = get_password_length()
        characters = build_character_pool()
        password = generate_password(length, characters)

        print("\n" + "=" * 45)
        print(f"Generated Password: {password}")
        print("=" * 45)

        choice = input("\nGenerate another password? (y/n): ").lower()

        while choice not in ("y", "n"):
            choice = input("Please enter only 'y' or 'n': ").lower()

        if choice == "n":
            print("\nThank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()
    