# chat history
def read_file(filename):
	lines = []	# in list, each line becomes a string
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())	# string附屬的strip功能來把換行符號去掉 再裝進list
	return lines	# 回傳出lines清單


def convert(lines):
	new = []
	#person = '123'	# declare person outside the for loop
	person = None	# 絕佳的預設值 虛無 但我們有先宣告 (Null in other language)
	for line in lines:	# call things in list iteratively
		if line == 'Allen':
			person = 'Allen'  # use a variable to save who is speaking now
			continue	# 直接跳到下一個迴圈
		elif line == 'Tom':
			person = 'Tom'
			continue	# 確定人名後 就可以跳到下一個迴圈去填入聊天內容
		# 如果person不是手動設定的預設值
		#if person != '123':
		if person:	# if person 有值(不是None) 才運行append
			new.append(person + ': ' + line)  # person: 聊天內容 整句話變成一個字串
		#print(line)	# print exactly the same input content
	#print(new)  # 確定output format沒有錯
	#如果input檔第一行不是人名 就沒有person 程式不知道person是什麼(還沒有背declare的variable) 會當掉
	return new


def write_file(filename, lines):	# filename and what we want to write in
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')	# 設計成parameter
	lines = convert(lines)	# converts lines to output format, 有點覆蓋的感覺
	write_file('output.txt', lines)


main()
