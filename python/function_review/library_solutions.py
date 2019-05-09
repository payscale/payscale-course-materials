def count_capitals(string):
    count = 0
    for char in string:
        if char.isalpha() and char == char.upper():
            count += 1
    return count


def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u", "y"]
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


def reverse_string(string):
    # fancy way: return string[::-1]
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

