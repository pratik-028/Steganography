import cv2
import os

# Load encrypted image
image_path = "encryptedImage.png"
img = cv2.imread(image_path)

if img is None:
    print("Error: Encrypted image not found.")
    exit()

# Load saved password
try:
    with open("password.txt", "r") as f:
        saved_password = f.read().strip()
except FileNotFoundError:
    print("Error: Password file not found.")
    exit()

# Input passcode for decryption
pas = input("Enter passcode for Decryption: ")


if saved_password == pas:
    msg_length = int(img[0, 0][0]) * 256 + int(img[0, 0][1])
    # Create ASCII-to-character mappings
    c = {}

    for i in range(256):
        c[i] = chr(i)
    n, m, z = 1, 1, 0
    message = ""
    for i in range(msg_length):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
        print("YOU ARE NOT auth")