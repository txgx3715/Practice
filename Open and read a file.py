#If you want to read some file out of you file
#You can use "open"

#You should be watch "\" is escapes,so you need use "\\" to explain to python or use "r"
#Add r in front of the path, which means to process as the original character.
Hamlet = open(r'C:\Users\ASUS\Desktop\test.txt', "r")
    #                       print(Hamlet.read())

#You have mant mode like "r"(read),"w"(write),"a"(append),"r+"(read + write)

#You can also use " .close " to close this file

#And you can read a line in you file 

#         print(Hamlet.readline())

#And you can use readlins put all string in a list.

#        print(Hamlet.readlines())

#You can also choose what's you should line.

#Like this etc.

#print(Hamlet.readlines()[1])



#It can use in for loop.
for words in Hamlet.readlines():
    print(words)

Hamlet.close()

