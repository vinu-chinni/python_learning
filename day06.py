#SET METHODS
#create a empty dict and print its type
d={}
print(type(d))


#create a empty set and print its type
s=set()
print(type(s))


#add 5 non-sequences and 5 sequences to that set with add method
s.add(123)
s.add(2.11)
s.add(3+4j)
s.add(None)
s.add(True)
print(s)

s.add('vinutna')
s.add(range(1,4))
s.add((1,2,3))
# s.add({1,2,3})
# s.add({1:2,5:4})
#s.add([4,5,6]) # error because it is list ,it means it is mutable


#add 5 non-sequences and 5 sequences with update method
#s.update(123)
#s.update(2.11)
#s.update(3+4j)
#s.update(None)
#s.update(True)
#print(s)                   # error because update allows only sequence data types

s.update('vinutna')
s.update(range(1,4))
s.update((1,2,3))
s.update([5,6,7])
s.update({1,2,3})
s.update({1:2,5:4})

#print a set and remove first element from that set
s={3,4,2,5,6,1}
print(s)
s.remove(1)
print(s)

#remove one existing and one non-existing element from that set
s.remove(2)
print(s)
#s.remove(11) #error because it is no element present in the set


#discard one existing and one non-existing element from that set
s.discard(6)
s.discard(7)
print(s)


#remove all elements from the set
s.clear()
print(s)

#create a set {1,2,3,4}, a list [3,4,5,6].
s={1,2,3,4}
l=[3,4,5,6]
print(s)
print(l)
#write union of set and list
print(s.union(l))         #{1,2,3,4,5,6}
#write intersection of set and list
print(s.intersection(l))  #{3,4}
#write difference of set and list
print(s.difference(l))   #{1,2}
#write symmetric difference of set and list
print(s.symmetric_difference(l))
#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

l=[3,4,5,6]
# print(s1 | l)     
# print(s1 & l)    
# print(s1 - l)     
# print(s1 ^ l)     # error because when we use operators there should be both sets

#DICT METHODS
#create a empty dict
d={}
print(d)

#extend dict with another dict

d.update({1: 'a', 2: 'b'})
print(d)


#extend dict with another list

d.update([[4,'c'],[5,'d'],[6,'e']])
print(d)

#extend dict with another tuple
d = {1: 'a', 2: 'b'}
d.update(((3, 'f'), (4, 'g')))
print(d)

#extend dict with another set--- set does not have key values

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d={1:'a', 2:'b', 3:'c', 4:'d'}
print(d)

#remove the pair with key 4

print(d.pop(4))

#remove the pair with key 100
#print(d.pop(100))       # error because there is no 100 element


#remove the pair with key 100 if not there return 'z'
print(d.pop(100,'z'))

#remove the last pair
#print(d.popitem())

#remove all elements from the dict
d.clear()
print(d)


#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d={1:'a', 2:'b', 3:'c', 4:'d'}
print(d)
#get the value of key 4
print(d.get(4))
#get the value of key 100
print(d.get(100))
#get the value of key 100, if key is not present get 'z'
print(d.get(100,'z'))

#get the value of key 4 with setdefault
print(d.setdefault(4))
print(d)
#get the value of key 100 with setdefault
print(d.setdefault(100))
print(d)
#get the value of key 100 with setdefault, if key is not there add 100 with 'z'
print(d.setdefault(100,'z'))
print(d)
#get all keys of dict and print its type
print(d.keys())
print(type(d))
#get all values in dict and print its type
print(d.values())
print(type(d))
#get all items in dict and print its type
print(d.items())
print(type(d))


