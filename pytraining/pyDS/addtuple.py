tup1=() # using paranthasis create tuple
print(len(tup1))
print(type(tup1))
tup1=tuple() #using constructor method
print(len(tup1))
print(type(tup1))
tup1 = ("Rohan", "Physics", 21, 69.75) #heterogenious data type
tup2 = (1, 2, 3, 4, 5)  #numeric datatype
tup3 = ("a", "b", "c", "d") #string data type
tup4 = (25.50, True, -55, 1+2j) ##heterogenious data type
print(type(tup1))
print(type(tup2))
print(type(tup3))
print(type(tup4))
print(tup1[0])  #first value in the tup1 using forward index
print(tup1[len(tup1)-1]) #print the last value in the tup1
print(tup1[-1]) #BACKWARD INDEX
print(tup1[0:])# print all the values in tup1
print(tup1[0:2])# print index of 0 ,1 in tup1
#tup1[0]="senthil" #update the value is not possible in tuple. immutable object
tup1=(1,2,3)
print(tup1*1)#no replication
print(tup1*2)#one time replication
print(tup1*3)#two time replication
print(tup1*4)#three time replication

tuple1=(1,2,3)
tuple2=(4,5,6)
tupleadd=tuple1+tuple2#concatenation of two tuples
print(tupleadd)

#del tuple1
#del tuple1[0]
print(tuple1)
#using membership operator in or not in
for x in (1,2,3):
    print(x)

for x in tuple1:
    print(x)

print("Maximum value:" ,max(tuple1))
print("Minimum value:",min(tuple1))
print("Sum value:",sum(tuple1))
print("Length value:",len(tuple1))
print("Average value:",sum(tuple1)/len(tuple1))
tuple1=(3,2,5,61,3,4,5)
tuple1=sorted(tuple1) 
print(tuple1)
tuple1.remove(5)
print(tuple1)
tuple1.append(10)
print(tuple1)
print(tuple1.index(10))
tuple1.pop()
print(tuple1)