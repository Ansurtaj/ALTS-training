fruits=['banana', 'orange', 'mango', 'lemon']                     # list of fruits
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

vegetables=['Tomato','Potato','Cabbage', 'Onion','Carrot']
all_fruits=fruits[0:4]
print(fruits[0:3])
print(vegetables[::2]) #slicing
print(vegetables[1:])
print(fruits[:3])