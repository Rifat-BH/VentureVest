# -*- coding: utf-8 -*-
"""AES_Encryption.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10-GXitzn8fvpjTjsmWCT3XqdWzapKC61
"""

print("hi crypto")

# !pip install pycrypto

# !pip install --upgrade --force-reinstall pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Function to pad the data to be a multiple of 16
def pad(data):
    length = 16 - (len(data) % 16)
    return data + bytes([length]) * length

# Function to encrypt the image
def encrypt_image(input_file, output_file, key):
    # Generate a random initialization vector
    iv = get_random_bytes(16)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(input_file, 'rb') as f:
        data = f.read()

    # Pad the data to be a multiple of 16 bytes
    padded_data = pad(data)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    # Write the IV and encrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(iv)
        f.write(encrypted_data)

# Example usage
if __name__ == "__main__":
    # Specify input and output file paths
    input_file = 'image.png'
    output_file = 'encrypted_image.jpg'

    # Generate a random 16-byte key
    key = os.urandom(16)

    # Encrypt the image
    encrypt_image(input_file, output_file, key)
    print(key)

    print("Image encrypted successfully.")

# from Crypto.Cipher import AES

# Function to remove padding from the decrypted data
