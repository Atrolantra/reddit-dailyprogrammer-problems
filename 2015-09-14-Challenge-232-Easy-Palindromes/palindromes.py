# https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/
x = int(input("How many lines in the palindrome: "))
passage = ""
for _ in range(x):
    passage += ''.join(l for l in str(raw_input("Insert line number " + str(_ + 1) + ": ")) if l.isalnum())
if passage.lower() == passage[::-1].lower():
    print "Palindrome"
else:
    print "Not a palindrome"
