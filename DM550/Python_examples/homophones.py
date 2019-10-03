words = open("cmudict-0.7b.txt")
simwords = dict()
fivewords = []
for line in words:
	word = line.strip()
	i = 0
	key = ""
	while i < len(word) and word[i] != " ":
		key += word[i]
		i += 1
	if len(key) == 5:
		fivewords.append(key)
		simwords[key] = word[i+1:]
	if len(key) == 4:
		simwords[key] = word[i+1:]
for w in fivewords:
	if w[1:] in simwords and (w[0] + w[2:]) in simwords:
		if simwords[w] == simwords[w[1:]] and simwords[w] == simwords[w[0] + w[2:]]:
			print(w, " ", w[1:], " ", w[0] + w[2:], " ", simwords[w])