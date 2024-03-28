def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    
    return result
text = "Привет, мир!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)