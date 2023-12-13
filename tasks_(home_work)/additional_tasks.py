# https://github.com/WAKERONE237

# №1 (6kyu)If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.

def sum(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
print(sum(int(input("Введите число n:"))))  # Должно вернуть 23, так как 3, 5, 6 и 9 меньше 10 и делятся на 3 или 5

# №2 (5kyu)Write an algorithm that takes an array and
# moves all of the zeros to the end, preserving the order of the other elements.

def movin(arr):
    zero_count = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            zero_count += 1
            arr.pop(i)
        else:
            i += 1
    arr.extend([0] * zero_count)
    return arr

array = [0, 1, 0, 3, 12]
print(movin(array))

# №3 (5kyu) Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it('Pig latin is cool') # igPay atinlay say oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    words = text.split()
    result = []

    for word in words:
        if word.isalpha():
            result.append(word[1:] + word[0] + "ay")
        else:
            result.append(word)

    return ' '.join(result)


print(pig_it(input("Введите слово:")))

# №4 (5kyu)The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

def rgb(r, g, b):

    r = min(255, max(0, r))
    g = min(255, max(0, g))
    b = min(255, max(0, b))

    hex_r = format(r, '02X')
    hex_g = format(g, '02X')
    hex_b = format(b, '02X')

    result = hex_r + hex_g + hex_b
    return result

print(rgb(255, 255, 255))   # Вывод: "FFFFFF"
print(rgb(255, 255, 300))   # Вывод: "FFFFFF"
print(rgb(0, 0, 0))         # Вывод: "000000"
print(rgb(148, 0, 221))     # Вывод: "9400D3"

# №5 (4 kyu) Write a function called sumIntervals/sum_intervals that accepts an array of intervals,
# and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

def sum_of_intervals(intervals):
    merged_intervals = []

    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    for interval in sorted_intervals:
        if not merged_intervals or interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

    total_length = sum(end - start for start, end in merged_intervals)
    return total_length

intervals = [
    [1, 4],
    [7, 12],
    [3, 5]
]

result = sum_of_intervals(intervals)
print(result)
