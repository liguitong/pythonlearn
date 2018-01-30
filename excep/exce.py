import os
import nester
import pickle
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
    with open('man_data.txt', 'wb') as man_data,open('other_data.txt', 'wb') as other_data:
        pickle.dump(man, man_data)
        pickle.dump(other,other_data)
except IOError as err:
    print("Can't not write to file" + str(err))
except pickle.PickleError as perr:
    print('Pickling Error:' + str(perr))
finally:
    man_data.close()
    other_data.close()
