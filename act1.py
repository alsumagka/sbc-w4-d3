user = input("Enter something: ")
lis = []
new = []
for i in user:
    if i.isalpha():
        lis.append(i)
    
    elif i == " ":
        var = "".join(lis)
        new.append(var)
        lis.clear()

neww = "".join(lis)
new.append(neww)
print(new)