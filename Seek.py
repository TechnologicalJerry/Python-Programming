fi = open("text.txt", "r+")
print("Name of the file: ", fi.name)

line_1 = fi.readline()
print("Read Line: %s" % (line_1))

fi.seek(0, 1)
line_2 = fi.readline()
print("Read Line: %s" % (line_2))

fi.close()
