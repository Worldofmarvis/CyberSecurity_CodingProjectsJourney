def caesar_decode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

cipher_text = input("Enter text to decode: ")
shift_value = int(input("Enter shift value: "))
print("Decoded text:", caesar_decode(cipher_text, shift_value))