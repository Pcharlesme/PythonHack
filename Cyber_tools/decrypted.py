from Crypto.Cipher import AES
import base64

# Key should be 16, 24, or 32 bytes long
key = b'Sixteen byte key'
iv = b'This is an IV456'

# Prompt the user to enter the base64-encoded cipher text
encoded_cipher_text = input("Enter the base64-encoded cipher text: ")

# Decode the base64-encoded cipher text
cipher_text = base64.b64decode(encoded_cipher_text)

# Create the cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the cipher text
padded_text = cipher.decrypt(cipher_text)

# Remove the padding
unpadded_text = padded_text[:-ord(padded_text[-1:])]

# Convert bytes to string
text = unpadded_text.decode('utf-8')

print(text)
