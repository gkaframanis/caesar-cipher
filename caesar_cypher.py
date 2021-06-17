import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(f"{art.logo}\n")

def caesar(start_text, shift, direction):
    end_text = ""
    shift = shift % 26
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                if (position + shift) > 25:
                    end_text += alphabet[position + shift - 26]
                else:
                    end_text += alphabet[position + shift]
            else:
                if (position - shift) < 0:
                    end_text += alphabet[position - shift + 26]
                else:
                    end_text += alphabet[position - shift]
        else:
            end_text += letter
    print(f"The {direction}d text is {end_text}.")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift=shift, direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if result == "no":
        should_continue = False
        print("Goodbye")