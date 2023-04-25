from Crypto.Cipher import AES
import base64
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Key should be 16, 24, or 32 bytes long
key = b'Sixteen byte key'
iv = b'This is an IV456'


def pad(s):
    """Pad the text to be a multiple of 16 bytes"""
    return s + (AES.block_size - len(s) % AES.block_size) * (bytes([AES.block_size - len(s) % AES.block_size]))


def encrypt_message():
    """Encrypt the user input message"""
    message = entry.get()
    bytes_message = message.encode('utf-8')
    padded_text = pad(bytes_message)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(padded_text)
    encoded_cipher_text = base64.b64encode(cipher_text).decode()
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert('1.0', encoded_cipher_text)
    output_text.config(state=tk.DISABLED)


def decrypt_message():
    """Decrypt the user input cipher"""
    cipher_text = entry.get()
    try:
        decoded_cipher_text = base64.b64decode(cipher_text.encode())
    except base64.binascii.Error:
        messagebox.showerror("Error", "Invalid base64-encoded cipher text.")
        return
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(decoded_cipher_text)
    unpadded_text = decrypted_padded_text[:-decrypted_padded_text[-1]]
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert('1.0', unpadded_text.decode())
    output_text.config(state=tk.DISABLED)


def copy_message():
    """Copy the encrypted or decrypted message to the clipboard"""
    message = output_text.get('1.0', tk.END)
    pyperclip.copy(message)


# Create the main window
root = tk.Tk()
root.title('Encryption and Decryption App')

# Create the input label and entry box
label = tk.Label(root, text='Enter your message or cipher:')
label.pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create the encrypt button
encrypt_button = tk.Button(root, text='Encryption', height=4, command=encrypt_message)
encrypt_button.pack(pady=5)

# Create the decrypt button
decrypt_button = tk.Button(root, text='Decryption', height=4, command=decrypt_message)
decrypt_button.pack(pady=5)

# Create the output label and text box
output_label = tk.Label(root, text='Output:')
output_label.pack(pady=5)
output_text = tk.Text(root, height=5, width=40, wrap=tk.WORD)
output_text.pack(pady=5)
output_text.config(state=tk.DISABLED)

# Create the copy button
copy_button = tk.Button(root, text='Copy', height=4, command=copy_message)
copy_button.pack(pady=5)

# Run the GUI
root.mainloop()
