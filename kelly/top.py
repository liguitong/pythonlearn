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
try:
    with open('./kelly/james.txt','r') as jaf:
        data = jaf.readline()
        james = data.strip().split(',')
    with open('./kelly/mikey.txt','r') as mif:
        data =mif.readline()
        mikey = data.strip().split(',')
    with open('./kelly/sarah.txt','r') as saf:
        data = saf.readline()
        sarah = data.strip().split(',')
    with open('./kelly/julie.txt','r') as juf:
        data = juf.readline()
        julie = data.strip().split(',')
except IOError as err:
    print('File Error: ' +str(err))
clean_james=[sanitize(each_t) for each_t in james]
clean_mikey=[sanitize(each_t) for each_t in mikey]
clean_sarah=[sanitize(each_t) for each_t in sarah]
clean_julie=[sanitize(each_t) for each_t in julie]

print(sorted(clean_james))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
print(sorted(clean_julie))
