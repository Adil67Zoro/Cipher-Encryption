import tkinter as tk
import string

def caesar_cipher_encode():
    shift = int(shift_entry.get())
    text = text_box_left.get("1.0", "end-1c")
    encoded_message_caesar = ""
    for c in text:
        if c.isalpha():
            if c.islower():
                encoded_message_caesar += chr((ord(c) - 97 + shift) % 26 + 97)
            else:
                encoded_message_caesar += chr((ord(c) - 65 + shift) % 26 + 65)
        else:
            encoded_message_caesar += c
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message_caesar)

def affine_cipher_encode():
    CHARACTERS = string.ascii_lowercase + " "
    slope = int(slope_entry.get())
    intercept = int(intercept_entry.get())
    text = text_box_left.get("1.0", "end-1c")
    encoded_message_affine = ""
    for c in text.lower():
        if c in CHARACTERS:
            index = CHARACTERS.index(c)
            encrypted_index = (slope * index + intercept) % len(CHARACTERS)
            encoded_message_affine += CHARACTERS[encrypted_index]
        else:
            encoded_message_affine += c
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message_affine)

def bacon_cipher_encode():
    bacon_dict = {
    'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb', 'e': 'aabaa',
    'f': 'aabab', 'g': 'aabba', 'h': 'aabbb', 'i': 'abaaa', 'j': 'abaab',
    'k': 'abaab', 'l': 'ababa', 'm': 'ababb', 'n': 'abbaa', 'o': 'abbab',
    'p': 'abbba', 'q': 'abbbb', 'r': 'baaaa', 's': 'baaab', 't': 'baaba',
    'u': 'baabb', 'v': 'baabb', 'w': 'babaa', 'x': 'babab', 'y': 'babba', 'z': 'babbb'
    }
    text = text_box_left.get("1.0", "end-1c")
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    encoded_message_bacon = ""
    name = " ".join(text)
    for char in name:
        if char.isalpha():
            encoded_message_bacon += bacon_dict[char]
        else:
            encoded_message_bacon += char
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message_bacon)

def vigenere_cipher_encode():
    text = text_box_left.get("1.0", "end-1c")
    keyword = keyword_entry.get()
    keyword = keyword.upper()
    encoded_message_vigenere = ""
    index = 0
    for char in text:
        if char.isalpha():
            key_char = keyword[index % len(keyword)]
            key = ord(key_char) - 65
            if char.isupper():
                encoded_message_vigenere += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encoded_message_vigenere += chr((ord(char) - 97 + key) % 26 + 97)
            index += 1
        else:
            encoded_message_vigenere += char
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message_vigenere)

def wig_wag_cipher_encode():
    wig_wag_dict = {
        "A": "o-o", "B": "-o-o", "C": "-o-o-", "D": "-o--o", "E": "o", "F": "oo-o", "G": "--o-", "H": "oooo", "I": "oo",
        "J": "o---o", "K": "-o-o-", "L": "o-o-o", "M": "--", "N": "-o", "O": "---", "P": "o--o", "Q": "--o-", "R": "o-o-",
        "S": "ooo", "T": "-", "U": "oo-", "V": "ooo-", "W": "o--", "X": "-oo-", "Y": "-o--", "Z": "--oo",
    }
    text = text_box_left.get("1.0", "end-1c")
    text = text.upper().replace(" ", "")
    encoded_message_wig_wag = ""
    for char in text:
        if char not in wig_wag_dict:
            continue
        encoded_message_wig_wag += (wig_wag_dict[char] + " ")
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message_wig_wag)

def dutch_spelling_alphabet_encode():
    dutch_alphabet_dict = {
        'A': 'Anton', 'B': 'Bernard', 'C': 'Cornelis', 'D': 'Dirk', 'E': 'Eduard',
        'F': 'Ferdinand', 'G': 'Gerrit', 'H': 'Hein', 'I': 'Isaak', 'J': 'Julius',
        'K': 'Karel', 'L': 'Leo', 'M': 'Maria', 'N': 'Nico', 'O': 'Otto',
        'P': 'Pieter', 'Q': 'Quotiënt', 'R': 'Rudolf', 'S': 'Simon', 'T': 'Theodoor',
        'U': 'Utrecht', 'V': 'Victor', 'W': 'Willem', 'X': 'Xantippe', 'Y': 'Ypsilon',
        'Z': 'Zaandam'
    }
    text = text_box_left.get("1.0", "end-1c")
    dutch_alphabet = []
    for char in text.upper():
        if char in dutch_alphabet_dict:
            dutch_alphabet.append(dutch_alphabet_dict[char])  
    encoded_message = " ".join(dutch_alphabet)
    text_box_right.delete("1.0", tk.END)
    text_box_right.insert(tk.END, encoded_message) 

def german_spelling_alphabet_encode():
    german_alphabet_dict = {
        'A': 'Anton', 'B': 'Berta', 'C': 'Cäsar', 'D': 'Dora', 'E': 'Emil',
        'F': 'Friedrich', 'G': 'Gustav', 'H': 'Heinrich', 'I': 'Ida', 'J': 'Julius',
        'K': 'Kaufmann', 'L': 'Ludwig', 'M': 'Martha', 'N': 'Nordpol', 'O': 'Otto',
        'P': 'Paula', 'Q': 'Quelle', 'R': 'Richard', 'S': 'Samuel', 'T': 'Theodor',
        'U': 'Ulrich', 'V': 'Viktor', 'W': 'Wilhelm', 'X': 'Xanthippe', 'Y': 'Ypsilon',
        'Z': 'Zacharias'
    }
    text = text_box_left.get("1.0", "end-1c")
    german_alphabet = []
    for char in text.upper():
        if char in german_alphabet_dict:
            german_alphabet.append(german_alphabet_dict[char])
    encoded_message = " ".join(german_alphabet)
    text_box_right.delete("1.0", tk.END)
    text_box_right.insert(tk.END, encoded_message) 

def italian_spelling_alphabet_encode():
    italian_alphabet_dict = {
        'A': 'Ancona', 'B': 'Bologna', 'C': 'Como', 'D': 'Domodossola', 'E': 'Empoli',
        'F': 'Firenze', 'G': 'Genova', 'H': 'Hotel', 'I': 'Imola', 'J': 'Jolly',
        'K': 'Kappa', 'L': 'Livorno', 'M': 'Milano', 'N': 'Napoli', 'O': 'Otranto',
        'P': 'Padova', 'Q': 'Quadro', 'R': 'Roma', 'S': 'Savona', 'T': 'Torino',
        'U': 'Udine', 'V': 'Venezia', 'W': 'Washington', 'X': 'Xeres', 'Y': 'Ipsilon',
        'Z': 'Zara'
    }  
    text = text_box_left.get("1.0", "end-1c")
    italian_alphabet = []
    for char in text.upper():
        if char in italian_alphabet_dict:
            italian_alphabet.append(italian_alphabet_dict[char])
        else:
            italian_alphabet.append(char)
    encoded_message = " ".join(italian_alphabet)
    text_box_right.delete("1.0", tk.END)
    text_box_right.insert(tk.END, encoded_message)

def nato_spelling_alphabet_encode():
    NATO_alphabet_dict = {
        "A":"Alpha", "B":"Bravo", "C":"Charlie", "D": "Delta", "E":"Echo", "F":"Foxtrot", 
        "G":"Golf", "H": "Hotel", "I":"India", "J":"Juliett", "K":"Kilo", "L":"Lima", "M":"Mike", "N":"November", 
        "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", 
        "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
    }
    text = text_box_left.get("1.0", "end-1c")
    NATO_alphabet = []
    for char in text.upper():
        if char in NATO_alphabet_dict:
            NATO_alphabet.append(NATO_alphabet_dict[char])
    encoded_message = " ".join(NATO_alphabet)
    text_box_right.delete("1.0", tk.END)
    text_box_right.insert(tk.END, encoded_message)

def enigma_encode():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
    
    text = text_box_left.get("1.0", "end-1c")
    rotor1_start_pos = int(rotor1_entry.get())
    rotor2_start_pos = int(rotor1_entry.get())
    rotor3_start_pos = int(rotor1_entry.get())
    encoded_message = ""
    for char in text.upper():
        if char not in alphabet:
            output += char
            continue

        rotor3_start_pos = (rotor3_start_pos + 1) % 26
        if rotor3_start_pos == alphabet.index(rotor3[0]):
            rotor2_start_pos = (rotor2_start_pos + 1) % 26
        if rotor2_start_pos == alphabet.index(rotor2[0]):
            rotor1_start_pos = (rotor1_start_pos + 1) % 26

        char_pos = alphabet.index(char)
        char_pos = (char_pos + rotor3_start_pos) % 26
        char_pos = alphabet.index(rotor3[char_pos])
        char_pos = (char_pos - rotor3_start_pos + rotor2_start_pos) % 26
        char_pos = alphabet.index(rotor2[char_pos])
        char_pos = (char_pos - rotor2_start_pos + rotor1_start_pos) % 26
        char_pos = alphabet.index(rotor1[char_pos])

        char_pos = (char_pos - rotor1_start_pos + 26) % 26
        char_pos = alphabet.index(reflector[char_pos])

        char_pos = (char_pos + rotor1_start_pos) % 26
        char_pos = rotor1.index(alphabet[char_pos])
        char_pos = (char_pos - rotor1_start_pos + 26) % 26
        char_pos = alphabet.index(rotor2[char_pos])
        char_pos = (char_pos + rotor2_start_pos) % 26
        char_pos = rotor2.index(alphabet[char_pos])
        char_pos = (char_pos - rotor2_start_pos + 26) % 26
        char_pos = alphabet.index(rotor3[char_pos])
        char_pos = (char_pos + rotor3_start_pos) % 26
        char_pos = rotor3.index(alphabet[char_pos])

        encoded_message += alphabet[char_pos]
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message)

def morse_code_encode():
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-', ' ': ' '
    } 
    text = text_box_left.get("1.0", "end-1c")
    encoded_message = ""
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])  
    encoded_message = " ".join(morse_code)
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message)    

def reverse_encode():     
    text = text_box_left.get("1.0", "end-1c")
    encoded_message = text[::-1]
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message)    

def swiss_k_encode():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    rotor1 = 'PEZUOHXSCVFMTBGLRINQJWAYDK'
    rotor2 = 'ZOUESYDKFWPCIQXHMVBLGNJRAT'
    rotor3 = 'EHRVXGAOBQUSIMZFLYNWKTPDJC'

    reflector = 'IMETCGFRAYSQBZXWLHKDVUPOJN'
    rotor1_start_pos = int(rotor1_entry.get())
    rotor2_start_pos = int(rotor1_entry.get())
    rotor3_start_pos = int(rotor1_entry.get())    
    text = text_box_left.get("1.0", "end-1c")
    encoded_message = ""
    for char in text.upper():
        if char not in alphabet:
            encoded_message += char
            continue

        rotor3_start_pos = (rotor3_start_pos + 1) % 26
        if rotor3_start_pos == alphabet.index(rotor3[0]):
            rotor2_start_pos = (rotor2_start_pos + 1) % 26
        if rotor2_start_pos == alphabet.index(rotor2[0]):
            rotor1_start_pos = (rotor1_start_pos + 1) % 26

        char_pos = alphabet.index(char)
        char_pos = (char_pos + rotor3_start_pos) % 26
        char_pos = alphabet.index(rotor3[char_pos])
        char_pos = (char_pos - rotor3_start_pos + rotor2_start_pos) % 26
        char_pos = alphabet.index(rotor2[char_pos])
        char_pos = (char_pos - rotor2_start_pos + rotor1_start_pos) % 26
        char_pos = alphabet.index(rotor1[char_pos])

        char_pos = (char_pos - rotor1_start_pos + 26) % 26
        char_pos = alphabet.index(reflector[char_pos])

        char_pos = (char_pos + rotor1_start_pos) % 26
        char_pos = rotor1.index(alphabet[char_pos])
        char_pos = (char_pos - rotor1_start_pos + 26) % 26
        char_pos = alphabet.index(rotor2[char_pos])
        char_pos = (char_pos + rotor2_start_pos) % 26
        char_pos = rotor2.index(alphabet[char_pos])
        char_pos = (char_pos - rotor2_start_pos + 26) % 26
        char_pos = alphabet.index(rotor3[char_pos])
        char_pos = (char_pos + rotor3_start_pos) % 26
        char_pos = rotor3.index(alphabet[char_pos])

        encoded_message += alphabet[char_pos]  
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message)

def tap_code_encode():
    text = text_box_left.get("1.0", "end-1c")
    encoded_message = ""
    text = text.upper().replace('K', 'C') 
    encoded_message = ''
    for char in text:
        if char == ' ':
            encoded_message += ' '
            continue
        row, col = divmod(string.ascii_uppercase.index(char), 5) 
        encoded_message += '.' * (row + 1) + ' ' + '.' * (col + 1) + ' '
    text_box_right.delete("1.0", "end")
    text_box_right.insert("1.0", encoded_message) 
    

def dropdown_changed(*args):
    selected_option = dropdown_var.get()
    if selected_option == "Caesar cipher":
        shift_label.pack()
        shift_entry.pack()
        button_encode.config(command=caesar_cipher_encode)
    else:
        shift_label.pack_forget()
        shift_entry.pack_forget()
    
    if selected_option == "Affine cipher":
        slope_label.pack()
        slope_entry.pack()
        intercept_label.pack()
        intercept_entry.pack()
        button_encode.config(command=affine_cipher_encode)
    else:
        slope_entry.pack_forget()
        slope_label.pack_forget()
        intercept_entry.pack_forget()
        intercept_label.pack_forget()
    
    if selected_option == "Bacon cipher":
        button_encode.config(command=bacon_cipher_encode)
            
    if selected_option == "Vigenere cipher":
        keyword_label.pack()
        keyword_entry.pack()
        button_encode.config(command=vigenere_cipher_encode)
    else:
        keyword_label.pack_forget()
        keyword_entry.pack_forget()
    
    if selected_option == "Wig Wag cipher":
        button_encode.config(command=wig_wag_cipher_encode)    
    
    if selected_option == "Dutch spelling alphabet":
        button_encode.config(command=dutch_spelling_alphabet_encode)       
    
    if selected_option == "German spelling alphabet":
        button_encode.config(command=german_spelling_alphabet_encode)         
    if selected_option == "Italian spelling alphabet":
        button_encode.config(command=italian_spelling_alphabet_encode) 
    if selected_option == "NATO spelling alphabet":
            button_encode.config(command=nato_spelling_alphabet_encode)  

    if selected_option == "Enigma":
        rotor1_label.pack()
        rotor1_entry.pack()
        rotor2_label.pack()
        rotor2_entry.pack()
        rotor3_label.pack()
        rotor3_entry.pack()
        button_encode.config(command=enigma_encode)
    else:
        rotor1_label.pack_forget()
        rotor1_entry.pack_forget()
        rotor2_label.pack_forget()
        rotor2_entry.pack_forget()
        rotor3_label.pack_forget()
        rotor3_entry.pack_forget()     

    if selected_option == "Morse code":
        button_encode.config(command=morse_code_encode)  

    if selected_option == "Reverse":
        button_encode.config(command=reverse_encode) 
        
    if selected_option == "Swiss-K":
        rotor1_label.pack()
        rotor1_entry.pack()
        rotor2_label.pack()
        rotor2_entry.pack()
        rotor3_label.pack()
        rotor3_entry.pack()
        button_encode.config(command=swiss_k_encode)
    else:
        rotor1_label.pack_forget()
        rotor1_entry.pack_forget()
        rotor2_label.pack_forget()
        rotor2_entry.pack_forget()
        rotor3_label.pack_forget()
        rotor3_entry.pack_forget()
    
    if selected_option == "Tap code":
        button_encode.config(command=tap_code_encode)     


window = tk.Tk()
window.title("Cipher Encryption")
window.geometry("1000x500")

frame_left = tk.Frame(master=window, width=400, height=500)
frame_left.pack(side=tk.LEFT)
text_box_left=tk.Text(frame_left, width=50, height=18)
text_box_left.grid(row=0, column=0, sticky="")

frame_right = tk.Frame(master=window, width=400, height=500)
frame_right.pack(side=tk.RIGHT)
text_box_right=tk.Text(frame_right, width=50, height=18)
text_box_right.grid(row=0, column=0, sticky="")

frame_center = tk.Frame(master=window, width=200, height=500)
frame_center.pack()

dropdown_label = tk.Label(master=frame_center, text="Encoding method:")
dropdown_label.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
options = ["Caesar cipher", "Affine cipher", "Bacon cipher", 
           "Vigenere cipher", "Wig Wag cipher", 
           "Dutch spelling alphabet", "German spelling alphabet",
           "Italian spelling alphabet", "NATO spelling alphabet",
           "Enigma", "Morse code", "Reverse", "Swiss-K", "Tap code"
           ]
dropdown_var = tk.StringVar()
dropdown_var.set(options[0])
selected_option = dropdown_var.get()
dropdown = tk.OptionMenu(window, dropdown_var, *options, command=dropdown_changed)
dropdown.pack()


shift_label = tk.Label(master=window, text="Shift:")
shift_entry = tk.Entry(master=window)
shift_label.pack_forget()
shift_entry.pack_forget()

button_encode = tk.Button(master=window, text="Encode")
button_encode.pack()

slope_label = tk.Label(master=window, text="Slope:")
slope_entry = tk.Entry(master=window)    
slope_label.pack_forget()
slope_entry.pack_forget()
intercept_label = tk.Label(master=window, text="Intercept:")
intercept_entry = tk.Entry(master=window)    
intercept_label.pack_forget()
intercept_entry.pack_forget()

keyword_label = tk.Label(master=window, text="Keyword: ")
keyword_entry = tk.Entry(master=window)
keyword_label.pack_forget()
keyword_entry.pack_forget()

rotor1_label = tk.Label(master=window, text="Rotor 1:")
rotor1_entry = tk.Entry(master=window)
rotor1_label.pack_forget()
rotor1_label.pack_forget()

rotor2_label = tk.Label(master=window, text="Rotor 2:")
rotor2_entry = tk.Entry(master=window)
rotor2_label.pack_forget()
rotor2_label.pack_forget()

rotor3_label = tk.Label(master=window, text="Rotor 3:")
rotor3_entry = tk.Entry(master=window)
rotor3_label.pack_forget()
rotor3_label.pack_forget()


window.mainloop()


