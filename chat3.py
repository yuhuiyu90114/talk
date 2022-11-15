def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def split_string(lines):
	for line in lines:
		s = line.split(' ')
		time = s[0][:5]
		name = s[0][5:]
		print(name)


def main():
	lines = read_file('3.txt')
	split_string(lines)


main()