import random
import string

def generate_password(length=12):
#Define a function to generate a random password.
    
#Define a string containing all possible characters for the password.
    characters = string.ascii_letters + string.digits + string.punctuation
    
#Generate a password by selecting random characters from the defined set.
    password = ''.join(random.choice(characters) for _ in range(length))
    
#Return the generated password.
    return password

if __name__ == "__main__":
#This block of code is executed when the script is run.
    
    print("Random Password Generator")
    print("------------------------")
    
#Get the desired password length from the user.
    password_length = int(input("Enter the desired password length: "))
    
#Call the generate_password function to create a new password.
    new_password = generate_password(password_length)
    
#Display the generated password.
    print(f"\nGenerated Password: {new_password}")
