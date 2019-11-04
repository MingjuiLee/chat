
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:	# need to be in same folder
	for line in f:	# 檔案f裡面的每一line加入lines list
		lines.append(line.strip())	# .strip()才不會空一行

for line in lines:
	s = line.split(' ')
	# list split; can view string as list
	time = s[0][:5]	# start - 4 is Time
	name = s[0][5:]	# 5 - end is name
	#print(time)
	print(name)
	