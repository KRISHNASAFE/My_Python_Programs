# *************************************Normal List in Python :******************************************
# List items are ordered, changeable, and allow duplicate values.


# thislist = ["apple", "mango", "banana", "orange", "pineapple", "kiwi", "watermelon"]
# print(thislist[2:6])
# print(thislist[-5:-2])
# List Constructor :
# thislist = (("bhendi", "raita", "tomato"))
# print(thislist)

# if "apple" in thislist:
#    print("Yes, Item exist in list.")
"""
thislist = ["apple", "mango", "banana", "orange", "pineapple", "kiwi", "watermelon"]
thislist[:2]=["APPLE", "MANGO", "CHERRY"]
thislist[-4:]=["BANANA", "KIWI", "WATERMELON", "ORANGE", "POMEGRANATE"]
print(thislist)
thislist.insert(9, "CHIKOO")
print(thislist)
thislist.append("GRAPES")
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop()
print(thislist)
del(thislist[0])
print(thislist)
del thislist
"""
"""
thislist=["APPLE", "MANGO", "CHERRY", "BANANA", "KIWI", "WATERMELON", "ORANGE", "POMEGRANATE", "GRAPES", "STRAWBERRY", "PAPAYA"]

Loops in list :

for i in range(len(thislist)):
    print(thislist)
i=0
while i < len(thislist):
   print(thislist[i])
   i = i +1

thislist.reverse()
thislist.sort()
print(thislist)
"""

"""
LISTS JOIN, APPEND, EXTEND :

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

mylist = list1 + list2
print(mylist)

for x in list2:
    list1.append(x)

print(list1)

list1.extend(list2)
print(list1)
"""
