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

#*************************************


# Write a program that reads in integer numbers from a text file named indata.txt in the same directory as the executing program.  
# Print the sum of the numbers with comma separators and two digits.

# For example if the file has the following data:

# 10
# 1000
# 20

# Your program should print 1030.00.

# path= "indata.txt"
# aFile = open(path, "rt")
# sum = 0
# for line in aFile:
#     sum += int(line)

# print(f"{sum:,.2f}")


#*************************************


# INHERITANCE IN PYTHON CLASSES

# OVERLOADING OCCURS WHEN TWO OR MORE METHODS IN ONE CLASS HAVE THE SAME NAME BUT DIFFERENT PARAMETERS.

# OVERRIDING OCCURS WHEN A METHOD IN A PARENT CLASS IS OVERRIDDEN BY A METHOD IN A CHILD CLASS.
# TO CALL THE OVERRIDDEN METHOD (THE PARENTS CLASS METHOD) YOU MUST USE THE SUPER() METHOD.
# OR YOU CAN USE THE PARENTS CLASS NAME TO CALL THE METHOD.

# class Animal:
#     def Walk(self, inDistance):
#         print("I am walking" + inDistance)


# class Cow(Animal):
#     spots = 3
#     # WALK METHOD BEING OVERRIDDEN BUT CALLING THE PARENT CLASS METHOD
#     def Walk(self, inDistance):
#         Animal.Walk(inDistance)
    
#*************************************

# EXCEPTIONS
# EXCEPTIONS ARE ERRORS THAT OCCUR WHEN A PROGRAM TRIES TO RUN.
# TRY EXCEPT IS WHAT IT IS CALLED TO HANDLE IT IN PYTHON
# TRY BLOCK TRIES TO RUN THE CODE IN THE TRY BLOCK. IF AN ERROR OCCURS IT WILL GO TO THE EXCEPT BLOCK.

# try:
#     #STUFF TO TRY
# except:
#     #STUFF TO DO IF AN ERROR OCCURS
# finally:
#     #STUFF TO DO ALWAYS

# CAN CREATE CUSTOM EXCEPTIONS TO HANDLE DIFFERENT ERRORS.
# IF USING A SPECIFIC EXCEPTION YOU MUST CHECK FOR THE SPECIFIC EXCEPTION BEFORE A GENERAL EXCEPTION
# EXCEPTIONS ARE NOT EXPECTED
# class CowException(Exception):
#     # pass IS USED HERE AS AN EXAMPLE.  IT BASICALLY MEANS DO NOTHING.
#     pass

# try:
#     myCow = Cow()
#     myCow.Walk("100")
#     myCow.Milk()
# except CowException:
#     print("There was a cow exception")
# except:
#     print("There was a general exception")

#*************************************


# MORE INHERITANCE
    
# class CowException(Exception):
#     # pass IS USED HERE AS AN EXAMPLE.  IT BASICALLY MEANS DO NOTHING.
#     pass

# class Animal:
#     def Walk(self, inDistance):
#         print("I am walking" + inDistance)


# class Cow(Animal):
#     spots = 3
#     # WALK METHOD BEING OVERRIDDEN BUT CALLING THE PARENT CLASS METHOD
#     def Walk(self, inDistance):
#         raise CowException("Moo this is a cow exception")
#         Animal.Walk(inDistance)



# aCow = Cow()
# try:
#     aCow.Walk("100")
# except CowException:
#     if isinstance(aCow, Animal):
#         print("This is an animal")

#*************************************

# Write a class that calculates and stores the height and weight of a person in metric.
# BMI is calculated using this formula:
# Weight/Height^2 - weight is in kilograms and height is in meters.
# The class should have two properties named:

#     Weight
#     Height

# The class should have two methods:

#     BMI_Value – This takes no arguments and returns a decimal value of the BMI
#     Equals – This should override the equals method from the object class to compare the weight and height of two BMI objects.
#     To override the equal method you should implement this method: __eq__(self, other) and return a boolean

# class BMI:

#     _weight = 0
#     _height = 0

#     # def __init__(self, inWeight, inHeight):
#     #     self.Weight = inWeight
#     #     self.Height = inHeight

#     def __get_Weight(self):
#         return self._weight
#     def __set_Weight(self, value):
#         self._weight = value

#     def __get_Height(self):
#         return self._height
#     def __set_Height(self, value):
#         self._height = value

#     weight = property(__get_Weight, __set_Weight)
#     height = property(__get_Height, __set_Height)

#     def BMI_Value(self):
#         return self.weight / (self.height ** 2)

#     def __eq__(self, other):
#         return self.weight == other.weight and self.height == other.height
    
# person1 = BMI()
# person2 = BMI()


# print(person1 == person2)