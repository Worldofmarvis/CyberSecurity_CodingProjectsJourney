from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

message = "This is a secret message!".encode()

cipher_text = cipher_suite.encrypt(message)
print("Cipher Text:", cipher_text)

plain_text = cipher_suite.decrypt(cipher_text)
print("Plain Text:", plain_text.decode())

if plain_text == message:
    print("Yes, both are the same")