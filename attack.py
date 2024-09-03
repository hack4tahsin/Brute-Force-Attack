import hashlib

# Function to hash a given password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to perform a dictionary attack using a wordlist
def dictionary_attack(hashed_password, wordlist):
    attempts = 0

    # Open the wordlist file and iterate over each line (password guess)
    with open(wordlist, 'r') as file:
        for line in file:
            # Remove any leading/trailing whitespace characters
            guess = line.strip()
            guess_hash = hash_password(guess)
            attempts += 1

            # Check if the hash of the current guess matches the target hash
            if guess_hash == hashed_password:
                return guess, attempts

    return None, attempts


# Main part of the script
if __name__ == "__main__":
    # Get user input for the password
    password = input("Enter the password to hash and attack: ")
    hashed_password = hash_password(password)

    print(f"SHA-256 Hash of the password: {hashed_password}")

    # Specify the path to your wordlist file
    wordlist_path = 'wordlist.txt'  # Replace with the path to your wordlist file

    # Perform the dictionary attack
    print("\nStarting Brute Force Attack...")
    found_password, attempts = dictionary_attack(hashed_password, wordlist_path)

    if found_password:
        print(f"\nPassword found: {found_password}")
        print(f"Attempts: {attempts}")
    else:
        print("\nPassword not found in the wordlist.")
