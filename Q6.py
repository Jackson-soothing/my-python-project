import re

#open and read the file
file = open('my file.txt', 'r')
text = file.read()

'''
I expect all the date formats are same as those listed 
in the question, no strange patterns like 111/01/2019, or 20178/01/09, or
05 Mon 2020 etc. 
otherwise the pattern setting in the code 
should be more precise to match those listed in the question
'''
#format a,b,c actually could be treated as the same type
format_abc = re.findall(r'(\d+/\d+/\d+)', text)

#find format d
format_d = re.findall(r'(\d{2} [a-zA-Z]{3} \d{4})', text)

#get the total no. of 'date'
print(len(format_abc) + len(format_d))

file.close()
