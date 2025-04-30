import re

regex = r"hello"
pattern = "hello world"
print(re.search(regex, pattern))#returns span of the match, case sensitive

regex2 = r"hello|hi|greetings"
pattern2 = "greetings! how are you?"
print(re.search(regex2,pattern2,re.IGNORECASE))#ignores case

regex3 = r"hello|\bhi\b|greetings"#\b<string>\b is boundary condition and will match only complete words
pattern3 = "hiya! how are you? Greetings"
print(re.search(regex3,pattern3,re.IGNORECASE))#won't find hi in hiya 


print(re.match(regex2,pattern3))#matches only beginning of the string

input_pattern = "Hello, how are You feeling. Greetings, and thanks!"
print(re.findall(regex3, input_pattern, re.IGNORECASE))# Finds all ocurrences and returns a list


if re.search(regex3,input_pattern,re.IGNORECASE):
    print("Present")
else:
    print("Absent")
   
   
    
"""Advanced string matching and pattern recognition
[a-z] --> \w
[0-9] --> \d
"""

regex = r"[a-z]"
regex1 = r"[a-z]+"
regex_digit = r"[0-9]+"
regex_email = r"[a-z]+[0-9]+@[a-z]+\.[a-z]+"
regex_email2 = r"\w+\d*@\w+\.\w+"
input_pattern = "example123@gmail.com"
input_patterns = "cm2015@mail.com, email9@look.com, markopolo@box.com"

print(re.search(regex,input_pattern))# matches 'e'
print(re.search(regex1,input_pattern))# matches 'example'
print(re.findall(regex1,input_pattern))# matches 'example','gmail', 'com'
print(re.findall(regex_digit,input_pattern))# matches '123'
print(re.findall(regex_email,input_pattern))# matches 'example123@gmail.com'
print(re.findall(regex_email2,input_pattern))# matches 'example123@gmail.com'
print(re.findall(regex_email2,input_patterns))

date = "01-01-2025"
regex_date = r"(\d{2})-(\d{2})-(\d{4})" #Parenthesise into groups to be accessed later
match = re.search(regex_date, date)
print(match)
print(match.groups())
#print(match.group())

