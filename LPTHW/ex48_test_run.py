string = 'bear kill princess up your mother 9'

nouns = {'noun': ('bear', 'door', 'princess', 'cabinet')}
verbs = {'verb': ('go', 'kill', 'eat', 'stop')}
stops = {'stop': ('the', 'in', 'of', 'from', 'at', 'it')}
directions = {'direction': ('north', 'south', 'east', 'west', 
							'up', 'down', 'left', 'right', 'back')}

words = (nouns, verbs, stops, directions) # create tuple of dict's

wordlist = string.split()
print wordlist
result = []
for word in wordlist:
		try:
			x = False
			i = 0
			while x == False:
				for a, b in words[i].iteritems():
					if word in b:
						result.append((a, word))
						x = True
					else:
						i += 1
		except IndexError:
			try:
				result.append(('number', int(word)))
			except ValueError:
				result.append(('error', word))
				
print result

for z in words:
	for a, b in z.iteritems():
		if word in b:
			result.append((a, word))
			break