def vigenere_encrypt(plain_text, key):
    """
    Encrypts the given plain text using the Vigenère cipher with the provided key.

    Args:
    plain_text (str): The text to be encrypted.
    key (str): The key for encryption.

    Returns:
    str: The encrypted text.
    """
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            # Determine the shift value based on the key
            shift = ord(key[i % key_length].upper()) - ord('A')

            # Encrypt the current character
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            # Preserve non-alphabetic characters
            encrypted_text += char

    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    """
    Decrypts the given encrypted text using the Vigenère cipher with the provided key.

    Args:
    encrypted_text (str): The text to be decrypted.
    key (str): The key for decryption.

    Returns:
    str: The decrypted text.
    """
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            # Determine the shift value based on the key
            shift = ord(key[i % key_length].upper()) - ord('A')

            # Decrypt the current character
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            # Preserve non-alphabetic characters
            decrypted_text += char

    return decrypted_text

# Example usage:
plain_text = "baunbeklzlqskqkebgcjyhvskr"
key = "tncy"
decrypted_text = vigenere_encrypt(plain_text, key)

print("Plain Text:", plain_text)
print("Key:", key)
print("Decrypted Text:", decrypted_text)