import string

def caesar_cipher(text, key):
    shifted_text = ''
    for char in text:
        if char.isupper():
            shifted_text += chr(ord('A') + (ord(char) - ord('A') + key) % 26)
        elif char.islower():
            shifted_text += chr(ord('a') + (ord(char) - ord('a') + key) % 26)
        else:
            shifted_text += char
    return shifted_text


text=input("Enter the text:")
key =int(input("Enter the shift key (number):"))
shifted_text=''
text=str(text)

shifted_text=caesar_cipher(text,key)

print(f"Original text: {text}")
print(f"Shifted text: {shifted_text}")
