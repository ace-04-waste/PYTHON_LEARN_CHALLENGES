import re 
text = open('test.txt','r')
for line in text:
    line = line.strip()
    if re.search('^F..m:',line):
        print(line)