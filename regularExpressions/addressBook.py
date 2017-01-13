import re
from Carbon.Fonts import times

names_file = open("names.txt")
data = names_file.read()
names_file.close()

#print(data)

#print(re.match(r'mohan', data))

#print(re.search(r'kumar', data))

#parenthesis have special meaning
print(re.findall(r'\(\d{3}\) \d{3}-\d{4}', data))

print(re.findall(r'\w+, \w+', data))

#{3} - exactly 3 times
#{,3} - 0-3 times
#{3,5} - 3,4,5 times
#? - optional (0 or 1 time)
#* (o or many times)
#+ atleast 1 time
#\d number
#\w any character


#




