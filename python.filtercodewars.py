import re

def filter_string(item):
    #res = re.search('\S+',item)
    print item 
    res = isinstance(item,str)
    print res 
    if res:
       return 1
    return 0

def filter_list(l):
    indx=0
    #for i in range (1, len(l)):
    for i in l:
        print ">>S"
        print i
        print ">>E"
        indx = indx+1
        if filter_string(i):
            l.pop(indx-1)
    return l

#print filter_list([1,2,3,'forty five'])
print filter_list ([1,2,'a','b'])
#print filter_list([1,'a','b',0,15])
#print filter_list([1,2,'aasf','1','123',123])
