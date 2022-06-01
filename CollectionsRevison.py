#Python Types
#Built in Sequence Types: - Strings/Lists/Tuples are Ordered collections
str = 'norwegian blue' 'Mr.Khan\'s bike'
#above shows two string values assinged to the variable 'str'

list = ['cheedar',['Camembert','Brie'],'Stilton']
#

Tuple = (47,'spam','major',638,'Ovine Aviation')
#the commers make a list a tuple

#set is an unordered collection of unique objects - no duplicates/ selective capabilities
#Dictionaries a special form of set
Dictionary = {'Tones':'Barber', 'BritishColumbia': 'LumberJack'}
#Dictionaries are collections of objects with values at the key

#Generic Built in functions itrerable - we can interate over
#len() - Number of Elements/ Characters     min() - Minimum Value
#max() - Maximum Value                    sum() - Numeric summation(not string or byte objects)- This will raise a Type
#error if not a number
myn = [32, 66,12,3,99,3.142, 42]
print("min:",min(myn), "max:",max(myn))
print("sum:", sum(myn))

myd= {'fred':3,'jim':8,'dave':42}
print("min:",min(myd), "max:",max(myd))
#here we can see the different built in functions in action^^

#useful tuple operations
a = 7
b = 3
print(a,b)

a, b = b, a
print(a,b)

x , y, z, = 10, 20, 30
print(x, y, z)
#asign in one line

x, y, z = range(3)
print(x, y, z)

#OPERATOR OVERLOADING
print('hello '* 5)
first_three = 'imaan','amber','CJ'
print(type(first_three))
print(first_three * 5)

#two ways to create lists
#with a list (object) or []
cheese = ['cheddar', 'stilton','cornish rag']
print(cheese[-1])
cheese[-1] = 'red leicster'
print(cheese)

#Slicing


#ended
x, y, z = first_three
print(x)
mytuple = ('eggs','bacon','spam',)

t1 = 'cat'
#set operators, ven diagrams
#.append (add to the end) .insert() add first the index place and then the new value
#.extend(add new list) adding two lists together

#.remove() pass the value through the function
#.pop() witll remove last value by default
# .pop also runs the returned value popped = .pop
#.reverse - will reverse the list
#.sort will sort in alphabetical order
#.sort() pass through reverse=True
#Dictionairies
#{:} or dict()
# removing items from dict
#del dict[]
#| pipe symble