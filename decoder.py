
ALPHABET = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
    14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
    26: 'Z'
}

PUNCTUATION = {1: '!', 2: '?', 3: ',', 4: '.', 5: ' ', 6: ';', 7: '"', 8: "'"}
# defaults to U = uppercase
MODE = {'mode': 'U'}
final_message = []
msg_code_list = []


def check_mode(current_mode):
    """
    checks current mode
    """
    if current_mode['mode'] in ['U', 'L']:
        return 27
    return 9


def update_mode(current_mode):
    """
    updates mode according to cycle U => L => P, then back to U
    """
    if current_mode['mode'] == 'U':
        current_mode['mode'] = 'L'
        return

    if current_mode['mode'] == 'L':
        current_mode['mode'] = 'P'
        return

    if current_mode['mode'] == 'P':
        current_mode['mode'] = 'U'
        return


def manage_case(m, c):
    # character upper or lower case
    if m == 'U':
        return c.upper()
    if m == 'L':
        return c.lower()


def create_message(c):
    final_message.append(c)


def finalize_message(f):
    print(f)
    return "".join(f)


def recursive_string(full_msg, c_code):
    if not full_msg:
        return msg_code_list
    for char in full_msg:
        if char == ',':
            # remove the comma
            char = ''
            # append the character code to message code list
            msg_code_list.append(c_code)
            # empty character_code variable for new code
            c_code = ''
        c_code += char
        # walk the full message
        return recursive_string(full_msg[1:], c_code)


def process_message(m):

    character_code = ''
    # processing message 1 char at a time to determine the character codes
    msg = recursive_string(m, character_code)

    for number_string in msg:
        # check mode determine our modulo divisor, 27 or 9; then divide
        mode_modulo = check_mode(MODE)
        num = int(number_string) % mode_modulo
        # if remainder, change modes (upper/lower/punctuation)
        if num == 0:
            update_mode(MODE)
        else:
            # modulo divisor is 9, we need a punctuation character, else we need a alpha character
            if mode_modulo == 9:
                char = PUNCTUATION[num]
            else:
                # get alpha character and change case (upper/lower) based on mode
                char = ALPHABET[num]
                char = manage_case(MODE['mode'], char)
            # save to message array
            create_message(char)
    # finalize message
    print(finalize_message(final_message))


def main():
    """
    Decode a message:

    for...
    """
    message = '18,12312,171,763,98423,1208,216,11,500,18,241,0,32,20620,27,10'
    process_message(message)


if __name__ == '__main__':
    main()
