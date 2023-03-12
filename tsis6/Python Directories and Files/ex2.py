import os
print('Exist:', os.access('C:\ProgramData', os.F_OK))
print('Readable:', os.access('C:\ProgramData', os.R_OK))
print('Writable:', os.access('C:\ProgramData', os.W_OK))
print('Executable:', os.access('C:\ProgramData', os.X_OK))