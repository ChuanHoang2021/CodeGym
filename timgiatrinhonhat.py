def min_num(numbers):
    result = numbers[0]
    for num in numbers:
        if result > num:
            result = num
    return result
min_number = min_num([1,4,5,6,8,7,2,2])
print("Min number: ", min_number)