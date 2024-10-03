def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('А') if char.isupper() else ord('а')
            encrypted_char = chr((ord(char) - shift_base + shift) % 33 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    action = input("Выберите действие (зашифровать/расшифровать): ").strip().lower()
    shift = int(input("Введите сдвиг: "))
    text = input("Введите текст для шифрования/дешифрования: ")

    if action == "зашифровать":
        result = caesar_encrypt(text, shift)
        print("Зашифрованный текст:", result)
    elif action == "расшифровать":
        result = caesar_decrypt(text, shift)
        print("Расшифрованный текст:", result)
    else:
        print("Неверное действие. Пожалуйста, выберите 'encrypt' или 'decrypt'.")