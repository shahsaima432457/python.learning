
# collection ={ 1,2,3,4,5}

# print(collection)
# print(type(collection))
# # set can not print  dublicate  values

# print(len(collection))
#it can use only unique values
#syntex of set is given below:

collection = set()

print(type(collection))

collection.add(1)
collection.add(2)
collection.add(3)

print(collection)


#removes the element
# print the lenght of collection
print(collection)

print(len(collection))

#clear the set

collection.clear()

print(collection)
print(len(collection))


#pop method is used to remove the rendom values


collection = {"hello", "apnacollege", "world",}
print(collection.pop())
print(collection.pop())




# union
#combines both set values and returns new

set1 ={1,2,3}
set2 ={3,4,5}


print(set1.union(set2))


#intersection

#combines common values and returns new

set1 ={1,2,3}
set2 ={3,4,5}

print(set1.intersection(set2))





