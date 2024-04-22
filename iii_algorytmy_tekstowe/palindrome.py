def palindrome(string):
    modified_string = ''.join(letter for letter in string if letter.isalnum()).lower()
    return modified_string == modified_string[::-1]

string = input('Input string: ')
print('This is a palindrome.' if palindrome(string) else 'This is not a palindrome.')