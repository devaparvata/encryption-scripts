# pip install python-magic
# Debian/Ubuntu
# sudo apt-get install libmagic1
# Windows
# pip install python-magic-bin

import os
import magic

def detect_mime_type(file_path):
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path)

def detect_file_extension(file_path):
    mime = magic.Magic()
    return mime.from_file(file_path)

def reverse_hex(data):
    # Convert data to hexadecimal
    hex_data = data.hex()
    # Reverse the hexadecimal string
    reversed_hex_data = hex_data[::-1]
    # Convert the reversed hexadecimal data back to bytes
    reversed_data = bytes.fromhex(reversed_hex_data)
    return reversed_data

def get_file():
    file_name = input("Enter the initial file name: ")
    return file_name

def save_to_file(data, file_name):
    with open(file_name, 'wb') as f:
        f.write(data)

# Step 1: Get the file name from the user and change .txt
file_name = get_file()

# Step 2: Read the content of the initial file
try:
    with open(file_name, 'rb') as f:
        initial_data = f.read()
except FileNotFoundError:
    print("Initial file not found.")
    exit()

print("\n")
print("Initial file:")
print("    Name:", file_name)
print("    MIME type:", detect_mime_type(file_name))
print("    Real file extension:", detect_file_extension(file_name))

# Step 3: Reverse the hex value of the initial file and save it as the second file
base_name, extension = os.path.splitext(file_name)
second_file_name = "reversed_" + base_name + "_" + extension[1:] + ".txt"
reversed_data = reverse_hex(initial_data)
save_to_file(reversed_data, second_file_name)
print("\n")
print("Reversed file:")
print("    Name:", second_file_name)
print("    MIME type:", detect_mime_type(second_file_name))
print("    Real file extension:", detect_file_extension(second_file_name))
