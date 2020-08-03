# Now we will create a new thing: Dictionary
New_Dictionary = {
    "A" : "App",
    "B" : "Brilliant",
    "C" : "Color",
    "D" : "Hero",
    "E" : "Elage",
    "F" : "Fox",
    "G" : "God",
    "H" : "Hero",
    "I" : "In",
}


# now you have you frist Dictionary,try to do sth
print(New_Dictionary.get("A"))
# You can also by this way to refer to dictionary
print(New_Dictionary["H"])

# But if you input one words not in dictionary,what will happen?
print(New_Dictionary.get("not"))

# Yes,Like you known,that's \"none\".
#But if you give a value to this "not belong to dictionary words",what will happen?

print(New_Dictionary.get("not","This words not belong to Dictionary."))



num_Dictionary = {
    1 : "App",
    3 : "Brilliant",
    2 : "Color",
    5 : "Hero",
    99 : "Elage",
    565 : "Fox",
    3715 : "God",
    959 : "Hero",
    757 : "In",
}
# This dictionary is cool,but the key is not only can use string，but also can use number .
print(num_Dictionary.get(1))
print(num_Dictionary.get(959))