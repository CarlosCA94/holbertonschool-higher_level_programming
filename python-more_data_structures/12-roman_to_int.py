#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
    result = 0
    for n in range(len(roman_string)):
        if romans.get(roman_string[n], 0) == 0:
            return (0)
        elif (n != (len(roman_string) - 1) and
              romans[roman_string[n]] < romans[roman_string[n + 1]]):
            result += romans[roman_string[n]] * - 1
        else:
            result += romans[roman_string[n]]
    return result
