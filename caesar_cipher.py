def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

text = input("Enter text: ")
key = int(input("Enter key (number): "))

if choice == 'e':
    print("Encrypted:", encrypt(text, key))
elif choice == 'd':
    print("Decrypted:", decrypt(text, key))
else:
    print("Invalid choice.")
