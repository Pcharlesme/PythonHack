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


def copy_message():
    """Copy the encrypted message to the clipboard"""
    message = output_text.get('1.0', tk.END)
    pyperclip.copy(message)


# Create the main window
root = tk.Tk()
root.title('Encryption App')

# Create the input label and entry box
label = tk.Label(root, text='Enter your message:')
label.pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create the encrypt button
encrypt_button = tk.Button(root, text='Encrypt', command=encrypt_message)
encrypt_button.pack(pady=5)

# Create the output label and text box
output_label = tk.Label(root, text='Encrypted Message:')
output_label.pack(pady=5)
output_text = tk.Text(root, fg= 'green', height=5, width=40, wrap=tk.WORD, bg='gray90')
output_text.pack(pady=5)
output_text.config(state=tk.DISABLED)

# Create the copy button
copy_button = tk.Button(root, text='Copy', command=copy_message)
copy_button.pack(pady=5)

# Run the GUI
root.mainloop()
