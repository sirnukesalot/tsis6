color = ['M', 'O', 'R', 'N', 'I', 'N', 'G']
with open('aaaa.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('aaaa.txt')
print(content.read())