file= open('test.txt')

#print(file.read(7))#read till 7 characters and will include enter as well


#print(file.readline())
#print(file.readline()) #read one single line


#print line by line using Readline
#line=file.readline()
#while line!="":
 #   print(line)
  #  line=file.readline()
for line in file.readlines():
    print(line)
file.close()

