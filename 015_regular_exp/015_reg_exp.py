"""
REGULAR EXPRESSIONS
"""
# ! --- # ! --- # ! --- # ! --- # ! --- # ! --- # ! ---
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
'''
email = '''
SampleMail@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Sample@example.co.uk
example@example.org
'''
urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''
sentence = 'Start a sentence and then bring it to an end'
# ! --- # ! --- # ! --- # ! --- # ! --- # ! --- # ! ---
# pattern = re.compile(r'M(rs|r|s).? [A-Z][a-z]*')
# mtch = pattern.finditer(text_to_search)
# # mtch = pattern.finditer(sentence)
# for match in mtch:
#     print(match)

# pattern = re.compile(r'[A-Za-z0-9-\._+]+@[A-Za-z0-9-]+\.[A-Za-z]+(\.*[A-Za-z]+  )')
# pattern = re.compile(r'(https://|http://)?(www\.)?[A-Za-z0-9]+\.[A-Za-z]+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_url = pattern.sub(r'\2', urls)
mtch = pattern.finditer(urls)
print(subbed_url)
for match in mtch:
    print(match)