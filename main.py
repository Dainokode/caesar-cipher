from database import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
while shift >= 38:
    print("Choose a shift number between 1 and 38")
    shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_amount, direction):
    output_text = ""

    for letter in plain_text:
        if letter in alphabet:
            if direction == "encode":
                letter_index = alphabet.index(letter) + shift_amount
                output_text += alphabet[letter_index]
            elif direction == "decode":
                letter_index = alphabet.index(letter) - shift_amount
                output_text += alphabet[letter_index]
        else:
            output_text += letter

    print(f"The {direction}d text is {output_text}\n")


caesar(plain_text=text, shift_amount=shift, direction=direction)

user_choice = input(
    "Would you like to restart or stop the program? Type 'yes' or 'no'\n").lower()

while user_choice != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift >= 38:
        print("Choose a shift number between 1 and 38\n")
        shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=shift, direction=direction)
    user_choice = input(
        "Would you like to restart or stop the program? Type 'yes' or 'no'\n").lower()
