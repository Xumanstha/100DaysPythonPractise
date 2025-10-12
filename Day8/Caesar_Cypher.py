Alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text=input("Enter the text for encrpytion or decryption:")
shift=int(input("enter the shift amount for encryption or decryption:"))



def Encrypt(original_text,shift_amount):
    original_text=original_text.lower()
    encrypted_message=""
    for letter in original_text:
        if letter in Alphabets:
            position=Alphabets.index(letter)
            new_position=(position+shift_amount)%25
            new_letter=Alphabets[new_position]

        encrypted_message=encrypted_message+new_letter
    return encrypted_message

print(Encrypt(text,shift))

def Decrypt(original_text,shift_amount):
    original_text=original_text.lower()
    encrypted_message=""
    for letter in original_text:
        if letter in Alphabets:
            position=Alphabets.index(letter)
            new_position=(position-shift_amount)%25
            new_letter=Alphabets[new_position]

        encrypted_message=encrypted_message+new_letter
    return encrypted_message

print(Decrypt("khoor",3))
