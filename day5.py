# INSERT OPERATIONS
a = [1, 2, 3]  # create a list with 3 elements
print(a)       #[1,2,3]

# appending
a.append(10)   # add 5 types of non-sequence elements
a.append(2.5)
a.append(True)
a.append(None)
a.append(3+4j)
print(a)        #[1,2,3,10,2.5,True,None,3+4j]


a.append("vinutna")  # add 5 types of sequences to it with append
a.append([4, 5])
a.append((6, 7))
a.append({8, 9})
a.append({1: 1})
print(a)             #["vinutna",[4,5],(6,7),{8,9},{1:1}]

# extending
# add 5 types of non-sequence elements to it with extend
#a.extend(None)
#a.extend(20)
#a.extend(2.41)         #its comes error because in extend method it should be sequence data types 
#a.extend(3+4j)
#a.extend(True)
#print(a)

# add 5 types of sequence elements to it with extend
a.extend("vinutna") # v,i,n,u,t,n,a
a.extend([1, 2])  # 1,2
a.extend((3, 4))  #3,4
a.extend({5, 6})   #5,6
a.extend({1: 7})   #1
print(a)

#inserting
# insert an element at index 1 and print
a.insert(1, 100)   #[1,100,2,3........]   positive index left to right
print(a)             # 0 1  2  2

# insert an element at index -1 and print
a.insert(-1, 200)   #[1,2,3........200]   negative index right to left
print(a)

# insert an element at index 10000 and print
a.insert(10000, 300) #[1,2,3,.....,300]
print(a)

# insert an element at index -10000 and print
a.insert(-10000, 400) #[400,1,2,3.....]
print(a)


# DELETE OPERATIONS

# create a list with 1,2,1,3,4,1
a= [1, 2, 1, 3, 4, 1]

# pop element at index 3 and print element and list
x = a.pop(3)  #3 
print(x)
print(a)      #[1,2,1,4,1]

# remove first 1 from list and print element and list
a.remove(1)   
print(a)   #[2,1,4,1]

# clear all elements in the list
a.clear()
print(a)  #empty []

# UPDATE OPERATIONS

# create a list with 3,2,1,5,4
a = [3, 2, 1, 5, 4]

# sort the list in ascending and print
a.sort()
print(a)  #[1,2,3,4,5]

# sort the list in descending and print
a.sort(reverse=True)  #[5,4,3,2,1]
print(a)

# reverse the list and print
a.reverse()
print(a)   #[1,2,3,4,5]

 #READ OPERATIONS

# create a list with 1,2,1,3,1,2
a = [1, 2, 1, 3, 1, 2]

# find count of 1 and 2 in list
print(a.count(1)) # 3
print(a.count(2)) # 2

# find index of 1 from start
print(a.index(1))  #0

# find index of 1 from 2nd index
print(a.index(1, 2)) #2

# find index of 1 from 5th index
#print(a.index(1, 5))  #error there is no 5 th index


# TUPLE
# create a tuple with 1,2,1,3,1,2
a = (1, 2, 1, 3, 1, 2)

# find count of 1 and 2 in tuple
print(a.count(1)) # 3
print(a.count(2))# 2

# find index of 1 from start
print(a.index(1)) 

# find index of 1 from 2nd index
print(a.index(1, 2))

# find index of 1 from 5th index
#print(a.index(1, 5)) # error





