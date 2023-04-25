from Crypto.Cipher import AES
import base64
import binascii

# Key should be 16, 24, or 32 bytes long
key = b'Sixteen byte key'
iv = b'This is an IV456'

# Prompt the user for input
message = input("Enter your message: ")

# Convert the message to bytes using UTF-8 encoding
bytes_message = message.encode('utf-8')

# Pad the text to be a multiple of 16 bytes
pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * (bytes([AES.block_size - len(s) % AES.block_size]))
padded_text = pad(bytes_message)

# Create the cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt the text
cipher_text = cipher.encrypt(padded_text)

# Convert the cipher text to binary
binary_cipher = binascii.hexlify(cipher_text)

# Encode the cipher text as base64 for transmission/storage
encoded_cipher_text = base64.b64encode(cipher_text).decode()

# Print the encrypted message and binary cipher
print("Encrypted Message: "+ encoded_cipher_text)
print("Binary Cipher: " + binary_cipher.decode())
