# chat history convertion: Line
# read_file no need to change
def read_file(filename):
	lines = []	# in list, each line becomes a string
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())	# string附屬的strip功能來把換行符號去掉 再裝進list
	return lines	# 回傳出lines清單


def convert(lines):
	person = None	# 絕佳的預設值 虛無 但我們有先宣告 (Null in other language)
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')	# 一整行字串切完會變成一個list
		time = s[0]
		name = s[1]
		if name == 'Allen':
			#print(s[2:])  # m = msg = message
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:	# not sticker, so count how many words
				for m in s[2:]:  # no matter how many chunks after splitting, we need total count
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:	# not sticker, so count how many words
				for m in s[2:]:  # no matter how many chunks after splitting, we need total count
					viki_word_count += len(m)
	print('Allen said %d words, sent %d stickers, and sent %d images' %(allen_word_count, allen_sticker_count, allen_image_count))
	print('Viki said %d words, sent %d stickers, and sent %d images' %(viki_word_count, viki_sticker_count, viki_image_count))


def write_file(filename, lines):	# filename and what we want to write in
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('-LINE-Viki.txt')	# 設計成parameter
	lines = convert(lines)	# converts lines to output format, 有點覆蓋的感覺
	#write_file('output.txt', lines)	# 先不要寫入檔案


main()
