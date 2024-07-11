user = input("Enter something: ")
lis = []
new = []

for i in user:
    if i.isalnum() or i == " " or i == "." or i == "'":
        lis.append(i)
    
    elif i == ":" or i == "?" or i == "!" or i == ";" or i == "~" or i == "-" or i == "@":
        if lis[0] == " ":
            lis[0] = ""
        lis.append(i)
        var = "".join(lis)
        new.append(var)
        lis.clear()

if lis[0] == " ":
    lis[0] = ""
neww = "".join(lis)
new.append(neww)
print(new)