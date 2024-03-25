str1 = "P@#yn26at^&i5ve"
list1 = []
string = 0
numbers = 0
symbols = 0
for x in str1:
    if x.isalpha():
        string = string + 1
    elif x.isnumeric():
        numbers = numbers + 1
    else:
        symbols = symbols + 1

print(f'No of Strings: {string}'
      f'\nNo of Numbers: {numbers}'
      f'\nNo of Symbols: {symbols}')
