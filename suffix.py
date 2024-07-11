user = input("Enter a string: ")
lis = ["ful", "ment", "ion", "age", "dom", "ee", "hood", "ness", "ship", "ir", "ous", "ly", "ian", "ive", "ish", "ese", "en", "able", "ible", "ify", "ate", "ity", "ty", "ist", "ism", "er", "or", "ance", "ence", "al"]
emp = []

if user[-2:] in lis:
    emp.append(user[-2:])
    emp.append(user[0:-2] + "##")
    print(emp)

elif user[-3:] in lis:
    emp.append(user[-3:])
    emp.append(user[0:-3] + "###")
    print(emp)

elif user[-4:] in lis:
    emp.append(user[-4:])
    emp.append(user[0:-4] + "####")
    print(emp)

else:
    print("Wala")
