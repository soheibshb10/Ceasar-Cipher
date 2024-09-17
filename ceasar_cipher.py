import string

text=input("Enter the text:")

text=string.ascii_letters
shifted_text=''.join(
chr((ord(char)-ord('A')+3)%26 +ord('A')) if char.isupper() else
chr((ord(char)-ord('a')+3)%26 +ord('a')) if char.islower() else char
for char in text
)


print(f"Original text: {text}")
print(f"Shifted text: {shifted_text}")
