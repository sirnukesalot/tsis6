import os
filePath = 'C:\XboxGames\boom.txt';
if os.path.exists(filePath) and os.access("boom.txt", os.R_OK): 
    os.remove(filePath)
else:
    print("File doesn't exist")