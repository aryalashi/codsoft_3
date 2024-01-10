import random
import string

used_passwords = set()

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation
    else:
        print("Invalid complexity option. Using medium complexity.")
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_password_used(password):
    return password in used_passwords

def add_used_password(password):
    used_passwords.add(password)

def main():
    try:
        length = int(input("Enter the length of the password: "))
        complexity = input("Choose complexity (easy/medium/hard): ").lower()
        
        if complexity not in ["easy", "medium", "hard"]:
            print("Invalid complexity option. Using medium complexity.")
            complexity = "medium"

        if length <= 0:
            print("Invalid input. Please enter a positive length.")
        else:
            while True:
                password = generate_password(length, complexity)
                if not is_password_used(password):
                    print("Generated Password:", password)
                    add_used_password(password)
                    break
                else:
                    print("Password already generated. Generating a new one...")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
