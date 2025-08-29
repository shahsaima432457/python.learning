str ="i am  studing python from ApnaCollege "

#it shows us the true or false value
print(str.endswith("apnaCollege"))
print(str.endswith("ApnaCollege "))

print(str.startswith("I"))

#capitalize  convert small to captial but it can convert only first alpha in the word

print(str.capitalize())
print(str)

#replace
name = " i am  today very buzy i cant  watch all lectures"

print(name)
print(name.replace("a","m"))

#find

name = " i am  today very buzy today very buzy i cant  watch all lectures"
print(str.find("am"))

#count
print(name.count("very"))