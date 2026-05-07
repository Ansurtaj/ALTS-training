thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))
thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grapes"])
print(thisset)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) #set1=set1+set2
print(set1)
l = [10,20,30,40,50]
s = set(l)
print(s)
s = set(range(2,10))
print(s)
s = {}
print(s)
print(type(s))
s = set()
print(s)
print(type(s))
s = {10,20,30}
s1 = s.copy()
print(s1)