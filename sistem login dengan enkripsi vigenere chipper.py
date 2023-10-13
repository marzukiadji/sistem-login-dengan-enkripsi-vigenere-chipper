# Fungsi enkripsi Vigenère Cipher
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_len = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % key_len].upper()) - 65  # Menggunakan huruf kapital untuk kunci
            if char.isupper():
                encrypted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
            else:
                encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi dekripsi Vigenère Cipher
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_len = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = ord(key[i % key_len].upper()) - 65
            if char.isupper():
                decrypted_char = chr(((ord(char) - 65 - shift) % 26) + 65)
            else:
                decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Contoh penggunaan
key = "SECRET"
username = "Alice"
password = "Password123"

# Enkripsi username dan password sebelum penyimpanan atau transmisi
encrypted_username = vigenere_encrypt(username, key)
encrypted_password = vigenere_encrypt(password, key)

# Simpan atau kirim encrypted_username dan encrypted_password

# Kemudian, saat login, dekripsi kembali username dan password
decrypted_username = vigenere_decrypt(encrypted_username, key)
decrypted_password = vigenere_decrypt(encrypted_password, key)

# Periksa apakah username dan password yang di-dekripsi cocok dengan input pengguna
if decrypted_username == username and decrypted_password == password:
    print("Login berhasil")
else:
    print("Login gagal")
