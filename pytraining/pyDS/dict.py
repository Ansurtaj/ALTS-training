Dictionary_Name={} #symbol method
print(Dictionary_Name)
print(type(Dictionary_Name))
Dictionary_Name=dict()#dict constructor method
print(Dictionary_Name)
print(type(Dictionary_Name))
phone_book={
                'ramu':'1234568790',
                'santhosh':'9325698789',
                'ajay':'6326598752'
           }
print ("phone number:",phone_book['ramu'])
print ("phone number:",phone_book['santhosh'])
phone_book=dict(
                ramu='1234568790',
                santhosh='9325698789',
                ajay='6326598752'
           )
print ("phone number:",phone_book['ramu'])
print ("phone number:",phone_book['santhosh'])
words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"
print(words)
for key in words:  
         print(key," is :",words[key])
print("Keys are:",phone_book.keys())
print("Keys are:",words.keys())
print("Values are:",phone_book.values())
print("Values are:",words.values())
print( "tuples are:",phone_book.items())
print ("value:",phone_book.get('ramu'))
print ("value:",phone_book.pop('ramu'))
print(phone_book)
copy_phone_book=phone_book.copy()
print(copy_phone_book)
for key, value in phone_book.items():
    print(f"{key}: {value}")