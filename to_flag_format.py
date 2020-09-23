flag_to_convert = input('Enter the string to convert to flag: ')

def convert(flag):
    result = ''
    for i in flag:
        if i == 'o' or i == 'O':
            result += '0'
        elif i == 's' or i == 'S':
            result += '5'
        elif i == 'g' or i == 'G':
            result += '6'
        elif i == ' ':
            result += '_'
        elif i == 'e' or i == 'E':
            result += '3'
        else:
            result += i
    return result
print(convert(flag_to_convert))
