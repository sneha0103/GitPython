ItemsInCart = 0
#if ItemsInCart != 2: # raise Exception("Item count not matched")
    #pass

#assert(ItemsInCart == 2)
try:
 with open('filelog.txt', 'r') as Reader:
    Reader.read()

except:
 print("Failure in Try Block")

try:
 with open('filelog.txt', 'r') as Reader:
    Reader.read()

except Exception as e:
 print(e)

finally:
    print("cleaning up resource")

