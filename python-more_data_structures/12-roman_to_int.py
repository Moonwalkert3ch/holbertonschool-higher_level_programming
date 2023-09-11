#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return (0)
    sum = 0
    numbers = {"X": 10, "V": 5, "I": 1, "L": 50, "D": 500, "C": 100, "M": 1000}
    for roman in reversed(roman_string):
        numeral = numbers[roman]
        sum += numeral if sum < numeral * 5 else -numeral
    return (sum)
