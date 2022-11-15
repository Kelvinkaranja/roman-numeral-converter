#Make necessary imports
from collections import Counter
import re
#Populate a dictionary with comparing values
roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
         'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

#create a function that asks for input
def string():
    string = input('ENTER A ROMAN NUMERAL: ')
    return string.upper()

#Checker for validity of string
def valid_roman_numeral(string):
    valid = (
        re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", string))
    if valid:
        return True
    else:
        return False


def slicer(string):
    combos = []
    st = string.upper()
    while 'CD' in st or 'CM' in st:
        combo = st[st.index('C')]+st[st.index('C')+1]
        combos.append(combo)
        st = st[0:st.index('C')]+st[st.index('C')+2:]
        if 'CD' not in st and 'CM' not in st:
            break
    while 'XC' in st or 'XL' in st:
        combo = st[st.index('X')]+st[st.index('X')+1]
        combos.append(combo)
        st = st[0:st.index('X')]+st[st.index('X')+2:]
        if 'XC' not in st and 'XL' not in st:
            break

    while 'IV' in st or 'IX' in st:
        combo = st[st.index('I')]+st[st.index('I')+1]
        combos.append(combo)
        st = st[0:st.index('I')]+st[st.index('I')+2:]
        if 'IV' not in st and 'IX' not in st:
            break
    remainder = list(st)

    return remainder, combos


def roman_converter(a, b):
    combos = len(b)
    x = 0
    total1 = 0
    original = len(a)
    y = 0
    total2 = 0
    if combos > 0:
        while combos > 0:
            total1 = total1+roman[b[x]]
            x = x+1
            combos = combos-1

    if original > 0:
        while original > 0:
            total2 = total2+roman[a[y]]
            y = y+1
            original = original-1
    return total1+total2


#LOGIC
string = string()
valid = valid_roman_numeral(string)
if not valid:
    print(f'{string} not a valid Roman Numeral')
else:
    a, b = slicer(string)
    arabic = roman_converter(a, b)
    print(f'Roman Numeral {string} is {arabic} in Arabic Numeration.')
