# FILE OPEN MODES:
# r - read - DEFAULT VALUE. OPENS A FILE FOR READING.  ERROR IF THE FILE DOES NOT EXIST.
# w - write - OPENS A FILE FOR WRITING.  OVERWRITES AN EXISTING FILE. CREATES A NEW FILE IF THE FILE DOES NOT EXIST.
# a - append - OPENS A FILE FOR APPENDING TO THE END. CREATES A NEW FILE IF THE FILE DOES NOT EXIST.
# x - create - CREATES A FILE. ERROR IF THE FILE EXISTS.
# + - read and write

# CAN APPEND THE TYPE OF FILE IN THE MODE STRING 
# "t" - TEXT MODE - DEFAULT VALUE.
# "b" - BINARY MODE. (COULD BE IMAGES ETC)

# a = open("test.txt")
# b = open("test.txt", "r")
# c = open("test.txt", "rt")
# d = open("c:\\temp\\test.txt", "rt") #IF USING WINDOWS YOU MUST ESCAPE THE \ WITH \\
# e = open("/temp/test.txt", "rt")
# f = open("test.txt", "wt")

#*************************************

# TEXT DATA FILE STUFF
# READLINE READS THE NEXT LINE UNTIL THE END OF THE LINE OR THE END OF THE FILE
# path = "temp/test.txt"
# f = open(path, "rt")
# print(f.readline())
# f.close()

# LOOPING THROUGH LINES OF TEXT IN A FILE
# path = "temp/test.txt"
# f = open(path, "rt")
# for line in f:
#     print(line)
# f.close()

# WRITING A LINE OF TEXT TO A FILE (OVERWRITING THE FILE.)
# path = "temp/test.txt"
# f = open(path, "wt")
# line = "Hello this is a line of text"
# f.write(line)
# f.close()

#*************************************

# BINARY FILE STUFF
# WRITING A BINARY OBJECT TO A FILE (OVERWRITING THE FILE.)
# path = "temp/test.bin"
# f = open(path, "wb")
# value = 10
# f.write(value)
# f.close()

#READ A BINARY OBJECT FROM A FILE
# path = "temp/test.bin"
# f = open(path, "rb")
# value = f.read(4) #READS 4 BYTES OF DATA FROM THE FILE.
# f.close()



# Write a program that reads in integer numbers from a text file named indata.txt in the same directory as the executing program.  
# Print the sum of the numbers with comma separators and two digits.

# For example if the file has the following data:

# 10
# 1000
# 20

# Your program should print 1030.00.

path= "indata.txt"
aFile = open(path, "rt")
sum = 0
for line in aFile:
    sum += int(line)

print(f"{sum:,.2f}")

