#file io
#files
#python can be used to perform operations on a fire.(read and write data)
# io input output



# RAM random access memory
# it is fast in execution
# but the data can not store
# if we refresh it everything will get finish
# we store the data in the form of files so that
# it could not deleter















# types of all files
# text files:txt,docx, log etc
# the data is stored in the form of characters



# binary files: mp4,mov, png, png etc




#open, read, and close file
# we have to open a file before reading or writing
# by default python accumes the read operation


# f = open("file_name","mode")

#sample.txt                  r= read mode
#demo.docx                   w= write mode
#data = f.read()

#f.close()


f = open("E:\Python\lecture7.py\demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()


#E:\Python\lecture7.py\demo.txt
#E:\Python\lecture7.py\file.py
# read entire file    data = f.read()
# reads one line at a time   data = f.readline()

# the example is given below

f = open("E:\Python\lecture7.py\demo.txt","r")
data = f.readline()
print(data)
print(type(data))


data = f.readline()
print(data)

data = f.readline()
print(data)






f.close()






















































