string1 = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
string2 = string1.rstrip(' ')
print(string2)
string3 = string2.lstrip(' ')
print(string3)
pairs = string3.split('&')
print(pairs)


