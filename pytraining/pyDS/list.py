#built in function or constructor
empty_list = list()     #this is an empty list ,no item in the list
print(len(empty_list))    #0

#using square brackets
empty_list =[]     #this is an empty list ,no item in the list
print(len(empty_list))  #0

fruits =['banana','orange','mango','apple']
vegetables =['Tomato','potato','cabbage','onion']
animal_products=['milk','meat','butter','yogurt']
web_tech=['HTML','CSS','JS','REACT','NODE','MONGODB']

'''print(fruits)
print(len(fruits))
print(vegetables)
print(len(vegetables))
print(animal_products)
print(len(animal_products))
print(web_tech)
print(len(web_tech))'''


'''fruits=['banana', 'orange', 'mango', 'lemon']                     # list of fruits
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)'''

# list of fruits
fruits=['banana', 'orange', 'mango', 'lemon']
print(fruits)
#adding the item
fruits.append('apple') #adding to the last value in the List
print(fruits)  #printing the current list values
fruits.append('lemon') #adding to the last value in the List
print(fruits)
print(len(fruits)) #finding the length of the list(fruits)
print(fruits[len(fruits)-1])#print the last value
print(fruits[-1]) #print the last value
fruits.insert(2, 'xyz') #insert method used to insert particular place
print(fruits)
fruits.remove('xyz') #remove the item in the list
print(fruits) #it shows the list values
fruits.pop() # it remove the last item in the list
print(fruits)
fruits.pop(2) #pop pass the index place to remove
print(fruits)
del fruits[0]  #delete the particular index value
print(fruits)
fruitscopy=fruits.copy()  #copying the list to another name called fruitscopy
print(fruitscopy)    #both fruits and fruitscopy has the same value
fruits.clear() # clearning the all the elements in the list
print(fruits)
del fruits  # deletes the entire list
print(fruits)
fruitscopy=fruits.copy() #copying the list to another name called fruitscopy
print(fruitscopy)  #both fruits and fruitscopy has the same value
fruits.clear() # clearning the all the elements in the list
print(fruits)
fruitscopy.append('orange')
print(fruitscopy)
print("Count value:",fruitscopy.count('orange'))
fruits1=['a','b','c']
joinfruit=fruitscopy + fruits1 #concatenate two differnt list
print("Join two list:",joinfruit)
fruits2=['d','e','f']
print("fruits2:",fruits2)
fruits2.extend(fruits1) #fruits2=fruits2+fruits1 a+=1 a=a+1
print("Fruits2 extend:",fruits2)
print(fruits2.index('f'))
fruits2.reverse()
print(fruits2)
fruits2.sort()
print(fruits2)
fruits2.sort(reverse=True)
print(fruits2)
numlist=[100,269,32,269,1000,21]
print("Maximum value:",max(numlist)) #aggregate function max,min,count,sum,avg
print("Minimum value:",min(numlist))
print("Sum value:",sum(numlist))
print("Length value:",len(numlist))
print("Average value:",sum(numlist)/len(numlist))
print("Numlis value using iterator:")
for i in numlist:   #Iterator using the for loop.
    print(i,end=' ')
print('\n')
print("Current fruit list",fruitscopy)
myfruits=', '.join(fruitscopy) #join method is used go generate the normal values
print(myfruits)  #join method is the string datatype method
del fruits  # delete the entire list
print(fruits)