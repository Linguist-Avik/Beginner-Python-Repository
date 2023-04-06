from caesar_cipher_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(any_text, shift_amount, shift_direction):
    cipher_text = ""
    if shift_direction == "decode":
      shift_amount *= -1
    for char in any_text:
        if char in alphabet:
          position = alphabet.index(char)
          new_position = position + shift_amount
          cipher_text += alphabet[new_position % len(alphabet)]
        else:
          cipher_text += char
    print(f"The {shift_direction} text is: {cipher_text}")
counter = True
while counter:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  
  caesar(any_text=text, shift_amount=shift, shift_direction=direction)
  answer = input("\nWould like to restart Cipher?\nYes or No? ").lower()
  if answer == 'no':
    counter = False
    print('Goodbye')
    