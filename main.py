# Assignment - 1 Text to Morse code and Morse code to Text converter
text_to_morse_code = {'A': '.-', 'B': '-...',
                      'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-',
                      '?': '..--..', '/': '-..-.', '-': '-....-',
                      '(': '-.--.', ')': '-.--.-', ' ': '/',
                      '@': '.--.-.', '!': '-.-.--', ':': '---...',
                      ',': '--..--', "'": '.----.', '"': '.-..-.'}

morse_code_to_text = {'.-': 'A', '-...': 'B',
                      '-.-.': 'C', '-..': 'D', '.': 'E',
                      '..-.': 'F', '--.': 'G', '....': 'H',
                      '..': 'I', '.---': 'J', '-.-': 'K',
                      '.-..': 'L', '--': 'M', '-.': 'N',
                      '---': 'O', '.--.': 'P', '--.-': 'Q',
                      '.-.': 'R', '...': 'S', '-': 'T',
                      '..-': 'U', '...-': 'V', '.--': 'W',
                      '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                      '.----': '1', '..---': '2', '...--': '3',
                      '....-': '4', '.....': '5', '-....': '6',
                      '--...': '7', '---..': '8', '----.': '9',
                      '-----': '0', ', ': '--..--', '.-.-.-': '.',
                      '..--..': '?', '-..-.': '/', '-....-': '-',
                      '-.--.': '(', '-.--.-': ')', '/': ' ',
                      '.--.-.': '@', '-.-.--': '!', '---...': ":",
                      '--..--': ',', '.----.': "'", '.-..-.': '"'}

print("\n!!! WELCOME TO TEXT TO MORSE CODE AND MORSE TO TEXT CONVERTER !!!\n\n")

# These characters are cannot translate to morse code
invalid_char = ['~', '`', '#', '$', '%', '^', '*', '|', '<', '>', '[', ']', '{', '}', ';']

is_converter_on = True

# loop for converter
while is_converter_on:
    text_list = []
    morse_list = []
    # Ask user to choose which converter they want to use
    choose = input("Type 'T' for Text to morse Converter or Type 'M' for Morse to Text Converter: ").upper()

    if choose == 'T':
        user_input = input('Enter Text To Convert in Morse Code: ').upper()
        for letter in user_input:
            if letter in invalid_char:
                print(f"'{letter}' is invalid character.")
                print("'~', '`', '#', '$', '%', '^', '*', '|', '<', '>', '[', ']', '{', '}', ';' Cannot translate "
                      "these Character.")
                morse_list = []
                break
            else:
                morse_list.append(text_to_morse_code[letter])

        if morse_list:
            print(f'Morse Code Output: {" ".join(morse_list)}\n')

    elif choose == 'M':
        user_input = input("Type your Morse code using '.', '-' or '_', separating "
                           "letters by spaces and words by '/' : ")

        morse_input = user_input.split(' ')
        # Check if user put blank space at last of morse code
        if '' in morse_input:
            # remove blank elements form list
            for _ in morse_input:
                try:
                    morse_input.remove('')
                except ValueError:
                    pass

            # remove last index (i.e. blank space)
            for letter in morse_input:
                try:
                    text_list.append(morse_code_to_text[letter])
                except KeyError:
                    print('Invalid_Morse_Code_error')
                    text_list = []
                    break

        else:
            for letter in morse_input:
                try:
                    text_list.append(morse_code_to_text[letter])
                except KeyError:
                    print('Invalid_Morse_Code_error')
                    text_list = []
                    break

        if text_list:
            print(f'Text Output: {"".join(text_list)}\n')

    elif choose == 'EXIT':
        is_converter_on = False
