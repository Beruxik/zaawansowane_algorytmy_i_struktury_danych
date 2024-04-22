def anagram(string1, string2):
    return sorted(string1.lower().replace(' ', '')) == sorted(string2.lower().replace(' ', ''))

string1 = input('Input first string: ')
string2 = input('Input second string: ')

print('This words are anagram.' if anagram(string1, string2) else 'This words aren\'t anagram')