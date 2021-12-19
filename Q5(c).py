# i've alr clone the git repo to local, i can deal with that now

import glob
import re

#get all the files in the desired folder
files = glob.glob("/Users/soothing/git/my-python-project/*")


def check_def(line):
    m = re.match(r'(^[\s]*def\s.*:)' , line)
    if m:
        return True
    else:
        return False
    
def count_functions(file_name):
    
    f = open(file_name, 'r')
    
    count=0
    
    for i in f.readlines():
        if check_def(i):
            count = count + 1
            
    return count

counts = []
for i in files:
    counts.append(count_functions(i))

print("Totoal functions defined: " + str(sum(counts)))
