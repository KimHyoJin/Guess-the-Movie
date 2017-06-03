# download the videos froom Youtube using Youtube.dl
import os

f = open('url.txt')
name = 0

while True:
	line = f.readline()
	if line == '':
		break
	cmd = "youtube-dl -o " + str(name) + ".mp4" + " " +line
	os.system(cmd)
	name = name + 1;

