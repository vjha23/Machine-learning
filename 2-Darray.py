import numpy as np
import random
n1=np.arange(6).reshape(3,2)
n2=np.arange(42).reshape(6,7)
for i in range(3):
    for j in range(2):
        n1[i][j]=random.randint(1,10)
for i in range(6):
    for j in range(7):
        n2[i][j]=random.randint(1,50)
print(n1)
print(n2)
#storing into file
f=open("array1.txt","w+")
f.write(str(n1))
f.close()
f=open("array1.txt",'r')
show=f.read()
print(show)

f1=open("array2.txt",'w+')
f1.write(str(n2))
f1.close()

f1=open("array2.txt","r")
show2=f1.read()
print(show2)