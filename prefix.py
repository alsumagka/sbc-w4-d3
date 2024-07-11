user = input("Enter a string: ")
lis = ["pre", "un", "re", "auto-", "dis", "il", "im", "in", "ir", "mis", "anti-", "mega", "pro", "semi-", "semi", "sub", "sub-"]
emp = []

if user[0:2] in lis:
    emp.append(user[0:2])
    emp.append("##" + user[2:])
    print(emp)

elif user[0:3] in lis:
    emp.append(user[0:3])
    emp.append("###" + user[3:])
    print(emp)

elif user[0:4] in lis:
    emp.append(user[0:4])
    emp.append("####" + user[4:])
    print(emp)

elif user[0:5] in lis:
    emp.append(user[0:5])
    emp.append("#####" + user[5:])
    print(emp)

else:
    print("Wala")
