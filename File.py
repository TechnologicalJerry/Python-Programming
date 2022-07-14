fileptr = open("file2.txt", "r")

print("The filepointer is at byte :", fileptr.tell())

fileptr.seek(10)

print("After reading, the filepointer is at:", fileptr.tell())
