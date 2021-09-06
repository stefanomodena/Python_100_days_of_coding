alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser(encrypt_direction, plain_text, shift_amount):
   cipher_text = ""
   if encrypt_direction == "decode":
       shift_amount *= -1
   for char in plain_text:
      if char in alphabet:
         position = alphabet.index(char)   
         new_position = position + shift_amount
         cipher_text += alphabet[new_position]
      else:
         cipher_text += char
     
   print(f"The {encrypt_direction}d text is: {cipher_text}")

continuar = True
while continuar:
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   text = input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))

   shift = shift % 26

   caeser(encrypt_direction = direction, plain_text = text, shift_amount = shift)

   resultado = input("Type 'yes' if you want to go again. Otherwise type 'no'. >> ")
   if resultado == "no":
      continuar = False
      print("Goodbye")