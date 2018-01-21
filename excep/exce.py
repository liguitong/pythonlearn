import os
""" A test program to test exception"""
try:
    data=open('/home/lgt/Program/pythonlearn/excep/sketch.txt')
    for each_line in data:
        try:
            if not each_line.find(':')== -1:
                (role,line_spoken) = each_line.split(':',1)
                print(role,end='')
                print(' said:',end='')
                print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print("The datafile is missing")

