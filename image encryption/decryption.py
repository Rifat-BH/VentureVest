from Crypto.Cipher import AES

def unpad(data):
    return data[:-data[-1]]

# Function to decrypt the image
def decrypt_image(input_file, output_file, key):
    # Read the IV and encrypted data from the input file
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove padding
    unpadded_data = unpad(decrypted_data)

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(unpadded_data)

# Example usage
if __name__ == "__main__":
    # Specify input and output file paths
    input_file = 'encrypted_image.jpg'
    output_file = 'decrypt.jpg'


    key = b"\xc8\xc6C\x00\xfa\x8e\x10\xd7\x84z\xea\x9b'\xbcFF"

    # Decrypt the image
    decrypt_image(input_file, output_file, key)

    print("Image decrypted successfully.")

# !pip install pycrypto