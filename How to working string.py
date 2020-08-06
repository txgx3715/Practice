print("Hello\nWorld")


print("Hello\"World\"")

phrase = "Hello World"
#"plus some words after u phrase like:

print(phrase + " I'm here.")
print("")

#Some funtion like: if u use \".lower\" \nthat's will let you words to be lower 

print(phrase.lower())
print("")

#You can also use \".upper\" like this

print(phrase.upper())
print("")

#If you want to judge some value is right or not,\nyou can use some basic logic to do.
#like this codes:(python will be judge this words is Ture or False.）
print(phrase.isupper())
print("or")
print(phrase.islower())
#But in pyhon the code is in order,\nthis can help you to understand.
print(phrase.upper().isupper())

print("")
print("If you want to figure the len of pharse,\nLike this:")
print(len(phrase))

print("")
print("In python,the code by this sequence to arrange:\n0,1,2,3,4,5,,....")
print("You must notice we start at Zero")
print("\"H\" at position \'0\' , \"e\" at position \'1\' etc.")
print(phrase[0])
print(phrase[4])

print("")
print("index funtion:")
print("By this funtion \nwe can index this phrase to find specific letter position or \nwhere start at this words positon")
print(phrase.index("H"))
print(phrase.index("World"))

print("")
print("replace funtion:")
print("By this funtion,we can replace some specific letter or words")
print(phrase.replace("Hello","Human"))

print(phrase.replace("Hello","New"))

