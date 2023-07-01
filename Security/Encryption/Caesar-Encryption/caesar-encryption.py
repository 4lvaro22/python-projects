def caesar_cypher(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def asking_text():
    text = input("What message do you want to encrypt?\n")
    return text

if __name__ == "__main__":
    text = asking_text()
    print("Encrypted text: " + caesar_cypher(text, 3))