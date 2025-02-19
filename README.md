

# **SECURE DATA HIDING IN IMAGES USING STEGANOGRAPHY**  

## **Overview**  
This project implements steganography to securely hide and retrieve messages inside images. It modifies pixel values to store secret data, ensuring confidentiality. The decryption process requires a passcode, preventing unauthorized access.  

## **Features**  
✅ Encrypt a message inside an image.  
✅ Secure the message with a passcode.  
✅ Decrypt and retrieve the message only with the correct passcode.  
✅ Uses OpenCV for image processing.  

## **Technologies Used**  
- Python   
- OpenCV (`cv2` module)
- OS Library 

## **Installation**  
Ensure you have Python installed. Then, install the required dependencies:  
```bash
pip install opencv-python
```  

## **How It Works**  

### **Encryption Process**  
Run the `encryption.py` script to embed a secret message in an image.  
```bash
python encryption.py
```  
1. Enter the secret message.  
2. Provide a passcode for security.  
3. The script encrypts the message inside the image pixels.  
4. The encrypted image is saved as `encryptedImage.png`.  
5. The passcode is stored in `password.txt`.  

### **Decryption Process**  
Run the `decryption.py` script to extract the hidden message.  
```bash
python decryption.py
```  
1. Enter the passcode.  
2. If correct, the hidden message is displayed.  
3. If incorrect, access is denied.  

## **File Structure**  
- `encryption.py` → Hides the message inside an image.  
- `decryption.py` → Retrieves the hidden message from the image.  
- `password.txt` → Stores the passcode.  
- `encryptedImage.png` → The output image containing the secret data.  

## **Limitations & Future Improvements**  
🚫 Passcode stored as plaintext (`password.txt`).  
🚫 Message length depends on image size.  
🔹 Improve encryption strength.  
🔹 Use a more secure passcode storage method.  
