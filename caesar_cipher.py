def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# -------- Main Program --------
print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

print("\nChoose an option:")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Enter 1 or 2: ")

if choice == "1":
    encrypted_text = encrypt(message, shift)
    print("\nEncrypted Message:", encrypted_text)

elif choice == "2":
    decrypted_text = decrypt(message, shift)
    print("\nDecrypted Message:", decrypted_text)

else:
    print("Invalid choice!")
