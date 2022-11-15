def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def count_file(lines):
	count_image_Allen = 0
	count_sticker_Allen = 0
	count_word_Allen = 0
	count_image_Viki = 0
	count_sticker_Viki = 0
	count_word_Viki = 0
	
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				count_image_Allen += 1
			elif s[2] == '貼圖':
				count_sticker_Allen += 1
			else:
				for i in s[2:]:
					count_word_Allen += len(i)
		elif name == 'Viki':
			if s[2] == '圖片':
				count_image_Viki += 1
			elif s[2] == '貼圖':
				count_sticker_Viki += 1
			else:
				for i in s[2:]:
					count_word_Viki += len(i)
	print('Allen說了{}個字,{}貼圖,{}圖片'.format(count_word_Allen, count_sticker_Allen, count_image_Allen))
	print('Viki說了{}個字,{}貼圖,{}圖片'.format(count_word_Viki, count_sticker_Viki, count_image_Viki))

lines = read_file('LINE-Viki.txt')
count_file(lines)

