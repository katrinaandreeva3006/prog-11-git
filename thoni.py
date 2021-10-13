f = open("demofile.txt", "r")
#print(f.readline())
#print(f.readline())
#print(f.readline())
#for x in f:
   # print(x)
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())