#!/usr/bin/env python
import sys
# phone number mnemonic - return all character sequences for a phone number

keypad = {
    '1': [], '2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'], '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'], '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z'], '*': [], '0': [], '#': []
}

def phone (phone_number):
# well, I'm lazy for tests=(
    """
    >>> phone(['2'])
    ['A', 'B', 'C']
    >>> phone(['1'])
    []
    >>> phone(['2', '3'])
    ['AD', 'BD', 'CD', 'AE', 'AF', 'BE', 'BF', 'CE', 'CF']
    >>> phone(['2', '9', '4'])
    ['AWG', 'BWG', 'CWG', 'AXG', 'AYG', 'AZG', 'BXG', 'BYG', 'BZG', 'CXG', 'CYG', 'CZG', 'AWH', 'AWI', 'BWH', 'BWI', 'CWH', 'CWI', 'AXH', 'AXI', 'AYH', 'AYI', 'AZH', 'AZI', 'BXH', 'BXI', 'BYH', 'BYI', 'BZH', 'BZI', 'CXH', 'CXI', 'CYH', 'CYI', 'CZH', 'CZI']
    """
    result = [letter for letter in keypad[phone_number[0]]]
    for key in phone_number[1:len(phone_number)]:
        for j in range(len(result)):
            i = 0
            old_result = result[j]
            for letter in keypad[key]:
                word = old_result + letter
                if i == 0:
                    result[j] = word
                else:
                    result.append(word)
                i += 1
        # result.append(''.join(letters))
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False, optionflags= doctest.REPORT_ONLY_FIRST_FAILURE)
    #print phone(['2', '9', '4'])
