def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # If the character is not an alphabet, leave it unchanged
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            # If the character is not an alphabet, leave it unchanged
            decrypted_text += char
    return decrypted_text


input_text = input("Enter Your text you want to encrypt :")
shift = int(input("Enter shift :"))
encrypted_text = caesar_encrypt(input_text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
