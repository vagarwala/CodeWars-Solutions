def whitespace_number(n):
    def binary(n):
        s = ''
        for char in bin(n)[2:]:
            if char == '1':
                s += '\t'
            else:
                s += ' '
        return s
    if n > 0:
        return ' ' + binary(n) + '\n'
    elif n == 0:
        return " \n"
    else:
        return '\t' + binary((-1)*n) + '\n'