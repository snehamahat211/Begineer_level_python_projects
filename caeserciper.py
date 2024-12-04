from asci import logo
print(logo)

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesert(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=='decode':
        shift_amount*=-1
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=letter
    print(f"THE {cipher_direction}d code is {end_text}")



should_continue=True
while should_continue:
    direction=input("enter you want 'encode' or 'decode': ")
    text=input("type your message:\n").lower()
    shift=int(input("type the shift number:\n"))
    shift=shift%25
    caesert(start_text=text, shift_amount=shift,cipher_direction=direction)
    result=input("type 'yes' to continue and 'no' to finish the game \n" ).lower()
    if result=="no":
        should_continue=False
        print("good bye")



