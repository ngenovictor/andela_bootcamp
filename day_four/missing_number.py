def find_missing(a,b):
	if not a or not b:
		return 0
	else:
		for t in b:
			if t not in a:
				return t
		else:
			return 0
