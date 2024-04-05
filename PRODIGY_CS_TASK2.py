from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Convert the image to RGB mode
    img = img.convert("RGB")

    # Create a new image for encryption
    encrypted_img = Image.new("RGB", (width, height))

    # Encrypt each pixel in the image
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            # XOR the pixel values with the key
            r ^= key
            g ^= key
            b ^= key
            encrypted_img.putpixel((x, y), (r, g, b))

    return encrypted_img

def decrypt_image(encrypted_img, key):
    width, height = encrypted_img.size

    # Create a new image for decryption
    decrypted_img = Image.new("RGB", (width, height))

    # Decrypt each pixel in the image
    for y in range(height):
        for x in range(width):
            r, g, b = encrypted_img.getpixel((x, y))
            # XOR the pixel values with the key
            r ^= key
            g ^= key
            b ^= key
            decrypted_img.putpixel((x, y), (r, g, b))

    return decrypted_img

# Example usage:
image_path = "/content/image1.png"
key = 123  # Key for encryption
encrypted_img = encrypt_image("/content/image1.png", key)
encrypted_img.save("encrypted_image.jpg")
decrypted_img = decrypt_image(encrypted_img, key)
decrypted_img.save("decrypted_image.jpg")
