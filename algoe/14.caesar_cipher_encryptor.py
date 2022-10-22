import string


def caesar_cipher(s, shifter):


    alphabet = list(string.ascii_lowercase)
    new_shifter = shifter % 26
    new_string = []
    for i in range(len(s)):
        alpha_idx = alphabet.index(s[i])
        total_idx = alpha_idx + new_shifter

        if total_idx > len(s):
            norm_shifter = (total_idx % 25) -1
            new_string.append( alphabet[norm_shifter])
        else:
            new_string.append(  alphabet[i+shifter])

    return "".join(new_string)


if __name__=="__main__":
    print(caesar_cipher("xyz", 2))
