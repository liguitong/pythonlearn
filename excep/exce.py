import os
import nester
""" A test program to test exception"""
man = []
other = []
try:
    data=open('/home/lgt/Program/pythonlearn/excep/sketch.txt')
    for each_line in data:
        try:
            if not each_line.find(':')== -1:
                (role,line_spoken) = each_line.split(':',1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("The datafile is missing")
try:
    with open('man_data.txt', 'w') as man_data,open('other_data.txt', 'w') as other_data:
        nester.print_lol(man,fh=man_data)
        nester.print_lol(other,fh=other_data)
except IOError as err:
    print("Can't not write to file" + str(err))
finally:
    man_data.close()
    other_data.close()
