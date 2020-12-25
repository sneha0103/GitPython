#read the file and store all the lines in lisy
#Reverse the list
#write it back to the file
with open('test.txt','r') as Reader:
    content= Reader.readlines()
    reversed(content)
with open('test.txt','w') as Writer:
    for line in reversed(content):
        Writer.write(line)





