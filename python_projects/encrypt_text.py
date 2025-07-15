
def encrypt(message):
    nato_alphabet = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
        'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
        'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }

    encrypted_message=""

    for char in message:
        if char.upper() in nato_alphabet:
            encrypted_message += nato_alphabet[char.upper()] + " "
        else:
            encrypted_message += char
    return encrypted_message


message = input("Enter a message to encrypt:- ")
encrypted_message = encrypt(message)
print("Encrypted message:", encrypted_message)