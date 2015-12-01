import random
import string

text = """According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are, 
the only important thing is that the first and last letter be in the right place. 
The rest can be a total mess and you can still read it without a problem. 
This is because the human mind does not read every letter by itself, but the word as a whole. 
Such a condition is appropriately called Typoglycemia."""

# text = text.replace("\n", "")
scrambled = []


for word in text.split(' '):
	word = word.replace("\n", "")
	if word[-1] in string.punctuation:
		cut_word = word[1:-2]
		if len(cut_word) <= 2:
			scrambled.append(word)
			continue
		cut = -2


	else:
		if len(word) <= 3:
			scrambled.append(word)
			continue
		cut_word = word[1:-1]
		cut = -1


	listed = list(cut_word)
	random.shuffle(listed)
	scrambled_word = word[0] + ''.join(listed) + word[cut:]


	scrambled.append(scrambled_word)



print ' '.join(scrambled)


