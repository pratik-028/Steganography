import cv2
import os

# Load image
image_path = r"mypic.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found or cannot be opened.")
    exit()

# Input message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

msg_length = len(msg)
img[0, 0] = (msg_length // 256, msg_length % 256, 0)

height, width, _ = img.shape
max_capacity = (height * width * 3) - 2  # Reserve 2 pixels for metadata
if msg_length > max_capacity:
    print("Error: Message too long to fit in the image.")
    exit()

# Create character-to-ASCII mappings
d = {}


for i in range(256):
    d[chr(i)] = i

# Initialize pixel positions
n, m, z = 1, 1, 0

# Encrypt the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save encrypted image
encrypted_image_path = "encryptedImage.png"
cv2.imwrite(encrypted_image_path, img)
print(f"Encrypted image saved as {encrypted_image_path}")

# Save password in a text file
with open("password.txt", "w") as f:
    f.write(password)

# Open the image (Windows)
os.system(f"start {encrypted_image_path}")
