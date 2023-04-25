from Crypto.Cipher import AES
import base64
import tkinter as tk
from tkinter import messagebox

# Key should be 16, 24, or 32 bytes long
key = b'Sixteen byte key'
iv = b'This is an IV456'

# Create a tkinter window
root = tk.Tk()
root.title("Decryption App")

# Create a label for the input field
label_input = tk.Label(root, text="Enter the base64-encoded cipher text:")
label_input.pack()

# Create an entry field for the input
entry_input = tk.Entry(root, width=50)
entry_input.pack()

# Create a label for the output field
label_output = tk.Label(root, text="Decrypted message:")
label_output.pack()

# Create a text field for the output
text_output = tk.Text(root, width=50, height=5)
text_output.pack()

# Function to decrypt the message
def decrypt():
    # Get the input from the user
    encoded_cipher_text = entry_input.get()

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

    # Show the output in the text field
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, text)

# Function to copy the output to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text_output.get(1.0, tk.END))
    messagebox.showinfo("Copied", "The output has been copied to clipboard.")

# Create a button to decrypt the message
button_decrypt = tk.Button(root, text="Decrypt", command=decrypt)
button_decrypt.pack()

# Create a button to copy the output to clipboard
button_copy = tk.Button(root, text="Copy Output", command=copy_to_clipboard)
button_copy.pack()

# Start the GUI
root.mainloop()

