def convert_hex_to_dec(myhex):
    """
    Input: myhex - string
    Output: dec - integer
    """
    conversion = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
                  '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                  'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14',
                  'F': '15'}
    dec = 0
    for i, letter in enumerate(list(reversed(myhex))):
        dec += int(conversion[letter.upper()]) * 16**(i)
    return dec


if __name__ == "__main__":
    test_hexes = ['10CE', '7DE', '1D9', '80E1']
    for myhex in test_hexes:
        print("Decimal output of {}: {}".format(
            myhex, convert_hex_to_dec(myhex)))
