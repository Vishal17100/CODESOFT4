import random
import string

def generate_password(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(len))
    return password

def main():
    len = int(input("Enter the desired length of the password: "))
    password = generate_password(len)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()