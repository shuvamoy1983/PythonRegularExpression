import re

#Identifiers:

#\d = any number
#\D = anything but a number
#\s = space
#\S = anything but a space
#\w = any letter
#\W = anything but a letter
#. = any character, except for a new line
#\b = space around whole words
#\. = period. must use backslash, because . normally means any character.

exampleString = '''
Jessica is 150 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
Ip is 10.20.33.0
'''

### Search a word followed by a another word.
## we will use match or search or findall function for this
## This match() function matches the pattern in the beginning of a given string.
## The function search() finds the first occurrence of pattern in string. If pattern is found it returns pattern, None otherwise.
## If you want to find all occurrence of pattern RE in string, use findall() function.

line = "There is no theory of evolution. Only a list of animals Chuck Norris allows to live"
line1 = "The big bag of bits was bugged"

exp_followed_by_word = r'th'
exp_followed_by_word_g = r'b.g'

matchObj = re.match(exp_followed_by_word, line, re.M|re.I)
matchObj1 = re.match(exp_followed_by_word_g, line1)


#v = re.match(r'15',exampleString)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

if matchObj1:
   print ("match --> matchObj1.group() : ", matchObj1.groups())
else:
   print ("No match!!")

matchObj = re.search(exp_followed_by_word_g, line1)

if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

matchObj = re.findall(exp_followed_by_word_g, line1)
print("With FIndall:" , matchObj)

