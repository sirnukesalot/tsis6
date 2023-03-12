with open('aaaa.txt','r') as firstfile, open('a.txt','w') as secondfile:
    for letters in firstfile:
             secondfile.write(letters)