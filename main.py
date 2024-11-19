alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser_enc(plain_text, shift_value):
    ceaser_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_value) % 26  # function for encryption
            ceaser_text += alphabet[new_position]
        else:
            ceaser_text += char
    print(ceaser_text)


def ceaser_dec(plain_text, shift_value):
    ceaser_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_value) % 26  # function for decryption
            ceaser_text += alphabet[new_position]
        else:
            ceaser_text += char
    print(ceaser_text)

def main():
    flag = False
    while not flag:
        type = input("what you need encryption or decryption?\ne or d \n")
        
        text = input("enter plain text\n").lower()      #if user enter caps leeter also converted into small
        shift = int(input("enter shift value\n"))
        
        if type == "e":
            ceaser_enc(plain_text=text, shift_value=shift)
            
        elif type == "d":
            ceaser_dec(plain_text=text, shift_value=shift)
            
        again = input("want to try again yes or no?")
        
        if again == "no":
            flag = True
            print("good bye have a nice day..")
        elif again != "yes":
            flag = True
            print("good bye have a nice day..")   #if user not enters yes or no it exits
main()


