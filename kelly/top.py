""" the fastest score of runner"""
import nester

def sanitize(time_string):
    if('-' in time_string):
        splitter = '-'
    elif(':' in time_string):
        splitter = ':'
    else:
        return time_string

    (mins,secs)  =time_string.split(splitter)
    return (mins + '.' + secs)
class AthleteList(list):
    ''' the athlete class extend list'''
    def __init__(self, a_name,a_dob=None, a_times=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_times)
    def top(self,num):
        return sorted(set([sanitize(t) for t in self]))[0:num]
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            temp = data.strip().split(',')
            return AthleteList(temp.pop(0), temp.pop(0), temp)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
print(james.name +"'s fastest times are: " + str(james.top(3)))
print(julie.name +"'s fastest times are: " + str(julie.top(3)))
print(mikey.name +"'s fastest times are: " + str(mikey.top(2)))
print(sarah.name +"'s fastest times are: " + str(sarah.top(3)))

