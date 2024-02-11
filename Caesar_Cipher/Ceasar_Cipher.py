import art
def caesar(start_text, shift_amount, direction):
    end_message = ""
    if direction == "decode":
        shift_amount*= -1
    for letters in start_text:
        if letters in alphabet:
            index_letter = alphabet.index(letters)
            end_index_letter = index_letter + shift_amount
            end_message += alphabet[end_index_letter]
        else:
            end_message += letters
    print(end_message)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
turn_off = False
while turn_off == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, direction=direction)
    turnof = input("Do you wanna quit the program? (YES/NO)").lower()
    if turnof == "yes":
        turn_off = True
    else:
        turn_off = False

