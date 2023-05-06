a = str(input("enter first string"))
b = str(input("enter second string"))
x = [i for i in a]
y = [i for i in b]


for i in range(0,len(x)):
    for j in range(0,len(y)):
        if(x[i] == y[j]):
            y[j] = 0
            


if(len(x) == y.count(0)):
    print("true")

else:
    print("false")

            



