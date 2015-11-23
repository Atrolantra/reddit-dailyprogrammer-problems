# Quick script to format the challenge titles to make the folders to keep them in
# Eg before: [2015-11-09] Challenge #240 [Easy] Typoglycemia
# Eg after:  2015-11-09-Challenge-240-Easy-Typoglycemia
string = raw_input()
string = string.replace('[', '')
string = string.replace(']', '')
string = string.replace('#', '')
string = string.replace(' ', '-')
print string