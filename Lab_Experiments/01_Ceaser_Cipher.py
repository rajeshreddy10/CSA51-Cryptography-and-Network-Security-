message = input("Enter the message: ")
k = int(input("Enter the shift value (1-25): "))

if 1 <= k <= 25:
    encrypted = ""
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                encrypted += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            else:
                encrypted += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        else:
            encrypted += ch
    print("Encrypted Message:", encrypted)
    decrypted = ""
    for ch in encrypted:
        if ch.isalpha():
            if ch.isupper():
                decrypted += chr((ord(ch) - ord('A') - k) % 26 + ord('A'))
            else:
                decrypted += chr((ord(ch) - ord('a') - k) % 26 + ord('a'))
        else:
            decrypted += ch
    print("Decrypted Message:", decrypted)
else:
    print("Shift value must be between 1 and 25.")

    

'''
output:
Enter the message: i am good boy
Enter the shift value (1-25): 5
Encrypted Message: n fr ltti gtd
Decrypted Message: i am good boy
'''
