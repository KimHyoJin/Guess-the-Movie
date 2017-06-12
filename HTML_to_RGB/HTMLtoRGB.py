
fw = open("train_RGB_dataset.txt", "w")

f = open("train_HTML_dataset.txt")
for line in f:
	index = 1
	#data = f.readline()
	data_split = line.split()
	num = int(data_split[0])
	write_data2 = "%d" % num
	fw.write(write_data2)

	for i in range(1, 6):
		feature = data_split[i].split(':')
		html = feature[1]
		r = int(html[0:2], 16)
		g = int(html[2:4], 16)
		b = int(html[4:6], 16)

		write_data = " %d:%d %d:%d %d:%d" % (index, r, index+1, g, index+2, b)
		fw.write(write_data)
		index = index+3

	fw.write("\n")




