from cryptography.fernet import Fernet

# === Generate a new key ===
key = Fernet.generate_key()

# === Save the key to use later ===
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# === Encrypt the file ===
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)
    print(f"{file_path} ➡ {file_path}.encrypted created.")

# === Decrypt the file ===
def decrypt_file(encrypted_file_path, key):
    f = Fernet(key)
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    original_file = encrypted_file_path.replace('.encrypted', '')
    with open(original_file, 'wb') as file:
        file.write(decrypted_data)
    print(f"{encrypted_file_path} ➡ {original_file} restored.")

# === Optional: Create example.txt if it doesn't exist ===
with open("example.txt", "w") as file:
    file.write("This is a secret message.")
print("example.txt created.")

# === Run encryption and decryption ===
encrypt_file("example.txt", key)
decrypt_file("example.txt.encrypted", key)
