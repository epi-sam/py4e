fhand = open("/ihme/code/ssbyrne/py4e/ch8_mbox.txt", mode = "r")
count = 0

for line in fhand:
	count = count + 1
print("line count:", count)
