def count_string(txt):
    result = 0
    for char in txt:
        result += 1
    return result

input_str = input('Your string: ')

print('Length: ', count_string(input_str))

