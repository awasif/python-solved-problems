#Code Encription and description 

alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(orginal_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
            shift_amount *= -1
    for letter in orginal_text:
        if letter not in alphabets:
            output_text+=letter
        else:
          shifted_position=alphabets.index(letter)+shift_amount
          shifted_position %= len(alphabets)
          output_text+=alphabets[shifted_position]
    print(f"Here is {encode_or_decode}d result:{output_text}")

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt ,Type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type your shift number:\n"))

    caesar(orginal_text=text,shift_amount=shift,encode_or_decode=direction) 

    restart = input("Type 'yes' if you want to go again.Otherwise , type 'no' .\n").lower()
    if restart== "no":
      should_continue==False
      print("Goodbye")

def encrypt(orginal_text,shift_amount):
    cipher_text=""

    for letter in orginal_text:
        shifted_position=alphabets.index(letter)+shift_amount
        shifted_position %= len(alphabets)
        cipher_text+=alphabets[shifted_position]
    print(f"Here is encoded result:{cipher_text}")

def decrypt(orginal_text,shift_amount):
    output_text=""

    for letter in orginal_text:
        shifted_position=alphabets.index(letter)-shift_amount
        shifted_position %= len(alphabets)
        output_text+=alphabets[shifted_position]
    print(f"Here is decoded result:{output_text}")






encrypt(orginal_text=text,shift_amount=shift)
decrypt(orginal_text=text,shift_amount=shift)

