# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Alex"
print( "Hello", name)	# with a comma
print( "Hello "+name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 24
print( "Hello", name)	# with a comma
print("Hello "+str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "rice"
fave_food2 = "steak"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

string = "hello i am alex"
print(string.upper())

string = "litTle avoCado teqUiLA"
print(string.lower())

# define string
string = "Coding is awesome, and it is the best?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)

