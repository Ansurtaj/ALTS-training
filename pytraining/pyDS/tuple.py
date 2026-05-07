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
tupl=(1,2,3)
print (tupl*1)#no replication
print (tupl*2)#one time replication
print (tupl*3)#two time replication

print (tupl*4)#three time replication