import string
plain_alphabet = string.ascii_lowercase
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM".lower() 
cipher_map = {plain_alphabet[i]: cipher_alphabet[i] for i in range(26)}
reverse_map = {cipher_alphabet[i]: plain_alphabet[i] for i in range(26)}
message = input("Enter the message : ")
ciphertext = ""
for char in message.lower():
    if char in cipher_map:
        ciphertext += cipher_map[char]
    else:
        ciphertext += char
decrypted = ""
for char in ciphertext.lower():
    if char in reverse_map:
        decrypted += reverse_map[char]
    else:
        decrypted += char
print("Plaintext :", message)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)


'''
output:
Enter the message : MatrixMultiplication
Plaintext : MatrixMultiplication
Ciphertext: dqzkobdxszohsoeqzogf
Decrypted : matrixmultiplication
'''