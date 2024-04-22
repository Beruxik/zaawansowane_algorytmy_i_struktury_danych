def anagram(string1, string2):
    string1_count = {}
    string2_count = {}

    for letter in string1.replace(' ', '').lower():
        if letter in string1_count:
            string1_count[letter] += 1
        else:
            string1_count[letter] = 1
    
    for letter in string2.replace(' ', '').lower():
        if letter in string2_count:
            string2_count[letter] += 1
        else:
            string2_count[letter] = 1
    
    return sorted(string1_count) == sorted(string2_count)

string1 = input('Input first string: ')
string2 = input('Input second string: ')

print('This words are anagram.' if anagram(string1, string2) else 'This words aren\'t anagram')