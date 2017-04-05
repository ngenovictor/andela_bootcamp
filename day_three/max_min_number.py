def find_max_min(list_value):
	result = []
	max_value = max(list_value)
	min_value = min(list_value)
	if max_value==min_value:
		result.append(min_value)
	else:
		result.append(min_value)
		result.append(max_value)
	return result