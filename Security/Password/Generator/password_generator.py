import random, string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

password_length = 20
generate_password = generate_password(password_length)
print(generate_password)

