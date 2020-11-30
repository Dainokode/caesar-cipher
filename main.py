alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_amount, direction):
    output_text = ""

    for letter in plain_text:
        if direction == "encode":
            letter_index = alphabet.index(letter) + shift_amount
        elif direction == "decode":
            letter_index = alphabet.index(letter) - shift_amount
        else:
            print("You entered a wrong keyword, try typing 'encrypt' to encode a message or 'decrypt' to decode a message.")

        output_text += alphabet[letter_index]

    print(f"The {direction}d text is {output_text}")


caesar(plain_text=text, shift_amount=shift, direction=direction)
