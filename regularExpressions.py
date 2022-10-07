import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Meta Characters
. ^ $ * + ? { } [ ] \ | ( )

ha haha

gmail.com
1234567890
. - Matches any character except new line
\d - digit 0-9
\D - not a digit 0-9
\w - word character 0-9 a-z A-Z
\W - not a word character 0-9 a-z A-Z
\s - white space (space, tab, newline)
\S - not a white space (space, tab, newline)
\b - word boundary
\B - Not a word boundary
^ - Start of the string
$ - End of the string
[] - Matches  characters in a string
[^ ] - Macthes charatcers not in string
| either or
() - Group


* - 0 or more
+ 1 or more
? 0 or more
{3} - Exact Number
{3,4} - Range of Numbers (min, max)

    
444-234-2345
444.234.2345
444#234#2345
444-234-2345
123.2345.45432

0427-8923456
0442-23456334

Mr. Myil
Mr S
Mrs KU
Mr. M


cat
bat
hat
sat

pattern.findAll - returns all the matches
pattern = re.compile(r'start', re.IGNORECASE)
'''

print('\tMyilvaganan')  # Prints with tab space - 	Myilvaganan
print(r'\tMyilvaganan')  # Prints without tab space - \tMyilvaganan

pattern = re.compile(r'xyz')
pattern = re.compile(r'\.')  # Need to escape it as it is reserved character in regex
pattern = re.compile(r'gmail\.com')
pattern = re.compile(r'\d')
pattern = re.compile(r'\s')
pattern = re.compile(r'\w')
pattern = re.compile(r'\Bha')
pattern = re.compile(r'\d\d\d')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # match='444-234-2345
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')  # match='444-234-2345
pattern = re.compile(r'[04]\d\d[-]\d{7}\d')  # match='444-234-2345
pattern = re.compile(r'[^b]at') # Not starts with b
pattern = re.compile(r'Mr\.?\s[A-Z]?\w+')
pattern = re.compile(r'(Mr|Mrs)\.?\s[A-Z]?\w+')

urls = '''
1234@gmail.com
'''

matches = pattern.finditer(
    text_to_search)  # Returns the first occurrences of the match with the index to confirm print(text_to_search[24:27])

for match in matches:
    print(match)
    # match.group(1) returns the first group
    # patter.sub(r'\2\3',urls) - Returns the group 2 and group 3 of the urls variable
