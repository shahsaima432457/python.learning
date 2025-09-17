try:
    file = open("test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program finished.") 
#how to explain this program is we use try  except method for this program in this program we have used a finally  keyword it will run the
# programm whether the above program is true or false
# # ok
# try:
#   file =open("test.txt","r")
#   print(file.read)
# except FileNotFoundError:
#   print("File not found")

# Finally:
#     Print("program finished")
