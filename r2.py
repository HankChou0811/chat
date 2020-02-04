

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count =0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else: 
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen said', allen_word_count, 'and stickers', allen_sticker_count)
	print(allen_image_count, 'pic')
	print('viki said', viki_word_count, 'and stickers',viki_sticker_count)
	print(viki_image_count, 'pic')
	return new
#前三個 n[:3] (也就是n的零到三) 這樣會給出前三個清單中的東西 (開始值包含 結束值不包含)
#中間 n[2:4] 這樣是第二個跟第三個會被拿出來~
#結尾 n[-2:] 這樣就是倒數第二個開始到最後都拿出來


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('-LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()