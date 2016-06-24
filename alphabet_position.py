def alphabet_position(text):
    import string
    punc = string.punctuation
    for char in text:
        if char in punc or char in '1234567890':
            text = text.replace(char, '')
    text = text.replace(' ', '')
    text = text.lower()
    alphabet = string.ascii_lowercase
    res = ''
    for char in text:
        res += str(alphabet.index(char) + 1) + ' '
    return res[:-1]