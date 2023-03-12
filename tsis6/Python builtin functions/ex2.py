def upperlowers(string):
    upper = 0
    lower = 0
    for i in range(len(string)):
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122):
            lower += 1
        elif (ord(string[i]) >= 65 and
            ord(string[i]) <= 90):
            upper += 1
    print('Lower case = ',lower,
		'Upper case =' ,upper)
str = 'I am The Heavy Weapons Guy'
print(upperlowers(str))