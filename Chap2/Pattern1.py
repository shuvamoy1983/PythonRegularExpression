import re

## Using dot operator

line = "You can live like a king but make sure it isn't a lie"
exp = 'l..e'
print(re.findall(exp,line))

##Ranges of Characters
line ="When today is over Ted will have a tedious time tidying up."
exp = 't[eo]d'
print(re.findall(exp,line))

##Ranges of numbers
line="G4 G9 F2 H1 L0 K7 M9"
exp = '[0-9]'
print(re.findall(exp,line))

##We can also combine multiple sets.
exp ='[1-5a-fx]'
line = "ah34yhis 39 juujrx"
print(re.findall(exp,line))

##Negating - Find characters that aren't
line = "When today is over Ted will have a tedious time tidying up"
exp = r't[^eo]d'
print(re.findall(exp,line))

##Multipliers
## Multipliers allow us to increase the number of times an item may occur in our regular expression.
## Here is the basic set of multipliers:

## * - item occurs zero or more times.
## + - item occurs one or more times.
## ? - item occurs zero or one times.
## {5} - item occurs five times.
## {3,7} - item occurs between 3 and 7 times.
## {2,} - item occurs at least 2 times.

##In the below example we are looking for the character 'l'
# followed by the character 'o' zero or more times.
line ="Are you looking at the lock or the silk?"
exp = r'lo*'
print(re.findall(exp,line))

## This is what's referred to as greedy matching.
exp =r'l.*k'
print(re.findall(exp,line))
##We may reverse this behaviour and make it not
## greedy or lazy by placing a question mark ( ? ) after the multiplier
exp1 =r'l.*?k'
print(re.findall(exp1,line))

##Escaping Metacharacters




