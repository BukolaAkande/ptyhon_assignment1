import string
import random

characters = list(string.ascii_letters + string.hexdigits + string.digits + string.punctuation)

def specific_length_password():
    #length of password from the user
    length = int(input ("Enter password length: "))
    # shuffling the characters
    random.shuffle(characters)

    # picking random characters from the list
    password = []
    for m in range(length):
        password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    # printing the list
    print("".join(password))

#invoking the function
specific_length_password()

