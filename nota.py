#Funcion para descifrar el texto cifrado con ROT13
def decrypt_rot13(text):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr(((ord(char) - ord('a') - 13) % 26) + ord('a'))
            else:
                decrypted_text += chr(((ord(char) - ord('A') - 13) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

#Leemos el texto cifrado desde el archivo
file_path = 'Nota..txt'
with open(file_path, 'r') as file:
    encrypted_text = file.read()

#Desciframos el texto
decrypted_text = decrypt_rot13(encrypted_text)

print("Texto descifrado:")
print(decrypted_text)

#Escribimos el texto descifrado al final del archivo readme.txt
with open('README.md', 'a') as file:
    file.write('\n\n')
    file.write('Texto descifrado:\n')
    file.write(decrypted_text)

# Imprimir mensaje de confirmación
print('\nTexto descifrado agregado al archivo readme.txt.')