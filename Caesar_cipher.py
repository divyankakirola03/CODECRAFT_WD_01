def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            stay_in_alphabet = 65 if char.isupper() else 97
            result += chr((ord(char) - stay_in_alphabet + shift) % 26 + stay_in_alphabet)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User input
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == 'e':
    print("Encrypted Message:", encrypt(message, shift))
elif choice == 'd':
    print("Decrypted Message:", decrypt(message, shift))
else:
    print("Invalid choice.")